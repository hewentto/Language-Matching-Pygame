import pygame
import pygame_gui
import random
from pygame.mouse import get_pos
from pygameEndScreen import youMatch


def comienzo(screen, sampleSize, eng, span):

    class word:
        def __init__(self, word, screen):
            self.word = word
            self.screen = screen
            self.x = random.randrange(20,800 - 20,1) #creates a random position for x and y within the screen range for the object
            self.y = random.randrange(20,600 - 20,1)
            self.vx = random.randrange(-3,3,1) #creats random direction and speed for the object
            self.vy = random.randrange(-3,3,1)

        def draw(self, fontColor = (105,105,105)):
            renderText = pygame.font.SysFont('Cooper Black', 20).render(self.word, False, fontColor)
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

    #To keep track of what word we click
    word = ''

    #To know if we're on a first or second click
    count = 1

    #Keep track of the index where the word was clicked
    clickOneWord = 0


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
                            clickOneWord=i

                        #If we're on the second click
                        else:

                            #If the spanish word (which was clicked first) has the same index as the english word just clicked
                            #and
                            #if the same english word wasn't clicked twice in a row
                            if clickOneWord == i and word != engObjs[i].word:

                                #Delete the objects from the list
                                del engObjs[i]
                                del spanObjs[i]


                            #Break to update the size of engObjs to iterate through
                            break
                        
                        #Debugging
                        print(engObjs[i].word)



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
                            clickOneWord=i

                        #If we're on the second click
                        else:

                            #If the spanish word (which was clicked first) has the same index as the spanish word just clicked
                            #and
                            #if the same spanish word wasn't clicked twice in a row
                            if clickOneWord == i and word != spanObjs[i].word:

                                #Delete the objects from the list
                                del engObjs[i]
                                del spanObjs[i]


                            #Break to update the size of engObjs to iterate through
                            break
                            
                        #Debugging
                        print(spanObjs[i].word)

            elif event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit(0)

            gameManager.process_events(event)


        #Initialize variables to keep track of index
        spanWord=0
        engWord=0

        for i in range(len(engObjs)):

            #If we're on the first click and the word is spanish
            if count%2 and word in span:

                #Find the word in the spanObjs list
                if spanObjs[i].word == word:

                    #Use this to track which index the word is in
                    spanWord += i

                    #Draw the word with a different color (yellow)
                    spanObjs[i].draw((255,255,0))

            #If we're on the first click and the word is english
            if count%2 and word in eng:

                #Find the word in the engObjs list
                if engObjs[i].word == word:

                    #Use this to track which index the word is in
                    engWord += i

                    #Draw the word with a different color (yellow)
                    engObjs[i].draw((255,255,0))

            #Draw all the other spanish words in the standard color
            if i != spanWord:
                spanObjs[i].draw()

            #Draw all the other english words in the standard color
            if i != engWord:
                engObjs[i].draw()
            
            #Despite which word is getting highlighted, the words will always move
            engObjs[i].mover()
            spanObjs[i].mover()

        #If engObjs is empty, go to end screen
        if not engObjs:
            youMatch(screen)

        #Update manager (for the buttons)
        gameManager.update(time_delta)
        #Display buttons
        gameManager.draw_ui(screen)
        # updates the postions of the objects that were changed because of their class functions
        pygame.display.update()