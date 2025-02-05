import pygame
import sys
import math
from pomocne_funkce import *




KULOMET = 0
KANON = 1

strela = pygame.image.load("z0pq38qb.png")
strela = pygame.transform.scale(strela, (36,9))


class Strela:
    def __init__(self, pozice, smer, kohotoje, cotoje=KANON , rychlost = 20,):
        self.pozice = pozice
        self.smer = smer
        self.rychlost = rychlost
        self.cotoje = cotoje
        self.kohotoje= kohotoje


    def nakresli(self, screen):
        if self.cotoje == KANON:
            blitRotate(screen, strela, self.pozice , [18,4],- self.smer / math.pi * 180)
        elif self.cotoje == KULOMET:
            surf = pygame.Surface((5,3))
            pygame.draw.rect(surf, GRAY, pygame.Rect(0,0, 5, 3))
            blitRotate(screen, surf, self.pozice, [18, 4], - self.smer / math.pi * 180)


    def posun(self):
        # kod kterej zmeni pozici o smer kazdy frame
        self.pozice[0] += self.rychlost * math.cos(self.smer)
        self.pozice[1] += self.rychlost * math.sin(self.smer)

    def hitbox(self):

        return pygame.Rect(self.pozice[0], self.pozice[1], 7, 7)

    #jmhgfuye