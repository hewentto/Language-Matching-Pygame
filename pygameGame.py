import pygame
import pygame_gui
import random
import time
from pygame.mouse import get_pos
from pygameEndScreen import youMatch



def comienzo(screen, sampleSize, eng, span):

    #To keep track of what word we click
    word = ''

    #To know if we're on a first or second click
    count = 0

    #Keep track of the index where the word was clicked
    wordOneIndex = 0

    #Keeps the index of matches
    deleteMeHere=0

    #Colors
    match_color = (0,255,0)
    wrong_color = (255,0,0)
    default_color = (105,105,105)

    #Initialize start time to be a giant number so the current time will never be greater
    start_time_correct = start_time_wrong = 9615952996
   

    #How many seconds to display different color (wrong or right answers)
    seconds = .5

    class word:
        def __init__(self, word, screen):
            self.word = word
            self.screen = screen
            self.x = random.randrange(20,800 - 20,1) #creates a random position for x and y within the screen range for the object
            self.y = random.randrange(20,600 - 20,1)
            self.vx = random.randrange(-3,3,1) #creats random direction and speed for the object
            self.vy = random.randrange(-3,3,1)
            self.color = default_color

        def draw(self):
            renderText = pygame.font.SysFont('Cooper Black', 20).render(self.word, False, self.color)
            self.screen.blit(renderText, (self.x, self.y))
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

    engObjs  = [word(i, screen) for i in eng]
    spanObjs = [word(i, screen) for i in span]
    gameManager = pygame_gui.UIManager((800, 600))


    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                            text='Back',
                                            #Study manager
                                            manager=gameManager)


    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(40)
        #Fill the screen with black
        screen.fill((0,0,0))

        #Variable to determine coordinates on mouse click
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
                        # youMatch(screen)
                        return

            # Here i am attempting to see if I can match the x,y of the cursor on button press to one of the words and print the word i clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:

                #Make sure we iterate through engObjs so it gets updated each time an element is deleted
                for i in range(len(engObjs)):

                    # This creates a box around the word to give a window for the user to click
                    # If the x value of the word +length*15 > mouse's x position > x value od the word
                    # and
                    # if the y value of the word + 30 > mouse's y position > y value of the word
                    if engObjs[i].x+len(engObjs[i].word)*15 > mouse[0] > engObjs[i].x and engObjs[i].y+len(engObjs[i].word)+30  > mouse[1] > engObjs[i].y:

                        #Update count
                        count+=1

                        #If we're on the first click
                        if count % 2:

                            #Keep track of the word
                            word=engObjs[i].word

                            #Keep track of i
                            wordOneIndex=i

                        #If we're on the second click
                        else:

                            #If the spanish word (which was clicked first) has the same index as the english word just clicked
                            #and
                            #if the same english word wasn't clicked twice in a row
                            if wordOneIndex == i and word != engObjs[i].word:

                                #Create variable so we can delete without mattering what i equals
                                deleteMeHere=i

                                #Change the color
                                engObjs[i].color = match_color
                                spanObjs[i].color = match_color

                                #Start the timer
                                start_time_correct = time.time()

                            #If the second click was not a match of the first click
                            else:

                                #If the first word was english
                                if word in eng:
                                    engObjs[i].color = wrong_color
                                    engObjs[wordOneIndex].color = wrong_color
                                
                                #If the first word was spanish
                                else:
                                    engObjs[i].color = wrong_color
                                    spanObjs[wordOneIndex].color = wrong_color

                                #Start the timer of making the words red
                                start_time_wrong = time.time()

                            #Break to update the size of engObjs to iterate through
                            break

                    # This creates a box around the word to give a window for the user to click
                    # If the x value of the word +length*15 > mouse's x position > x value od the word
                    # and
                    # if the y value of the word + 30 > mouse's y position > y value of the word
                    if spanObjs[i].x+len(spanObjs[i].word)*15 > mouse[0] > spanObjs[i].x and spanObjs[i].y+len(spanObjs[i].word)+30  > mouse[1] > spanObjs[i].y:

                        #Update count
                        count+=1

                        #If we're on the first click
                        if count % 2:

                            #Keep track of the word
                            word=spanObjs[i].word

                            #Keep track of i
                            wordOneIndex=i

                        #If we're on the second click
                        else:

                            #If the english word (which was clicked first) has the same index as the spanish word just clicked
                            #and
                            #if the same spanish word wasn't clicked twice in a row
                            if wordOneIndex == i and word != spanObjs[i].word:

                                #Create variable so we can delete without mattering what i equals
                                deleteMeHere=i

                                #Change the color
                                engObjs[i].color = match_color
                                spanObjs[i].color = match_color

                                start_time_correct = time.time()

                            #If the second click was not a match of the first click
                            else:
                                #If the first word was spanish
                                if word in span:
                                    spanObjs[i].color = wrong_color
                                    spanObjs[wordOneIndex].color = wrong_color

                                #If the first word was english
                                else:
                                    spanObjs[i].color = wrong_color
                                    engObjs[wordOneIndex].color = wrong_color
                        
                                #Start the timer of making the words red
                                start_time_wrong = time.time()

                            #Break to update the size of engObjs to iterate through
                            break
                            
            #'X' in the top right being clicked
            elif event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit(0)

            #Manager needs to know what happened
            gameManager.process_events(event)


        #Get the current time to measure how long it's been since the start time
        current_time = time.time()

        #Check timer for the correct matches
        elapsed_time_correct = current_time - start_time_correct

        #If the words have been discolored for longer than {seconds}
        if elapsed_time_correct > seconds:

            #If time is up, reset the correct start time to a giant number again
            start_time_correct=9615952996
            del engObjs[deleteMeHere]
            del spanObjs[deleteMeHere]

        #Check timer for the incorrect matches
        elapsed_time_wrong = current_time - start_time_wrong

        #If the words have been discolored for longer than {seconds}
        if elapsed_time_wrong > seconds:

            #If time is up, reset the correct start time to a giant number again
            start_time_wrong=9615952996

            #Reset all the words back to default color
            for q in range(len(engObjs)):
                engObjs[q].color=default_color
                spanObjs[q].color=default_color


        #Initialize variables to keep track of index

        #DO NOT INITIALIZE AT 0
        #This would cause for the 0th word of the list to not show up.
        spanWord= -1

        #Assign them to a number that won't be in the index
        engWord= -1

        #Make sure variables are different for each for loop inside While True loop
        for k in range(len(engObjs)):

            #If we're on the first click and the word is spanish
            if count%2 and word in span:

                #Find the word in the spanObjs list
                if spanObjs[k].word == word:

                    #Use this to track which index the word is in
                    #Since we initialize at -1, add an extra 1
                    spanWord += k+1

                    #Draw the word with a different color
                    spanObjs[k].color = (0,255,255)
                    spanObjs[k].draw()

            #If we're on the first click and the word is english
            if count%2 and word in eng:

                #Find the word in the engObjs list
                if engObjs[k].word == word:

                    #Use this to track which index the word is in
                    #Since we initialize at -1, add an extra 1
                    engWord += k+1

                    #Draw the word with a different color
                    engObjs[k].color = (0,255,255)
                    engObjs[k].draw()

            #Draw all the other spanish words in the standard color
            if k != spanWord:
                spanObjs[k].draw()

            #Draw all the other english words in the standard color
            if k != engWord:
                engObjs[k].draw()
            
            #Despite which word is getting highlighted, the words will always move
            engObjs[k].mover()
            spanObjs[k].mover()

        #If engObjs is empty, go to end screen
        if not engObjs:
            youMatch(screen)

        #Update manager (for the buttons)
        gameManager.update(time_delta)
        #Display buttons
        gameManager.draw_ui(screen)
        # updates the postions of the objects that were changed because of their class functions
        pygame.display.update()