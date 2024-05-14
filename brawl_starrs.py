import pygame
import sys
import math
from strela import Strela
from pomocne_funkce import blitRotate

## ahoj, tohle ti sem napsal tata

# Inicializace pygame
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 1500,800
WINDOW_SIZE = (WIDTH, HEIGHT)

# Barvy
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
WHITE = (255, 255, 255)
DARK_WHITE = (128, 128, 128)


# Tmavé odstíny
DARK_BLUE = (0, 0, 128)
DARK_GREEN = (0, 128, 0)
DARK_YELLOW = (128, 128, 0)
DARK_RED = (128, 0, 0)
DARK_BLACK = (0, 0, 0)
DARK_WHITE = (128, 128, 128)
DARK_PURPLE = (128, 0, 128)
DARK_PINK = (255, 20, 147)
DARK_BROWN = (139, 69, 19)

# Základní odstíny
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)

# Světlé odstíny
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_RED = (255, 192, 203)
LIGHT_BLACK = (128, 128, 128)
LIGHT_WHITE = (255, 255, 255)
LIGHT_PURPLE = (221, 160, 221)
LIGHT_PINK = (255, 182, 193)
LIGHT_BROWN = (210, 105, 30)








vysrelene_srely = []


def palma(screen):
    # Načtení obrázku tanku
    palma = pygame.image.load("python-palma.png")
    screen.blit(palma, (300, 200))






def nakresli_tank(screen, kamtocivim ):
    # Načtení obrázku tanku

    blitRotate(screen,tank,(x,y),(25,25),- kamtocivim / math.pi * 180)



def kulka(screen,k):
    pygame.draw.rect(screen,GRAY,pygame.Rect(k[0],k[1],10,5))

vysrelene_srely = []
vystrelene_kulky = []









clock = pygame.time.Clock()
fps = 60
fps_was = 0
# Vytvoření okna
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("hra")


tank = pygame.image.load("leopard2a9.png").convert()
tank.set_colorkey((255, 128, 255))

dopredu = pygame.K_w
dozadu = pygame.K_s

doprava = pygame.K_d
doleva = pygame.K_a

vystrel = pygame.K_SPACE

y = 100
x = 100

kamtocumim = 0

rychlost = 0

kamtomířim = kamtocumim

s_angle = kamtomířim


kulomet = pygame.K_LSHIFT
kulomet_str = False

k_rychlost = [20,0]



toceni = [0,0]



charged = 0
charge_time = 1.5
charge_frames = charge_time*fps
chargebar_max = 60
charge_increment = chargebar_max/charge_frames


# Hlavní smyčka
running = True
while running:

    screen.fill(DARK_BROWN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
            if event.key == dopredu:
                rychlost = 2
            if event.key == dozadu:
                rychlost = -2
            if event.key == doleva:
                toceni[0] = 0.04
            if event.key == doprava:
                toceni[1] = 0.04
            if event.key == kulomet:
                kulomet_str = True



            if event.key == vystrel and charged >= chargebar_max:
                s_pozice = [x + 40, y + 18]
                nova_strela = Strela( s_pozice, kamtocumim)
                vysrelene_srely.append(nova_strela)
                charged = 0

        if event.type == pygame.KEYUP:
            if event.key == dozadu:
                rychlost = 0
            if event.key == dopredu:
                rychlost = 0
            if event.key == doleva:
                toceni[0] = 0
            if event.key == doprava:
                toceni[1] = 0
            if event.key == kulomet:
                kulomet_str = False



    # Vykreslení modrého pozadí

    x += rychlost*math.cos(kamtocumim)
    kamtocumim += toceni[1] - toceni[0]
    y += rychlost * math.sin(kamtocumim)
    for s in  vysrelene_srely:
        s.posun()
        s.nakresli(screen)
        if s.pozice[0] > 3000:
            vysrelene_srely.remove(s)
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > WIDTH - 60:
        x = WIDTH - 60
    if y > HEIGHT - 30:
        y = HEIGHT - 30

    if kulomet_str:
        if charged >= chargebar_max/60:

            charged -= chargebar_max/60

            if fps_was%3 == 0:
                  k_pozice = [x + 30, y + 15]
                  vystrelene_kulky.append(k_pozice)
        else:
            charged = 0
    for k in  vystrelene_kulky:
        k[0] += k_rychlost[0]
        kulka(screen,k)
        if k[0] > 3000:
            vystrelene_kulky.remove(k)



    print(charged)
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(x-9,y-23,chargebar_max+6,11))
    if charged < chargebar_max:
        charged += charge_increment
    chargebar = pygame.Rect(x-6,y-20,charged,5)
    if charged >= chargebar_max:
        pygame.draw.rect(screen,DARK_RED,chargebar)
    else:
        pygame.draw.rect(screen,YELLOW,chargebar)


    # Vykreslení kámenem inspirovaného obrazce
    nakresli_tank(screen, kamtocivim=kamtocumim)
    print(kamtocumim)


    palma(screen)









    # Aktualizace obrazovky
    pygame.display.flip()

    clock.tick(fps)

# Ukončení pygame
pygame.quit()
sys.exit()
