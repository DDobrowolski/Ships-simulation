import sys, pygame, pygame_gui
pygame.init()


pygame.display.set_caption('Ship simulator')
window_surface = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600), 'graphics/theme.json')

background = pygame.Surface((800, 600))
background.fill(manager.ui_theme.get_colour(None, None, 'dark_bg'))

start_simulation = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 280), (150, 40)),
                                            text='Start Simulation',
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