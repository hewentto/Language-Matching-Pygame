# %%
import pygame
import pygame_gui
import random


d = {'english':['T-shirt','pants','skirt','socks','coat','shoes','boots','love','happy','tired','ready','box','wheel','can','wallet','screen','keyboard','bed','belt','glove','year','day','time','time(period of)','life','part','government','country','word','state','yes','no','maybe',"I don't know",'how','I','you','place','the','she'],
'spanish':['la camiseta','los pantalones','la falda','los calcetines','el abrigo','los zapatos','las botas','amor','feliz','consado','listo','cajón','rueda','lata','billetera','pantalla','teclado','cama','cinturón','guante','año','día','vez','tiempo','vida','parte','gobierno','país','mundo','estado','si','no','talvez','nose','cómo','yo','tu','lugar','el/la','ella']}


print(random.sample(list(range(len(d['english']))), 12))
print(d['english'][37])
print(d['spanish'][37])
# %%

pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
# myfont = pygame.font.SysFont('jokerman', 65) #jokerman, showcardgothic, magneto, franklingothicheavy, impact

myfont = pygame.font.SysFont('Cooper Black', 65)

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600),0,32)
textsurface = myfont.render('Spanglish Matching!', False, (0, 0, 0))

# background = pygame.Surface((800, 600))
# background.fill(pygame.Color('#33FFFF'))

# Denis Changes
window_surface = pygame.display.set_mode((800, 600),0,32)
#Denis Changes
bg_img = pygame.image.load('worldmap1024.jpg')
bg = pygame.transform.scale(bg_img, (800, 600))
width = 800
i = 0
####

manager = pygame_gui.UIManager((800, 600))
first_sound = pygame.mixer.Sound("crash.mp3")

backgroundMusic = pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(-1)


class word:
    def __init__(self, palabra, cosa, x, y):
        self.palabra = palabra
        self.cosa = cosa
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
    def draw(self):
        thing = pygame.font.SysFont('Cooper Black', 20).render(self.palabra, False, (105,105,105))
        self.cosa.blit(thing, (self.x, self.y))
    def mover(self):
        self.x += self.vx
        self.y += self.vy

def comienzo():
    global palabra
    palabra = word("happy", window_surface, 50, 100)
    palabra.vx = 3
    palabra.vy = 3
    global matching
    matching = word("feliz", window_surface, 0, 0)
    matching.vx = 4
    matching.vy = 5
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(40)
        window_surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                running = False
                sys.exit()
            manager.process_events(event)
        palabra.mover()
        if palabra.x >= 790:
            palabra.vx *= -1
            palabra.x = 790
        if palabra.x <= 0:
            palabra.vx *= -1
            palabra.x = 0
        if palabra.y >= 600:
            palabra.vy *= -1
            palabra.y = 600
        if palabra.y <= 0:
            palabra.vy *= -1
            palabra.y = 0
        palabra.draw()
        matching.mover()
        if matching.x >= 790:
            matching.vx *= -1
            matching.x = 790
        if matching.x <= 0:
            matching.vx *= -1
            matching.x = 0
        if matching.y >= 600:
            matching.vy *= -1
            matching.y = 600
        if matching.y <= 0:
            matching.vy *= -1
            matching.y = 0
        matching.draw()
        manager.update(time_delta)
        pygame.display.update()

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
                    comienzo()
                    print('Start the Game!')
                if event.ui_element == show_words_button:
                    print('I will show you the words!')
                if event.ui_element == exit_button:
                    print('Thanks for Playing!')

        manager.process_events(event)


    #Denis changes
    window_surface.fill((0,0,0))
    window_surface.blit(bg, (i, 0))
    window_surface.blit(bg, (width+i, 0))
    if i == -width:
        window_surface.blit(bg, (width+i, 0))
        i = 0
    i -= 1
    ####

    manager.update(time_delta)
    # window_surface.blit(background, (0, 0))
    window_surface.blit(textsurface,(95, 120))
    manager.draw_ui(window_surface)

    pygame.display.update()