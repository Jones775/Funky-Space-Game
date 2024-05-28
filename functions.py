import pygame

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

    for object in all_objects_on_screen:
        hypothetical_scale_x = (object.scale[0] - zoom * 10)
        hypothetical_scale_y = (object.scale[1] - zoom * 10) 
        if hypothetical_scale_x <= 0 or hypothetical_scale_y <= 0:
            return 1

    for object in all_objects_on_screen:
        #Calculate the Size ratio
        size_ratio = object.scale[1] / object.scale[0]

        #if the zoom is positiv, the objects should get smaller
        object.scale[0] -= zoom * 10
        object.scale[1] = object.scale[0] * size_ratio
 

def zooming(event, all_objects_on_screen):
    if event.type == pygame.MOUSEWHEEL:
        zoom = event.y
        scale_all_objects(all_objects_on_screen, zoom)

   
def print_all_objects(screen, all_objects_on_screen):
    for object in all_objects_on_screen:
        print_object(screen, object)

def print_object(screen, object):

    object_image = pygame.image.load(object.texture).convert_alpha()
    object_image = pygame.transform.scale(object_image, object.scale)

    screen.blit(object_image, object.coordinates)
    

def zoom():
    pass

def quit_game(event, running):

    if event.type==pygame.QUIT:
        running=False
    return running    