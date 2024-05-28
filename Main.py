import pygame
import time
from Spaceships import *
import Buildings
from functions import *

pygame.init()

#Pygame Variable
screen = pygame.display.set_mode((1500, 800))

all_objects_on_screen = []



small_sf = Small_Starfighter([800, 600], all_objects_on_screen)
cargo_vs = Cargo_Vessel([400, 500], all_objects_on_screen)




running = True
while running:
    
    for event in pygame.event.get():
        

        screen.fill(pygame.Color("dark blue"))
        running = quit_game(event, running)

        mouse_was_pressed, start_x, start_y, end_x, end_y = scroll(all_objects_on_screen, mouse_was_pressed, start_x, start_y, end_x, end_y)
        zooming(event, all_objects_on_screen)

        print_all_objects(screen, all_objects_on_screen)

        

    
    
    
    

    pygame.display.flip()