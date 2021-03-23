import pygame
import pygame_gui
import random
from pygameShowWords import display_study_words
from pygameGame import comienzo




def mainScreen(d,randomSample,window_surface,engList,spanList, mainScreenManager, gameTitle, bg):


    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 275), (150, 50)),
                                                text='Start!',
                                                #Place it in main manager
                                                manager=mainScreenManager)

    show_words_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 375), (150, 50)),
                                                text='Study Words',
                                                #Place it in main manager
                                                manager=mainScreenManager)

    exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((330, 475), (150, 50)),
                                                text='Exit',
                                                #Place it in main manager
                                                manager=mainScreenManager)

    #Create clock
    clock = pygame.time.Clock()
    is_running = True

    #Background scrolling parameters

    i = 0
    
    #Main game loop
    while is_running:
        time_delta = clock.tick(60)/1000.0

        #Needed (but don't know why)
        for event in pygame.event.get():
            #'X' top right closes game
            if event.type == pygame.QUIT:
                is_running = False

            #Check if something we created is processed
            if event.type == pygame.USEREVENT:
                # Make sound when hovering over button
                # if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                #     pygame.mixer.Sound.play(first_sound)

                # If button is pressed
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    # If start button, start
                    if event.ui_element == start_button:
                        comienzo(window_surface, randomSample, engList, spanList)
                    # If study button, study
                    if event.ui_element == show_words_button:
                        display_study_words(d,randomSample,window_surface,engList,spanList)
                    # If exit, exit
                    if event.ui_element == exit_button:
                        is_running = False
            
            #Process buttons
            mainScreenManager.process_events(event)


        #Denis changes
        #Scrolling background
        window_surface.blit(bg, (i, 0))
        window_surface.blit(bg, (800+i, 0))
        #If image is at end, wrap image around
        if i == -800:
            window_surface.blit(bg, (800+i, 0))
            #Reset i
            i = 0
        #Decrement i
        i -= 1
        ####

        #Display title
        window_surface.blit(gameTitle,(95, 120))
        #Update button logic
        mainScreenManager.update(time_delta)
        #Display buttons
        mainScreenManager.draw_ui(window_surface)

        #Show the display
        pygame.display.update()




#A main function to initalize all important variables for the start up
def main():
    pygame.init()
    pygame.font.init() # you have to call this at the start, 
                       # if you want to use this module.

    titleFont = pygame.font.SysFont('Cooper Black', 65)

    width = 800
    height = 600

    pygame.display.set_caption('Spanglish Matching')
    window_surface = pygame.display.set_mode((width, height),0,32)
    gameTitle = titleFont.render('Spanglish Matching!', False, (0, 0, 0))

    #Denis Changes
    bg_img = pygame.image.load('worldmap1024.jpg')
    bg = pygame.transform.scale(bg_img, (width, height))
    ####

    mainScreenManager = pygame_gui.UIManager((width, height))
    first_sound = pygame.mixer.Sound("crash.mp3")

    backgroundMusic = pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(0.06)
    pygame.mixer.music.play(-1)


    # dictionary with the spanish and english words
    d = {'english':['T-shirt','pants','skirt','socks','coat','shoes','boots',
                        'love','happy','tired','ready','box','wheel','can','wallet',
                        'screen','keyboard','bed','belt','glove','year','day','time',
                        'time(period of)','life','part','government','country','world',
                        'state','yes','of course','maybe',"I don't know",'how','I','you',
                        'place','the','she'],
    'spanish':['la camiseta','los pantalones','la falda','los calcetines','el abrigo',
                    'los zapatos','las botas','amor','feliz','consado','listo','cajón','rueda','lata',
                    'billetera','pantalla','teclado','cama','cinturón','guante','año','día','vez',
                    'tiempo','vida','parte','gobierno','país','mundo','estado','si','claro que si','talvez',
                    'nose','cómo','yo','tu','lugar','el/la','ella']}

    # Select 12 indeces for english and spanish words
    randomSample = random.sample(list(range(len(d['english']))), 12)

    # English list, Spanish list
    engList  = []
    spanList = []


    #Generate english/spanish lists, with corresponding indeces
    for x in randomSample:
        engList.append( d['english'][x])
        spanList.append(d['spanish'][x])

    #Call the main screen
    mainScreen(d,randomSample,window_surface,engList,spanList, mainScreenManager, gameTitle, bg)


#Call main
main()