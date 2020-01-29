import pygame
import pygame_gui


def generate_gui(manager, Rob, Bob, Mob, Lob):
    # Armator 1
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 10), (250, 40)),
                                text=Rob.name,
                                manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 40), (250, 40)),
                                text=f'Pieniądze: ${Rob.cash}',
                                manager=manager)

    # Armator 2
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 80), (250, 40)),
                                text=Bob.name,
                                manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 110), (250, 40)),
                                text=f'Pieniądze: ${Bob.cash}',
                                manager=manager)

    # Armator 3
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 150), (250, 40)),
                                text=Mob.name,
                                manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 180), (250, 40)),
                                text=f'Pieniądze: ${Mob.cash}',
                                manager=manager)

    # Armator 4
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 220), (250, 40)),
                                text=Lob.name,
                                manager=manager)

    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 250), (250, 40)),
                                text=f'Pieniądze: ${Lob.cash}',
                                manager=manager)

    # Wybierz port
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 400), (250, 40)),
                                text='Wybierz port:',
                                manager=manager)

    select_port = pygame_gui.elements.UIDropDownMenu(options_list=['Gdynia', 'Malmo', 'Goteborg', 'Tallin'],
                                                     starting_option='Gdynia',
                                                     relative_rect=pygame.Rect(
                                                         (1075, 440), (250, 40)),
                                                     manager=manager)

    # Wybierz statek
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 480), (250, 40)),
                                text='Wybierz statek:',
                                manager=manager)

    select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Piorun', 'Burza', 'Wilk', 'Sztygar'],
                                                      starting_option='Piorun',
                                                      relative_rect=pygame.Rect(
                                                          (1075, 520), (250, 40)),
                                                      manager=manager)

    # Wybierz armatora
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1075, 560), (250, 40)),
                                text='Wybierz armatora:',
                                manager=manager)

    select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Armator 1', 'Armator 2', 'Armator 3', 'Armator 4'],
                                                      starting_option='Armator 1',
                                                      relative_rect=pygame.Rect(
                                                          (1075, 600), (250, 40)),
                                                      manager=manager)

    # Statystyki Gdynia
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 768), (180, 40)),
                                text='Statystyki Gdynia:',
                                manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                                  relative_rect=pygame.Rect(
                                      (5, 805), (325, 150)),
                                  manager=manager)
    # Statystyki Malmo
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((335, 768), (180, 40)),
                                text='Statystyki Malmo:',
                                manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                                  relative_rect=pygame.Rect(
                                      (345, 805), (325, 150)),
                                  manager=manager)

    # Statystyki Goteborg
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((680, 768), (180, 40)),
                                text='Statystyki Goteborg:',
                                manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                                  relative_rect=pygame.Rect(
                                      (685, 805), (325, 150)),
                                  manager=manager)

    # Statystyki Tallin
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1015, 768), (180, 40)),
                                text='Statystyki Tallin:',
                                manager=manager)
    pygame_gui.elements.UITextBox(html_text="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.",
                                  relative_rect=pygame.Rect(
                                      (1025, 805), (325, 150)),
                                  manager=manager)
