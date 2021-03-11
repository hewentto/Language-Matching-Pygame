import pygame
import pygame_gui
from pygameGame import comienzo

def display_study_words(engSpanDict,randomSample, screen, eng, span):

    # Header font is bigger
    headerFont = pygame.font.SysFont('Cooper Black', 60)

    # Every word that's not header
    studyFont = pygame.font.SysFont('Cooper Black', 40)

    #Separate manager for study words screen
    studyManager = pygame_gui.UIManager((800, 600))

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
        screen.fill((255,255,255))

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
                        comienzo(screen, randomSample, eng, span)

            #Update studyManager
            studyManager.process_events(event)

        #Display English header
        screen.blit(headerFont.render('English', False, (0, 0, 0)),(95, -10))

        #Display separating pipes
        screen.blit(studyFont.render('|', False, (0, 0, 0)),(390, 0))
        #Overlap to look clean
        screen.blit(studyFont.render('|', False, (0, 0, 0)),(390, 20))

        #Display Spanish header
        screen.blit(headerFont.render('Spanish', False, (0, 0, 0)),(515, -10))

        #Display separating rows
        screen.blit(studyFont.render('________________________________', False, (0, 0, 0)),(75, 8))

        #First word starts at height 50
        wordHeight = 50
        for x in range(len(randomSample)):
            #English word
            screen.blit(studyFont.render(eng[x], False, (0, 0, 0)),(95, wordHeight))

            #Separating rows
            screen.blit(studyFont.render('________________________________', False, (0, 0, 0)),(75, wordHeight))

            #Separating columns
            screen.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight))
            screen.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight+20))

            #Spanish word
            screen.blit(studyFont.render(span[x], False, (0, 0, 0)),(515, wordHeight))

            #Update wordHeight
            wordHeight += 40

        #Update manager (for the buttons)
        studyManager.update(time_delta)
        #Display buttons
        studyManager.draw_ui(screen)

        #Update the display of the pygame
        pygame.display.update()