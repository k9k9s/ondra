import pygame
import sys
import math
from pomocne_funkce import *
from strela import *
rychlost=2
toceni = 0.02

tank = pygame.image.load("tanking.png").convert()
tank.set_colorkey((255, 128, 255))

charge_time = 1.5
charge_frames = charge_time*FPS
chargebar_max = 60
charge_increment = chargebar_max/charge_frames


class Tank:
    def __init__(self, pozice, smer, kdojsem):
        self.pozice = pozice
        self.smer = smer
        self.rychlost = 0
        self.toceni = [0,0]
        self.kulomet_str = False
        self.charged = 20
        self.kdojsem = kdojsem
        self.žiju = True

    def zmiz(self):
        self.žiju = False


    def nakresli(self, screen):
        if not self.žiju:
            return
        blitRotate(screen, tank, (self.pozice[0], self.pozice[1]), (25, 25), - self.smer / math.pi * 180)
        pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(self.pozice[0] - 9, self.pozice[1] - 23, chargebar_max + 6, 11))
        if self.charged < chargebar_max:
            self.charged += charge_increment
        chargebar = pygame.Rect(self.pozice[0] - 6, self.pozice[1] - 20, self.charged, 5)
        if self.charged >= chargebar_max:
            pygame.draw.rect(screen, DARK_RED, chargebar)
        else:
            pygame.draw.rect(screen, YELLOW, chargebar)



    def posun(self):
        # kod kterej zmeni pozici o smer kazdy frame
        self.pozice[0] +=  self.rychlost * math.cos(self.smer)
        self.pozice[1] += self.rychlost * math.sin(self.smer)
        self.smer += self.toceni[1] - self.toceni[0]

    def vystrel(self):
        s_pozice = [self.pozice[0] , self.pozice[1] ]
        nova_strela = Strela( s_pozice, self.smer,self.kdojsem,KANON)
        self.charged = 0
        return nova_strela

    def hitbox(self):
        hitbox = rotate( tank, (self.pozice[0], self.pozice[1]), (25, 25), - self.smer / math.pi * 180)[1]
        return hitbox

    # lijgfrshgf

