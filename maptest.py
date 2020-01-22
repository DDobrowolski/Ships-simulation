import pygame
import sys
from pygame import *
from helpers.Vector2 import Vector2
from models.Ship import Ship
from helpers.load_ports import load_from_csv

pygame.init()

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768

BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Symulator okrętów')


def main():
    # Instancje portów ładowane z csv
    available_ports = [Gdynia, Malmo, Goteborg, Tallin] = load_from_csv()
    # Instancje statków
    Sztygar = Ship('Sztygar', (220, 80), Malmo, None, None,
                   None, None, None, None, available_ports)
    Wilk = Ship('Wilk', (550, 80), Goteborg, None, None, None,
                None, None, None, available_ports)
    Burza = Ship('Burza', (200, 680), Tallin, None, None,
                 None, None, None, None, available_ports)
    Piorun = Ship('Piorun', (830, 600), Gdynia, None, None,
                  None, None, None, None, available_ports)

    # ładowanie obrazu statku
    ship_img = pygame.image.load('graphics/ship.png').convert()
    ship_img = pygame.transform.scale(ship_img, (120, 37))
    ship_img.set_colorkey(BLACK)

    # ładowanie tła z mapą
    background = pygame.image.load('graphics/mapa.png').convert()
    background_rect = background.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for ship in (Sztygar, Wilk, Burza, Piorun):
                    ship.move()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for ship in (Sztygar, Wilk, Burza, Piorun):
            ship.update()
       # wyświetlanie
        DISPLAYSURF.fill(BLACK)

        DISPLAYSURF.blit(background, background_rect)

        # wyświetlanie elementów
        Sztygar_rect = ship_img.get_rect(
            x=Sztygar.position.get_x(), y=Sztygar.position.get_y())
        Wilk_rect = ship_img.get_rect(
            x=Wilk.position.get_x(), y=Wilk.position.get_y())
        Burza_rect = ship_img.get_rect(
            x=Burza.position.get_x(), y=Burza.position.get_y())
        Piorun_rect = ship_img.get_rect(
            x=Piorun.position.get_x(), y=Piorun.position.get_y())

        DISPLAYSURF.blit(ship_img, Sztygar_rect)
        DISPLAYSURF.blit(ship_img, Wilk_rect)
        DISPLAYSURF.blit(ship_img, Burza_rect)
        DISPLAYSURF.blit(ship_img, Piorun_rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()
