import pygame

from pygame.locals import *
pygame.init()

#screen = pygame.display.set_mode([500,500])#setup
screen_width = 800
screen_height = 600 
screen = pygame.display.set_mode([screen_width,screen_height])

running = True 
while running :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

screen.fill([255,255,255])

surf = pygame.Surface((50,50))

surf.fill([0,0,0])
rect = surf.get_rect()

screen.blit(surf,(screen_width/2,screen_height/2))

surf_center = (screen_width - surf.get_width()/2,screen_height - surf.get_height()/2)
screen.blit(surf,surf_center)

#pygame.draw.circle(screen, [0,0,0], [250,250],75)
pygame.display.flip()

#pygame.quit()