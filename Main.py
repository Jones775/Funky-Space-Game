import pygame
import time

pygame.init()

#Pygame Variable
screen = pygame.display.set_mode((1500, 800))



ship_image = pygame.image.load('textures\\spaceship_textures\\Battle_Cruiser.png').convert_alpha()
ship_image = pygame.transform.scale(ship_image, (400, 200))



ship2 = pygame.image.load('textures\\spaceship_textures\\Small_Starfighter.png').convert_alpha()
ship2 = pygame.transform.scale(ship2, (200, 100))

ship3 = pygame.image.load('textures\\spaceship_textures\\Cargo_Vessel.png').convert_alpha()
ship3 = pygame.transform.scale(ship3, (200, 100))

running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            running=False

        

    screen.fill(pygame.Color("dark blue"))
    screen.blit(ship_image, (200, 100))
    screen.blit(ship2, (500, 500))
    screen.blit(ship3, (800, 600))
    

    pygame.display.flip()