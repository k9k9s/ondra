import pygame
import sys
import math
from pomocne_funkce import blitRotate



strela = pygame.image.load("z0pq38qb.png")
strela = pygame.transform.scale(strela, (36,9))


class Strela:
    def __init__(self, pozice, smer, rychlost = 20):
        self.pozice = pozice
        self.smer = smer
        self.rychlost = rychlost

    def nakresli(self, screen):
        blitRotate(screen, strela, self.pozice , [18,4],- self.smer / math.pi * 180)

    def posun(self):
        # kod kterej zmeni pozici o smer kazdy frame
        self.pozice[0] += self.rychlost * math.cos(self.smer)
        self.pozice[1] += self.rychlost * math.sin(self.smer)


