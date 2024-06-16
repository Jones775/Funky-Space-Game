import pygame
import copy
import datetime

#Variables

#These Variables are used for functions which have to be executed twice or more, so they can save values for the second run
mouse_was_pressed = False
start_x = None
start_y = None
end_x = None
end_y = None

#This function is used by the scroll function to move all objects
def move_all_objects_on_screen(all_objects_on_screen, offset):
    for element in all_objects_on_screen:
        element.coordinates[0] += offset[0]
        element.coordinates[1] += offset[1]


#This function checks if the mouse was pressed and then released and checks if the mouse was moved. If this is the case, all objects on the screen will move too
def scroll(all_objects_on_screen, mouse_was_pressed, start_x, start_y, end_x, end_y):
    
    if mouse_was_pressed:
        if not pygame.mouse.get_pressed()[0]:
            #Mouse was released
            end_x, end_y = pygame.mouse.get_pos()
            mouse_was_pressed = False
            start_x = None
            start_y = None
            end_x = None
            end_y = None
            
        else:
            #get mouse position
            end_x, end_y = pygame.mouse.get_pos()
            #Calculate offset
            x_offset = end_x - start_x
            #The y-Axis is upside down so the order is different
            y_offset = end_y - start_y

            start_x = end_x
            start_y = end_y
            end_x = None
            end_y = None
            
            #Move all objects on screen
            move_all_objects_on_screen(all_objects_on_screen, (x_offset, y_offset))

    else:  
        if pygame.mouse.get_pressed()[0]:
            #Mouse was pressed
            start_x, start_y = pygame.mouse.get_pos()
            mouse_was_pressed = True
            
    return mouse_was_pressed, start_x, start_y, end_x, end_y

#This function is used bvy the zoom function
def scale_all_objects(all_objects_on_screen, zoom):

    #Objects cannot appear bigger than that
    upper_zoom_limit = 2500
    #Objects cannot appear smaller than that
    lower_zoom_limit = 20
    #Objects get added this size when you zoom once
    zoom_factor = 10

    #Check if zoom limit is reached
    for object in all_objects_on_screen:
        hypothetical_scale_x = (object.scale[0] - zoom * 10)
        hypothetical_scale_y = (object.scale[1] - zoom * 10) 
        if hypothetical_scale_x <= lower_zoom_limit or hypothetical_scale_y <= lower_zoom_limit or hypothetical_scale_x > upper_zoom_limit or hypothetical_scale_y > upper_zoom_limit:
            return 1

    for object in all_objects_on_screen:
        #Calculate the Size ratio
        size_ratio = object.scale[1] / object.scale[0]
        #if the zoom is positiv, the objects should get smaller
        object.scale[0] -= zoom * zoom_factor
        object.scale[1] = object.scale[0] * size_ratio
 
def distance_of_all_objects_to_mouse(all_objects_on_screen):
    all_distances = {}
    mouse_position = pygame.mouse.get_pos()

    for object in all_objects_on_screen:
        coordinates = object.coordinates
        x_offset = coordinates[0] - mouse_position[0]
        y_offset = coordinates[1] - mouse_position[1]
        all_distances[object] = [x_offset, y_offset]
    return all_distances

#This function returns a dictionary which has a specific object as key and as value another dictionary which has the other objects as keys and the distance of the first object as value
def distance_of_all_objects_to_each_other(all_objects_on_screen):
    distances = {}
    for start_object in all_objects_on_screen:
        single_distance = {}
        
        for end_object in all_objects_on_screen:
            if end_object is not start_object:
                x_distance = start_object.coordinates[0] - end_object.coordinates[0]
                y_distance = start_object.coordinates[1] - end_object.coordinates[1]
                single_distance[end_object] = [x_distance, y_distance]
        distances[start_object] = single_distance
    return distances


#This function moves all objects away from each other
#The function is used in the zooming function to create the effect of all objects getting smaller and moving away from each other
def move_all_objects_away_from_each_other(zoom, all_objects_on_screen):
    
    distances = distance_of_all_objects_to_each_other(all_objects_on_screen)
    num_objects = len(all_objects_on_screen)

    distances_to_mouse = distance_of_all_objects_to_mouse(all_objects_on_screen)
    distances["Mouse"] = distances_to_mouse

    #Calculate a new position for every object
    for start_object in distances:
        #The vector to the new position of the object
        x_offset = 0
        y_offset = 0
        if start_object != "Mouse":
            for end_object in distances[start_object]:
                dist_to_obj = distances[start_object][end_object]
                
                
                x_offset += dist_to_obj[0]
                y_offset += dist_to_obj[1]

            x_offset = x_offset / (num_objects * -10 * zoom)
            y_offset = y_offset / (num_objects * -10 * zoom)
            start_object.change_coordinates((x_offset, y_offset))








def zooming(event, all_objects_on_screen):
    if event.type == pygame.MOUSEWHEEL:
        zoom = event.y
        

        err = scale_all_objects(all_objects_on_screen, zoom)
        if err == 1:
            return 1
        else:
            #TODO This whole function is very inefficient and unperforming, that causes the bug that if you zoom in very fast, the scale is changed 
            #but not the distance so the objects change their relative distance to each other
            move_all_objects_away_from_each_other(zoom, all_objects_on_screen)
            

def print_font(font, text, screen, coordinates):
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, coordinates)

def calculate_fps(times, counter, final_counter):

    if times[0] == 0:
        times[0] = datetime.datetime.now()
        times[1] = times[0] + datetime.timedelta(seconds=1)
        return times, counter, final_counter
    elif datetime.datetime.now() < times[1]:
        counter += 1
        return times, counter, final_counter
    elif datetime.datetime.now() >= times[1]:
            
            times[0] = 0
            times[1] = 1
            final_counter = counter
            counter = 0
            return times, counter, final_counter


    
           
            


   
def print_all_objects(screen, all_objects_on_screen):
    for object in all_objects_on_screen:
        print_object(screen, object)

def print_object(screen, object):

    object_image = pygame.image.load(object.texture).convert_alpha()
    object_image = pygame.transform.scale(object_image, object.scale)
    
    #Pygame blits the image at upper left side as the middle, but it should be printed with the middle as the middle
    height = object_image.get_height()
    width = object_image.get_width()

    y_offset = height / 2
    x_offset = width / 2
    real_coordinates = [object.coordinates[0] - x_offset, object.coordinates[1] - y_offset]

    screen.blit(object_image, real_coordinates)
    



def quit_game(event, running):

    if event.type==pygame.QUIT:
        running=False
    return running


#TODO
def check_if_mouse_position_is_between_coordinates():
    pass

def print_start_screen(screen, screen_scale, event, start_screen_bool, background):
    
    screen.blit(background, (0,0))

    start_game_width = 600
    start_game_height = 400
    start_game = pygame.image.load("textures\\other_textures\\Start_Game.png")
    start_game = pygame.transform.scale(start_game, (start_game_width, start_game_height))
    
    position = ((screen_scale[0] / 2) - (start_game_width/2), (screen_scale[1] / 3) - (start_game_height /2))
    screen.blit(start_game, position)


    #while True:
        #pass