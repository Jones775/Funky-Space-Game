import pygame
import time

pygame.init()

#Pygame Variable
screen = pygame.display.set_mode((1500, 800))



ship_image = pygame.image.load('textures\\spaceship_textures\\Battle_Cruiser.png').convert()
ship_image = pygame.transform.scale(ship_image, (400, 200))



ship2 = pygame.image.load('textures\\spaceship_textures\\Small_Starfighter.png').convert()
ship2 = pygame.transform.scale(ship2, (200, 100))


running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            running=False

        


    screen.blit(ship_image, (200, 100))
    screen.blit(ship2, (500, 500))
    pygame.display.flip()