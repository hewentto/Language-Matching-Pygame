import pygame

class Button:
    def __init__(self, x, y, width, height):
        self.rectanlge = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('#a6a6a6')    # Light grey
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 20)
        self.callback = None
        try:
            self.text
        except AttributeError:
            self.text = ""

    # Create a default sized button
    @classmethod
    def standard(self, x, y):
        return self(x, y, 150, 75)

    # Create a default sized button
    @classmethod
    def fitText(self, x, y, text):
        width = len(text) + 65
        self.addText(self, text)
        return self(x, y, width, 45)

    def addText(self, text):
        self.text = text
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rectanlge)
        text_surface = self.myfont.render(self.text, True, pygame.Color('#000000'))
        textCoor = {
            'X' : self.rectanlge.x + (self.rectanlge.width - text_surface.get_rect().width)/2,
            'Y' : self.rectanlge.y + (self.rectanlge.height - text_surface.get_rect().height)/2
        }
        surface.blit(text_surface, (textCoor['X'], textCoor['Y']))
    
    def setCallback(self, callback):
        self.callback = callback

    def checkPressed(self, event):
        if self.rectanlge.collidepoint(event.pos):
            if self.color == pygame.Color('#a6a6a6'):
                self.color = pygame.Color(255, 0, 0)
            else:
                self.color = pygame.Color('#a6a6a6')    # Light grey

            if self.callback != None:
                self.callback()
        