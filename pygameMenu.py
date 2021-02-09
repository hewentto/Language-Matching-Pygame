import pygame
import pygame_gui


pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('jokerman', 65) #jokerman, showcardgothic, magneto, franklingothicheavy, impact


pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600),0,32)
textsurface = myfont.render('Spanglish Matching!', False, (100, 200, 100))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#33FFFF'))

manager = pygame_gui.UIManager((800, 600))
first_sound = pygame.mixer.Sound("crash.mp3")

backgroundMusic = pygame.mixer.music.load("funky.mp3")
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(-1)




start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 275), (150, 50)),
                                            text='Start!',
                                            manager=manager)

show_words_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 375), (150, 50)),
                                            text='Study Words',
                                            manager=manager)

exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 475), (150, 50)),
                                            text='Exit',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                pygame.mixer.Sound.play(first_sound)
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    print('Start the Game!')
                if event.ui_element == show_words_button:
                    print('I will show you the words!')
                if event.ui_element == exit_button:
                    print('Thanks for Playing!')

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(textsurface,(110, 120))
    manager.draw_ui(window_surface)

    pygame.display.update()