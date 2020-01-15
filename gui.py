import sys, pygame, pygame_gui
pygame.init()

pygame.display.set_caption('Symulator okrętów')
window_surface = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600))

background = pygame.Surface((800, 600))
background.fill(manager.ui_theme.get_colour(None, None, 'dark_bg'))
## Wybierz port startowy
start_point = pygame_gui.elements.UIDropDownMenu(options_list=['Gdynia', 'Katar', 'Porto', 'Malmo'],
                                    starting_option='Gdynia',
                                    relative_rect=pygame.Rect((300, 100), (250, 40)),
                                    manager=manager)
## Wybierz port docelowy
final_point = pygame_gui.elements.UIDropDownMenu(options_list=['Gdynia', 'Katar', 'Porto', 'Malmo'],
                                    starting_option='Katar',
                                    relative_rect=pygame.Rect((300, 150), (250, 40)),
                                    manager=manager)
## Wybierz ładunek
select_cargo = pygame_gui.elements.UIDropDownMenu(options_list=['Drewno', 'Stal', 'Ropa', 'Piasek'],
                                    starting_option='Drewno',
                                    relative_rect=pygame.Rect((300, 200), (250, 40)),
                                    manager=manager)
## Start symulacji
start_simulation = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 280), (250, 40)),
                                            text='Rozpocznij symulację',
                                            manager=manager)



pygame.mouse.set_pos(20, 15)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if (event.type == pygame.USEREVENT and event.user_type == 'ui_button_pressed' and
                event.ui_element == start_simulation):
            print('Start symulacji!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()