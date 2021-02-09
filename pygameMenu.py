import pygame
import pygame_gui


pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 65)


pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600),0,32)
textsurface = myfont.render('Spanglish Matching!', False, (100, 200, 100))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#33FFFF'))

manager = pygame_gui.UIManager((800, 600))


start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 275), (150, 50)),
                                            text='Start!',
                                            manager=manager)

show_words_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 375), (150, 50)),
                                            text='Study Words',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    print('Start the Game!')
                if event.ui_element == show_words_button:
                    print('I will show you the words!')

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(textsurface,(130, 120))
    manager.draw_ui(window_surface)

    pygame.display.update()