
import pygame
import sys

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


DARK_BROWN = (139, 69, 19)

def tank(x,y):
    pygame.draw.rect(screen, DARK_GREEN,(x+500, y+500, 25, 25))
    pygame.draw.rect(screen, DARK_GRAY, (x+490, y+490, 45, 10))
    pygame.draw.rect(screen, DARK_GRAY, (x+490, y+525, 45, 10))

    pygame.draw.rect(screen, WHITE, (x+492, y+525, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+502, y+525, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+512, y+525, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+522, y+525, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+532, y+525, 2, 10))

    pygame.draw.rect(screen, WHITE, (x+492, y+490, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+502, y+490, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+512, y+490, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+522, y+490, 2, 10))
    pygame.draw.rect(screen, WHITE, (x+532, y+490, 2, 10))

    pygame.draw.rect(screen, BLACK, (x+511, y+505, 5, 2))
    pygame.draw.rect(screen, BLACK, (x+511, y+520, 5, 2))

    pygame.draw.rect(screen, BLACK, (x+505, y+511, 2, 5))
    pygame.draw.rect(screen, BLACK, (x+520, y+511, 2, 5))

    pygame.draw.rect(screen, BLACK, (x+506, y+509, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+507, y+507, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+509, y+506, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+516, y+506, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+518, y+507, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+519, y+509, 2, 2))

    pygame.draw.rect(screen, BLACK, (x+506, y+516, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+507, y+518, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+509, y+519, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+516, y+519, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+518, y+518, 2, 2))
    pygame.draw.rect(screen, BLACK, (x+519, y+516, 2, 2))

    pygame.draw.rect(screen, BLACK, (x+520, y+511, 15, 5))


# Vytvoření okna
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("hra")



# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Vykreslení modrého pozadí
    screen.fill(DARK_BROWN)

    # Vykreslení kámenem inspirovaného obrazce
    tank(-400,200)


    # Aktualizace obrazovky
    pygame.display.flip()



# Ukončení pygame
pygame.quit()
sys.exit()