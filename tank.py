import pygame
import sys
import math
from pomocne_funkce import *
rychlost=2
toceni = 0.04

tank = pygame.image.load("tanks.png")
tank = pygame.transform.scale(tank, (90,40))


class Tank:
    def __init__(self, pozice, smer, ):
        self.pozice = pozice
        self.smer = smer


    def nakresli(self, screen):
        blitRotate(screen, tank, (self.pozice[0],self.pozice[1] ), (25, 25), - self.smer / math.pi * 180)

    def posun(self):
        # kod kterej zmeni pozici o smer kazdy frame
        self.pozice[0] += rychlost * math.cos(self.smer)
        self.pozice[1] += rychlost * math.sin(self.smer)
