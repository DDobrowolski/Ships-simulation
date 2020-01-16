import pygame, sys
from pygame import *
 
pygame.init() 
 
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
 
BLACK = (0,0,0)
 
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Symulator okrętów')
 
def main(): 
    
    background = pygame.image.load('graphics/mapa.png').convert()
    background_rect = background.get_rect()
 
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
       
        DISPLAYSURF.fill(BLACK)
        
        DISPLAYSURF.blit(background, background_rect)
 
        
        pygame.display.flip()
 
if __name__ == "__main__":
    main()