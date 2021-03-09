
import pygame
from pygame.mouse import get_pos
import pygame_gui
import random


pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.


# myfont = pygame.font.SysFont('jokerman', 65) #jokerman, showcardgothic, magneto, franklingothicheavy, impact

titleFont = pygame.font.SysFont('Cooper Black', 65)

width = 800

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((width, 600),0,32)
gameTitle = titleFont.render('Spanglish Matching!', False, (0, 0, 0))

#Denis Changes
bg_img = pygame.image.load('worldmap1024.jpg')
bg = pygame.transform.scale(bg_img, (width, 600))

####

mainScreenManager = pygame_gui.UIManager((width, 600))
first_sound = pygame.mixer.Sound("crash.mp3")

backgroundMusic = pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(-1)

# dictionary with the spanish and english words
d = {'english':['T-shirt','pants','skirt','socks','coat','shoes','boots',
                    'love','happy','tired','ready','box','wheel','can','wallet',
                    'screen','keyboard','bed','belt','glove','year','day','time',
                    'time(period of)','life','part','government','country','word',
                    'state','yes','no','maybe',"I don't know",'how','I','you',
                    'place','the','she'],
'spanish':['la camiseta','los pantalones','la falda','los calcetines','el abrigo',
                'los zapatos','las botas','amor','feliz','consado','listo','cajón','rueda','lata',
                'billetera','pantalla','teclado','cama','cinturón','guante','año','día','vez',
                'tiempo','vida','parte','gobierno','país','mundo','estado','si','no','talvez',
                'nose','cómo','yo','tu','lugar','el/la','ella']}
# Select 12 indeces for english and spanish words
randomSample = random.sample(list(range(len(d['english']))), 12)

# i had to create a list of just strings because the other one used "render" functions and wouldnt pass into class objects correctly
engList = []
spanList = []


englishWords=[]
spanishWords=[]
# Every word that's not header
studyFont = pygame.font.SysFont('Cooper Black', 40)

    #Generate english/spanish lists, with corresponding indeces
for x in randomSample:
    engList.append(d['english'][x])
    spanList.append(d['spanish'][x])
    englishWords.append(studyFont.render(d['english'][x], False, (0, 0, 0)))
    spanishWords.append(studyFont.render(d['spanish'][x], False, (0, 0, 0)))

class word:
    def __init__(self, palabra, cosa):
        self.palabra = palabra
        self.cosa = cosa
        self.x = random.randrange(1,790,1) #creates a random position for x and y within the screen range for the object
        self.y = random.randrange(1,790,1)
        self.vx = random.randrange(-3,3,1) #creats random direction and speed for the object
        self.vy = random.randrange(-3,3,1)
    def draw(self):
        thing = pygame.font.SysFont('Cooper Black', 20).render(self.palabra, False, (105,105,105))
        self.cosa.blit(thing, (self.x, self.y))
    def mover(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 790:
            self.vx *= -1
            self.x = 790
        if self.x <= 0:
            self.vx *= -1
            self.x = 0
        if self.y >= 600:
            self.vy *= -1
            self.y = 600
        if self.y <= 0:
            self.vy *= -1
            self.y = 0
def mainScreen():






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
                        comienzo()
                    # If study button, study
                    if event.ui_element == show_words_button:
                        display_study_words(d,randomSample)
                    # If exit, exit
                    if event.ui_element == exit_button:
                        is_running = False
            
            #Process buttons
            mainScreenManager.process_events(event)


        #Denis changes
        #Scrolling background
        window_surface.blit(bg, (i, 0))
        window_surface.blit(bg, (width+i, 0))
        #If image is at end, wrap image around
        if i == -width:
            window_surface.blit(bg, (width+i, 0))
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
#  I created 2 lists of objects, one in spanish and one in english 
engObjs = [word(engList[i], window_surface) for i in range(12)]
spanObjs = [word(spanList[i], window_surface) for i in range(12)]
def comienzo():

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(40)
        window_surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False
            # Here i am attempting to see if I can match the x,y of the cursor on button press to one of the words and print the word i clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(12):
                    if ((engObjs[i].x or spanObjs[i].x) == pygame.mouse.get_pos()[0]) and  ((engObjs[i].y or spanObjs[i].y) == pygame.mouse.get_pos()[1]):
                        print(engObjs[i].palabra)
                print(engObjs[0].x,engObjs[0].y)#testing to see if we clicked on the word
                print(engObjs[0].palabra)#printing the word we want to test our click on
                print(pygame.mouse.get_pos())#getting the position of the mouse and printing it
            elif event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit(0)

        # this calls the mover functions and updated draw functions of the objects every loop 
        for i in range(12):
            engObjs[i].mover()
            engObjs[i].draw()
            spanObjs[i].mover()
            spanObjs[i].draw()
        
        # updates the postions of the objects that were changed because of their class functions
        pygame.display.update()


def display_study_words(engSpanDict,randomSample):

    # Header font is bigger
    headerFont = pygame.font.SysFont('Cooper Black', 60)



    #Separate manager for study words screen
    studyManager = pygame_gui.UIManager((width, 600))

    # Clock needed to update manager (don't know why.)
    clock = pygame.time.Clock()

    #Back to the main screen
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                            text='Back',
                                            #Study manager
                                            manager=studyManager)

    #Start the game from the study page
    start_from_study_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 545), (150, 50)),
                                            text='Start',
                                            #Study manager
                                            manager=studyManager)

    #Initialize english/spanish lists


    while True:
        time_delta = clock.tick(60)/1000.0

        #Make the screen white
        window_surface.fill((255,255,255))

        #Needed (but don't know why)
        for event in pygame.event.get():
            #'X' top right closes game
            if event.type == pygame.QUIT:
                #Exit the program
                exit(0)
 
            #Check if something we created is processed
            if event.type == pygame.USEREVENT:

                #If button is pressed
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    #Back button
                    if event.ui_element == back_button:
                        #Exit out of this function, returns to where it was called, which is in mainScreen.
                        return

                    #Start button
                    if event.ui_element == start_from_study_button:
                        #Start the game
                        comienzo()

            #Update studyManager
            studyManager.process_events(event)

        #Display English header
        window_surface.blit(headerFont.render('English', False, (0, 0, 0)),(95, -10))

        #Display separating pipes
        window_surface.blit(studyFont.render('|', False, (0, 0, 0)),(390, 0))
        #Overlap to look clean
        window_surface.blit(studyFont.render('|', False, (0, 0, 0)),(390, 20))

        #Display Spanish header
        window_surface.blit(headerFont.render('Spanish', False, (0, 0, 0)),(515, -10))

        #Display separating rows
        window_surface.blit(studyFont.render('________________________________', False, (0, 0, 0)),(75, 8))

        #First word starts at height 50
        wordHeight = 50
        for x in range(len(randomSample)):
            #English word
            window_surface.blit(englishWords[x],(95, wordHeight))

            #Separating rows
            window_surface.blit(studyFont.render('________________________________', False, (0, 0, 0)),(75, wordHeight))

            #Separating columns
            window_surface.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight))
            window_surface.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight+20))

            #Spanish word
            window_surface.blit(spanishWords[x],(515, wordHeight))

            #Update wordHeight
            wordHeight += 40

        #Update manager (for the buttons)
        studyManager.update(time_delta)
        #Display buttons
        studyManager.draw_ui(window_surface)

        #Update the display of the pygame
        pygame.display.update()





#Call main
mainScreen()