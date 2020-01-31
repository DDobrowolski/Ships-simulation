import pygame
import pygame_gui
import json


class GUI:
    def __init__(self, manager, owners, ships):
        self.manager = manager
        self.owner1, self.owner2, self.owner3, self.owner4 = owners
        self.ship1, self.ship2, self.ship3, self.ship4 = ships

        self.owner1_cash = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 40), (250, 40)),
                                                       text=f'Pieniądze: ${self.owner1.cash}',
                                                       manager=manager)
        self.owner2_cash = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 110), (250, 40)),
                                                       text=f'Pieniądze: ${self.owner2.cash}',
                                                       manager=manager)
        self.owner3_cash = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 180), (250, 40)),
                                                       text=f'Pieniądze: ${self.owner3.cash}',
                                                       manager=manager)
        self.owner4_cash = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 250), (250, 40)),
                                                       text=f'Pieniądze: ${self.owner4.cash}',
                                                       manager=manager)

        self.ship1_stats = pygame_gui.elements.UITextBox(html_text=self.ship1.to_string(),
                                                         relative_rect=pygame.Rect(
                                                             (5, 805), (325, 150)),
                                                         manager=manager)
        self.ship2_stats = pygame_gui.elements.UITextBox(html_text=self.ship2.to_string(),
                                                         relative_rect=pygame.Rect(
                                                             (345, 805), (325, 150)),
                                                         manager=manager)
        self.ship3_stats = pygame_gui.elements.UITextBox(html_text=self.ship3.to_string(),
                                                         relative_rect=pygame.Rect(
            (685, 805), (325, 150)),
            manager=self.manager)
        self.ship4_stats = pygame_gui.elements.UITextBox(html_text=self.ship4.to_string(),
                                                         relative_rect=pygame.Rect(
            (1025, 805), (325, 150)),
            manager=self.manager)

    def update_owners_stats(self):
        owners = [self.owner1, self.owner2, self.owner3, self.owner4]
        owners_cash = [self.owner1_cash, self.owner2_cash,
                       self.owner3_cash, self.owner4_cash]
        for i, o_c in enumerate(owners_cash):
            o_c.set_text(f'Pieniądze: ${owners[i].cash}')

    def update_ships_stats(self):
        ships = [self.ship1, self.ship2, self.ship3, self.ship4]
        ships_stats = [self.ship1_stats, self.ship2_stats,
                       self.ship3_stats, self.ship4_stats]
        for i, ship_stat in enumerate(ships_stats):
            ship_stat.html_text = ships[i].to_string()
            ship_stat.rebuild()

    def generate_main_gui(self):
        # Armator 1
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 10), (250, 40)),
                                    text=self.owner1.name,
                                    manager=self.manager)

        # Armator 2
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 80), (250, 40)),
                                    text=self.owner2.name,
                                    manager=self.manager)
        # Armator 3
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 150), (250, 40)),
                                    text=self.owner3.name,
                                    manager=self.manager)

        # Armator 4
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 220), (250, 40)),
                                    text=self.owner4.name,
                                    manager=self.manager)

        # Wybierz port
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 400), (250, 40)),
                                    text='Wybierz port:',
                                    manager=self.manager)

        select_port = pygame_gui.elements.UIDropDownMenu(options_list=['Gdynia', 'Malmo', 'Goteborg', 'Tallin'],
                                                         starting_option='Gdynia',
                                                         relative_rect=pygame.Rect(
            (1075, 440), (250, 40)),
            manager=self.manager)

        # Wybierz statek
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 480), (250, 40)),
                                    text='Wybierz statek:',
                                    manager=self.manager)

        select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Piorun', 'Burza', 'Wilk', 'Sztygar'],
                                                          starting_option='Piorun',
                                                          relative_rect=pygame.Rect(
            (1075, 520), (250, 40)),
            manager=self.manager)

        # Wybierz armatora
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 560), (250, 40)),
                                    text='Wybierz armatora:',
                                    manager=self.manager)

        select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Armator 1', 'Armator 2', 'Armator 3', 'Armator 4'],
                                                          starting_option='Armator 1',
                                                          relative_rect=pygame.Rect(
            (1075, 600), (250, 40)),
            manager=self.manager)

        # Statystyki Sztygar
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 768), (180, 40)),
                                    text='Statystyki Sztygar:',
                                    manager=self.manager)

        # Statystyki Wilk
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((335, 768), (180, 40)),
                                    text='Statystyki Wilk:',
                                    manager=self.manager)

        # Statystyki Burza
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((680, 768), (180, 40)),
                                    text='Statystyki Burza:',
                                    manager=self.manager)

        # Statystyki Piorun
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1015, 768), (180, 40)),
                                    text='Statystyki Piorun:',
                                    manager=self.manager)
