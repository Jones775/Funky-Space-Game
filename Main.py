import pygame
import time
from Spaceships import *
import Buildings
from functions import *
from Space_Bodies import *


screen_width = 1500
screen_height = 800

pygame.init()
pygame.display.set_caption("Funky Space Game")
background = pygame.image.load("textures\\other_textures\\Background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

#Pygame Variable
screen = pygame.display.set_mode((screen_width, screen_height))


all_objects_on_screen = []

#This variables are used to calculate the frames per second
times = [0,0]
temp_counter = 0
frame_counter = 0


#Fonts
freesansbold_font = pygame.font.Font('freesansbold.ttf', 32)






small_sf = Small_Starfighter([800, 600], all_objects_on_screen)
cargo_vs = Cargo_Vessel([400, 500], all_objects_on_screen)
small_sf2 = Small_Starfighter([900, 500], all_objects_on_screen)
small_sf3 = Small_Starfighter([600, 300], all_objects_on_screen)
battle_cr = Battle_Cruiser([650, 100], all_objects_on_screen)
carrier_s = Carrier_Ship([900, 600], all_objects_on_screen, [])
blockade_r = Blockade_Runner([1000, 500], all_objects_on_screen)

planet1 = Planet([100, 400], all_objects_on_screen)



desti = [100, 900]


start_screen_bool = True
running = True
while running:
    
    
    for event in pygame.event.get():
        
        

        screen.blit(background, (0,0))

        #Printing Frames per Second
        times, temp_counter, frame_counter = calculate_fps(times, temp_counter, frame_counter)
        print_font(freesansbold_font, f"FPS: {frame_counter}", screen, (10, 10))
            


        running = quit_game(event, running)
        

        if start_screen_bool:
            start_screen_bool = print_start_screen(screen, (screen_width, screen_height), event, start_screen_bool, background)
        else:
            mouse_was_pressed, start_x, start_y, end_x, end_y = scroll(all_objects_on_screen, mouse_was_pressed, start_x, start_y, end_x, end_y)
            zooming(event, all_objects_on_screen)

            print_all_objects(screen, all_objects_on_screen)

            #desti = blockade_r.fly(desti, all_objects_on_screen)

        

    
    
    
    

    pygame.display.flip()