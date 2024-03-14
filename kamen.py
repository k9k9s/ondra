
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





# Vytvoření okna
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Kámen")

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Vykreslení modrého pozadí
    screen.fill(RED)

    # Vykreslení kámenem inspirovaného obrazce

    pygame.draw.rect(screen, DARK_GREEN, (500, 500, 25, 25))
    pygame.draw.rect(screen, DARK_GRAY, (490, 490, 45, 10))
    pygame.draw.rect(screen, DARK_GRAY, (490, 525, 45, 10))

    pygame.draw.rect(screen, WHITE, (492, 525, 2, 10))
    pygame.draw.rect(screen, WHITE, (502, 525, 2, 10))
    pygame.draw.rect(screen, WHITE, (512, 525, 2, 10))
    pygame.draw.rect(screen, WHITE, (522, 525, 2, 10))
    pygame.draw.rect(screen, WHITE, (532, 525, 2, 10))

    pygame.draw.rect(screen, WHITE, (492, 490, 2, 10))
    pygame.draw.rect(screen, WHITE, (502, 490, 2, 10))
    pygame.draw.rect(screen, WHITE, (512, 490, 2, 10))
    pygame.draw.rect(screen, WHITE, (522, 490, 2, 10))
    pygame.draw.rect(screen, WHITE, (532, 490, 2, 10))

    pygame.draw.rect(screen, BLACK, (511, 505, 5, 2))
    pygame.draw.rect(screen, BLACK, (511, 520, 5, 2))

    pygame.draw.rect(screen, BLACK, (505, 511, 2, 5))
    pygame.draw.rect(screen, BLACK, (520, 511, 2, 5))

    pygame.draw.rect(screen, BLACK, (506, 509, 2, 2))
    pygame.draw.rect(screen, BLACK, (507, 507, 2, 2))
    pygame.draw.rect(screen, BLACK, (509, 506, 2, 2))
    pygame.draw.rect(screen, BLACK, (516, 506, 2, 2))
    pygame.draw.rect(screen, BLACK, (518, 507, 2, 2))
    pygame.draw.rect(screen, BLACK, (519, 509, 2, 2))

    pygame.draw.rect(screen, BLACK, (506, 516, 2, 2))
    pygame.draw.rect(screen, BLACK, (507, 518, 2, 2))
    pygame.draw.rect(screen, BLACK, (509, 519, 2, 2))
    pygame.draw.rect(screen, BLACK, (516, 519, 2, 2))
    pygame.draw.rect(screen, BLACK, (518, 518, 2, 2))
    pygame.draw.rect(screen, BLACK, (519, 516, 2, 2))

    pygame.draw.rect(screen, BLACK, (520, 511, 15, 5))


    # Aktualizace obrazovky
    pygame.display.flip()

# Ukončení pygame
pygame.quit()
sys.exit()