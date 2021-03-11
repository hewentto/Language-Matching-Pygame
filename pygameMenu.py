
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
height = 600

pygame.display.set_caption('Quick Start')
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

# Every word that's not header
studyFont = pygame.font.SysFont('Cooper Black', 40)

#Generate english/spanish lists, with corresponding indeces
for x in randomSample:
    engList.append( d['english'][x])
    spanList.append(d['spanish'][x])

class word:
    def __init__(self, word, screen):
        self.word = word
        self.screen = screen
        self.x = random.randrange(20,width - 20,1) #creates a random position for x and y within the screen range for the object
        self.y = random.randrange(20,height - 20,1)
        self.vx = random.randrange(-3,3,1) #creats random direction and speed for the object
        self.vy = random.randrange(-3,3,1)
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self):
        thing = pygame.font.SysFont('Cooper Black', 20).render(self.word, False, (105,105,105))
        self.screen.blit(thing, (self.x, self.y))
    def mover(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 790:
            self.vx *= -1
            self.x = 790
        if self.x <= 0:
            self.vx *= -1
            self.x = 0
        if self.y >= height:
            self.vy *= -1
            self.y = height
        if self.y <= 0:
            self.vy *= -1
            self.y = 0


#  I created 2 lists of objects, one in spanish and one in english 
engObjs  = [word(i, window_surface) for i in engList]
spanObjs = [word(i, window_surface) for i in spanList]

def comienzo():

    gameManager = pygame_gui.UIManager((width, height))


    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                            text='Back',
                                            #Study manager
                                            manager=gameManager)

    word = ''
    count = 1
    clickOneWord = 0
    clickOne = False
    dontShow=[]

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(40)
        window_surface.fill((0,0,0))

        mouse = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False

            if event.type == pygame.USEREVENT:

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    #Back button
                    if event.ui_element == back_button:
                        #Exit out of this function, returns to where it was called, which is in mainScreen.
                        # youMatch()
                        return

            # Here i am attempting to see if I can match the x,y of the cursor on button press to one of the words and print the word i clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(randomSample)):

                    if engObjs[i].x+len(engObjs[i].word)*15 > mouse[0] > engObjs[i].x and engObjs[i].y+len(engObjs[i].word)+30  > mouse[1] > engObjs[i].y:
                        if count % 2:
                            word=engObjs[i].word
                            clickOne=True
                            clickOneWord=i
                        else:
                            if clickOneWord == i and word != engObjs[i].word:
                                dontShow.append(i)
                                # del engObjs[i]
                                # del spanObjs[i]
                            clickOne=False

                        print(engObjs[i].word)
                        count+=1
                    if spanObjs[i].x+len(spanObjs[i].word)*15 > mouse[0] > spanObjs[i].x and spanObjs[i].y+len(spanObjs[i].word)+30 > mouse[1] > spanObjs[i].y:
                        if count % 2:
                            word=spanObjs[i].word
                            clickOne=True
                            clickOneWord=i
                        else:
                            if clickOneWord == i and word != spanObjs[i].word:
                                dontShow.append(i)
                                # del engObjs[i]
                                # del spanObjs[i]
                            clickOne=False
                            
                        print(spanObjs[i].word)
                        count+=1
                    
            elif event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit(0)

            gameManager.process_events(event)

        if clickOne and word in spanList:
            pygame.draw.rect(window_surface, (0,255,0),(spanObjs[clickOneWord].x,spanObjs[clickOneWord].y,len(spanObjs[clickOneWord].word)*15,len(spanObjs[clickOneWord].word)+30))
        if clickOne and word in engList:
            pygame.draw.rect(window_surface, (0,255,0),(engObjs[clickOneWord].x,engObjs[clickOneWord].y,len(engObjs[clickOneWord].word)*15,len(engObjs[clickOneWord].word)+30))

        for i in range(len(randomSample)):
            if i not in dontShow:
                engObjs[i].draw()
                engObjs[i].mover()
                spanObjs[i].draw()
                spanObjs[i].mover()

    
        if len(dontShow) == len(randomSample):
            youMatch()

        #Update manager (for the buttons)
        gameManager.update(time_delta)
        #Display buttons
        gameManager.draw_ui(window_surface)
        # updates the postions of the objects that were changed because of their class functions
        pygame.display.update()




def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center = (400, 300))
    return rotated_surface, rotated_rect

# Phrase of Matching
def youMatch():
    clock = pygame.time.Clock()
    running = True
    size = 100
    angle = 0
    phrase = pygame.font.SysFont('Cooper Black', size).render("Good Job!", False, (105,105,105))
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
        phrase_rect = phrase.get_rect(center = (400, 300))

        angle += 1

        window_surface.fill((0,0,0))
        phrase_rotated, phrase_rotated_rect = rotate(phrase, angle)

        window_surface.blit(phrase_rotated, phrase_rotated_rect)
        pygame.display.update() 



def display_study_words(engSpanDict,randomSample):

    # Header font is bigger
    headerFont = pygame.font.SysFont('Cooper Black', 60)


    #Separate manager for study words screen
    studyManager = pygame_gui.UIManager((width, height))

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
            window_surface.blit(studyFont.render(engList[x], False, (0, 0, 0)),(95, wordHeight))

            #Separating rows
            window_surface.blit(studyFont.render('________________________________', False, (0, 0, 0)),(75, wordHeight))

            #Separating columns
            window_surface.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight))
            window_surface.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight+20))

            #Spanish word
            window_surface.blit(studyFont.render(spanList[x], False, (0, 0, 0)),(515, wordHeight))

            #Update wordHeight
            wordHeight += 40

        #Update manager (for the buttons)
        studyManager.update(time_delta)
        #Display buttons
        studyManager.draw_ui(window_surface)

        #Update the display of the pygame
        pygame.display.update()


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


#Call main
mainScreen()