import pygame
import sys
import pygame_gui
from pygame import *
from helpers.Vector2 import Vector2
from models.Ship import Ship
from models.Owner import Owner
from helpers.load_ports import load_from_csv
from helpers.save_sim import save_sim_to_json
from helpers.gui_gen import generate_gui

pygame.init()

WINDOWWIDTH = 1366
WINDOWHEIGHT = 960

BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Symulator okrętów')
manager = pygame_gui.UIManager(
    ((WINDOWWIDTH, WINDOWHEIGHT)), 'graphics/theme.json')


def main():
    clock = pygame.time.Clock()
    # Instancje portów ładowane z csv
    available_ports = [Gdynia, Malmo, Goteborg, Tallin] = load_from_csv()
    # Instancje armatorów
    Rob = Owner('Rob', 200000)
    Bob = Owner('Bob', 200000)
    Mob = Owner('Mob', 200000)
    Lob = Owner('Lob', 200000)
    owners = [Rob, Bob, Mob, Lob]
    # Instancje statków
    Sztygar = Ship('Sztygar', (220, 80), Malmo, available_ports, Rob)
    Wilk = Ship('Wilk', (550, 80), Goteborg, available_ports, Bob)
    Burza = Ship('Burza', (200, 680), Tallin, available_ports, Mob)
    Piorun = Ship('Piorun', (830, 600), Gdynia, available_ports, Lob)
    ships = [Sztygar, Wilk, Burza, Piorun]
    # ładowanie obrazu statku
    ship_img = pygame.image.load('graphics/ship.png').convert()
    ship_img = pygame.transform.scale(ship_img, (120, 37))
    ship_img.set_colorkey(BLACK)

    # ładowanie tła z mapą
    background = pygame.image.load('graphics/mapa.png').convert()
    background_rect = background.get_rect()

    # Elementy GUI
    generate_gui(manager, Rob, Bob, Mob, Lob)
    # Start/stop symulacji
    start_stop_simulation = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1075, 695), (250, 40)),
                                                         text='Start/Stop symulacji',
                                                         manager=manager)
    is_running = False
    while True:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == USEREVENT and event.user_type == 'ui_button_pressed' and event.ui_element == start_stop_simulation:
                if not is_running:
                    is_running = True
                    for ship in ships:
                        ship.move()
                elif is_running:
                    save_sim_to_json(ships, owners, available_ports)
                    pygame.quit()
                    sys.exit()
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

        manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(DISPLAYSURF)

        pygame.display.update()


if __name__ == "__main__":
    main()
