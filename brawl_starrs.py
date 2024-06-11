import pygame


pygame.init()

WIDTH, HEIGHT = 1500,800
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)


import sys
import math
from strela import *
from pomocne_funkce import *
from tank import *










def palma(screen):

    palma = pygame.image.load("python-palma.png")
    screen.blit(palma, (300, 200))

vysrelene_srely = []



clock = pygame.time.Clock()
fps = 60
fps_was = 0
pygame.display.set_caption("hra")

dopredu = pygame.K_w
dozadu = pygame.K_s
doprava = pygame.K_d
doleva = pygame.K_a
vystrel = pygame.K_SPACE
kulomet = pygame.K_LSHIFT


dopredu2 = pygame.K_KP_8
dozadu2 = pygame.K_KP_5
doprava2 = pygame.K_KP_6
doleva2 = pygame.K_KP_4
vystrel2 = pygame.K_KP_0
kulomet2 = pygame.K_KP_ENTER


hrac1 = Tank([100,100], 0,kdojsem = 1)
hrac2 = Tank([1400,700], 0, kdojsem = 2)



k_rychlost = [20,0]



running = True
while running:

    screen.fill(DARK_BROWN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
            if event.key == dopredu:
                hrac1.rychlost = 2
            if event.key == dozadu:
                hrac1.rychlost = -2
            if event.key == doleva:
                hrac1.toceni[0] = 0.04
            if event.key == doprava:
                hrac1.toceni[1] = 0.04

            if event.key == dopredu2:
                hrac2.rychlost = 2
            if event.key == dozadu2:
                hrac2.rychlost = -2
            if event.key == doleva2:
                hrac2.toceni[0] = 0.04
            if event.key == doprava2:
                hrac2.toceni[1] = 0.04

            if event.key == kulomet:
                hrac1.kulomet_str = True
            if event.key == kulomet2:
                hrac2.kulomet_str = True

            if event.key == vystrel and hrac1.charged >= chargebar_max:
                vysrelene_srely.append(hrac1.vystrel())




        if event.type == pygame.KEYUP:
            if event.key == dozadu:
                hrac1.rychlost = 0
            if event.key == dopredu:
                hrac1.rychlost = 0
            if event.key == doleva:
                hrac1.toceni[0] = 0
            if event.key == doprava:
                hrac1.toceni[1] = 0

            if event.key == dozadu2:
                hrac2.rychlost = 0
            if event.key == dopredu2:
                hrac2.rychlost = 0
            if event.key == doleva2:
                hrac2.toceni[0] = 0
            if event.key == doprava2:
                hrac2.toceni[1] = 0

            if event.key == kulomet:
                hrac1.kulomet_str = False
            if event.key == kulomet2:
                hrac2.kulomet_str = False

            if event.key == vystrel2 and hrac2.charged >= chargebar_max:
                vysrelene_srely.append(hrac2.vystrel())




    hrac1.posun()
    hrac2.posun()




    for s in  vysrelene_srely:
        s.posun()
        s.nakresli(screen)
        if s.pozice[0] > 3000:
            vysrelene_srely.remove(s)
            continue

        if s.hitbox().colliderect(hrac1.hitbox()):
            if s.kohotoje == hrac2.kdojsem:
                if s.cotoje == KANON:
                    hrac1.zmiz()


        if s.hitbox().colliderect(hrac2.hitbox()):
            if s.kohotoje == hrac1.kdojsem:
                if s.cotoje == KANON:
                    hrac2.zmiz()



    if hrac1.pozice[0] < 0:
        hrac1.pozice[0] = 0
    if hrac1.pozice[1] < 0:
        hrac1.pozice[1] = 0
    if hrac1.pozice[0] > WIDTH - 60:
        hrac1.pozice[0] = WIDTH - 60
    if hrac1.pozice[1] > HEIGHT - 30:
        hrac1.pozice[1] = HEIGHT - 30


    if hrac2.pozice[0] < 0:
        hrac2.pozice[0] = 0
    if hrac2.pozice[1] < 0:
        hrac2.pozice[1] = 0
    if hrac2.pozice[0] > WIDTH - 60:
        hrac2.pozice[0] = WIDTH - 60
    if hrac2.pozice[1] > HEIGHT - 30:
        hrac2.pozice[1] = HEIGHT - 30




    if hrac1.kulomet_str:
        if hrac1.charged >= chargebar_max/60:
            hrac1.charged -= chargebar_max/60

            if fps_was%3 == 0:
                  k_pozice = [hrac1.pozice[0] + 30, hrac1.pozice[1] + 15]
                  nova_strela = Strela(k_pozice, hrac1.smer,hrac1.kdojsem,KULOMET)
                  vysrelene_srely.append(nova_strela)
        else:
            hrac1.charged = 0




    if hrac2.kulomet_str:
        if hrac2.charged >= chargebar_max/60:
            hrac2.charged -= chargebar_max/60

            if fps_was%3 == 0:
                  k_pozice = [hrac2.pozice[0] + 30, hrac2.pozice[1] + 15]
                  nova_strela = Strela(k_pozice, hrac2.smer,hrac2.kdojsem,KULOMET)
                  vysrelene_srely.append(nova_strela)
        else:
            hrac2.charged = 0




    hrac1.nakresli(screen)
    hrac2.nakresli(screen)
    #palma(screen)





    pygame.display.flip()

    clock.tick(fps)



pygame.quit()
sys.exit()
