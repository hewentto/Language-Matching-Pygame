import pygame
import pygame_gui
from pygame.mouse import get_pos
import random
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

    word = ''
    count = 1
    clickOneWord = 0
    clickOne = False
    dontShow=[]

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(40)
        screen.fill((0,0,0))

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
                for i in range(len(sampleSize)):

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

        if clickOne and word in span:
            pygame.draw.rect(screen, (0,255,0),(spanObjs[clickOneWord].x,spanObjs[clickOneWord].y,len(spanObjs[clickOneWord].word)*15,len(spanObjs[clickOneWord].word)+30))
        if clickOne and word in eng:
            pygame.draw.rect(screen, (0,255,0),(engObjs[clickOneWord].x,engObjs[clickOneWord].y,len(engObjs[clickOneWord].word)*15,len(engObjs[clickOneWord].word)+30))

        for i in range(len(sampleSize)):
            if i not in dontShow:
                engObjs[i].draw()
                engObjs[i].mover()
                spanObjs[i].draw()
                spanObjs[i].mover()

    
        if len(dontShow) == len(sampleSize):
            youMatch(screen)

        #Update manager (for the buttons)
        gameManager.update(time_delta)
        #Display buttons
        gameManager.draw_ui(screen)
        # updates the postions of the objects that were changed because of their class functions
        pygame.display.update()