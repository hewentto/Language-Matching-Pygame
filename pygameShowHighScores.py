import pygame
import pygame_gui
import highScores

def display_high_scores(screen):

    # Header font is bigger
    headerFont = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 60)

    # Every word that's not header
    studyFont = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 40)

    #Separate manager for study words screen
    scoresManager = pygame_gui.UIManager((800, 600))

    # Clock needed to update manager (don't know why.)
    clock = pygame.time.Clock()

    #Back to the main screen
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                            text='Back',
                                            #Study manager
                                            manager=scoresManager)


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


            #Update scoresManager
            scoresManager.process_events(event)

        #Display Names header
        screen.blit(headerFont.render('Names', False, (0, 0, 0)),(95, -10))

        #Display separating pipes
        screen.blit(studyFont.render('|', False, (0, 0, 0)),(390, 0))
        #Overlap to look clean
        screen.blit(studyFont.render('|', False, (0, 0, 0)),(390, 20))

        #Display Scores header
        screen.blit(headerFont.render('Scores', False, (0, 0, 0)),(515, -10))

        #Display separating rows
        screen.blit(studyFont.render('____________________________________', False, (0, 0, 0)),(75, 8))

        #First word starts at height 50
        wordHeight = 50

        listOfNames = highScores.getListOfNames()
        listOfScores = highScores.getListOfScores()
        
        for i in range(len(listOfScores)):
            #Names
            screen.blit(studyFont.render(listOfNames[i], False, (0, 0, 0)),(95, wordHeight))

            #Separating rows
            screen.blit(studyFont.render('____________________________________', False, (0, 0, 0)),(75, wordHeight))

            #Separating columns
            screen.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight))
            screen.blit(studyFont.render('|',False,(0,0,0)),(390, wordHeight+20))

            #High scores
            screen.blit(studyFont.render(str(listOfScores[i])[:5], False, (0, 0, 0)),(515, wordHeight))

            #Update wordHeight
            wordHeight += 50

        #Update manager (for the buttons)
        scoresManager.update(time_delta)
        #Display buttons
        scoresManager.draw_ui(screen)

        #Update the display of the pygame
        pygame.display.update()