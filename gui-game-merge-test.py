import pygame
import sys
import pygame_gui
from pygame import *
from helpers.Vector2 import Vector2
from models.Ship import Ship
from helpers.load_ports import load_from_csv

pygame.init()

WINDOWWIDTH = 1366
WINDOWHEIGHT = 960

BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Symulator okrętów')
manager = pygame_gui.UIManager(((WINDOWWIDTH, WINDOWHEIGHT)), 'graphics/theme.json')


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
    
    ## Elementy GUI

    ## Armator 1
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 0), (250, 10)),
                             text='..............................................',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 10), (250, 40)),
                             text='ARMATOR 1',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 40), (250, 40)),
                             text='Pieniądze: 2000 zł',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 70), (250, 10)),
                             text='..............................................',
                             manager=manager)

    ## Armator 2
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 80), (250, 40)),
                             text='ARMATOR 2',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 110), (250, 40)),
                             text='Pieniądze: 2000 zł',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 140), (250, 10)),
                             text='..............................................',
                             manager=manager)

    ## Armator 3
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 150), (250, 40)),
                             text='ARMATOR 3',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 180), (250, 40)),
                             text='Pieniądze: 2000 zł',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 210), (250, 10)),
                             text='..............................................',
                             manager=manager)

    ## Armator 4
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 220), (250, 40)),
                             text='ARMATOR 4',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 250), (250, 40)),
                             text='Pieniądze: 2000 zł',
                             manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 280), (250, 10)),
                             text='..............................................',
                             manager=manager)

    ## Wybierz port
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 400), (250, 40)),
                             text='Wybierz port:',
                             manager=manager)

    select_port = pygame_gui.elements.UIDropDownMenu(options_list=['Gdynia', 'Malmo', 'Goteborg', 'Tallin'],
                                    starting_option='Gdynia',
                                    relative_rect=pygame.Rect((1075, 440), (250, 40)),
                                    manager=manager)

    ## Wybierz statek
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 480), (250, 40)),
                             text='Wybierz statek:',
                             manager=manager)

    select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Piorun', 'Burza', 'Wilk', 'Sztygar'],
                                    starting_option='Piorun',
                                    relative_rect=pygame.Rect((1075, 520), (250, 40)),
                                    manager=manager)

    ## Wybierz armatora
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 560), (250, 40)),
                             text='Wybierz armatora:',
                             manager=manager)

    select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Armator 1', 'Armator 2', 'Armator 3', 'Armator 4'],
                                    starting_option='Armator 1',
                                    relative_rect=pygame.Rect((1075, 600), (250, 40)),
                                    manager=manager)                                    

    ## Start/stop symulacji
    start_simulation = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1075, 695), (250, 40)),
                                            text='Rozpocznij symulację',
                                            manager=manager)

    ## Statystyki Gdynia
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 768), (180, 40)),
                             text='Statystyki Gdynia:',
                             manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                            relative_rect=pygame.Rect((5, 805), (325, 150)),
                            manager=manager)
    ## Statystyki Malmo
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((335, 768), (180, 40)),
                             text='Statystyki Malmo:',
                             manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                            relative_rect=pygame.Rect((345, 805), (325, 150)),
                            manager=manager)

    ## Statystyki Goteborg
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((680, 768), (180, 40)),
                             text='Statystyki Goteborg:',
                             manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                            relative_rect=pygame.Rect((685, 805), (325, 150)),
                            manager=manager)

    ## Statystyki Tallin
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1015, 768), (180, 40)),
                             text='Statystyki Tallin:',
                             manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                            relative_rect=pygame.Rect((1025, 805), (325, 150)),
                            manager=manager)


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
        DISPLAYSURF.fill(manager.ui_theme.get_colour(None, None, 'dark_bg'))

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

        manager.draw_ui(DISPLAYSURF)

        pygame.display.flip()


if __name__ == "__main__":
    main()
