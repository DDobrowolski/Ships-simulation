import pygame, sys
from pygame import *
 
pygame.init() 
 
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
 
BLACK = (0,0,0)
 
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Symulator okrętów')
 
def main(): 
    
    #### ładowanie tła z mapą
    background = pygame.image.load('graphics/mapa.png').convert()
    background_rect = background.get_rect()

    #### ładowanie statków
    Sztygar_img = pygame.image.load('graphics/ship.png').convert()
    Sztygar_img = pygame.transform.scale(Sztygar_img, (120, 37))
    Sztygar_img.set_colorkey(BLACK)
    Sztygar_rect = Sztygar_img.get_rect(center=(224, 80))
 
    Wilk_img = pygame.image.load('graphics/ship.png').convert()
    Wilk_img = pygame.transform.scale(Wilk_img, (120, 37))
    Wilk_img.set_colorkey(BLACK)
    Wilk_rect = Wilk_img.get_rect(center=(864, 80))

    Burza_img = pygame.image.load('graphics/ship.png').convert()
    Burza_img = pygame.transform.scale(Burza_img, (120, 37))
    Burza_img.set_colorkey(BLACK)
    Burza_rect = Burza_img.get_rect(center=(286, 680))

    Piorun_img = pygame.image.load('graphics/ship.png').convert()
    Piorun_img = pygame.transform.scale(Piorun_img, (120, 37))
    Piorun_img.set_colorkey(BLACK)
    Piorun_rect = Piorun_img.get_rect(center=(830, 600))

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
       ##### wyświetlanie
        DISPLAYSURF.fill(BLACK)
        
        DISPLAYSURF.blit(background, background_rect)
        
        ##### wyświetlanie elementów
        DISPLAYSURF.blit(Sztygar_img, Sztygar_rect)
        DISPLAYSURF.blit(Wilk_img, Wilk_rect)
        DISPLAYSURF.blit(Burza_img, Burza_rect)
        DISPLAYSURF.blit(Piorun_img, Piorun_rect)
        
        pygame.display.flip()
 
if __name__ == "__main__":
    main()