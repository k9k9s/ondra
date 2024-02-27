import pygame
import math

# Inicializace knihovny Pygame
pygame.init()

# Nastavení rozměrů okna
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Stars")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Nastavení tanků
PLAYER_TANK = pygame.image.load("player_tank.png")
ENEMY_TANK = pygame.image.load("enemy_tank.png")
TANK_WIDTH, TANK_HEIGHT = 50, 50
PLAYER_START_X, PLAYER_START_Y = 100, HEIGHT - 100
ENEMY_START_X, ENEMY_START_Y = WIDTH - 150, HEIGHT - 100

# Funkce pro vykreslení tanku
def draw_tank(tank, x, y):
    WINDOW.blit(tank, (x, y))

# Funkce pro vykreslení střely
def draw_bullet(x, y):
    pygame.draw.circle(WINDOW, RED, (x, y), 5)

# Hlavní herní smyčka
def main():
    player_x, player_y = PLAYER_START_X, PLAYER_START_Y
    enemy_x, enemy_y = ENEMY_START_X, ENEMY_START_Y
    bullet_x, bullet_y = None, None
    bullet_speed = 10
    is_shooting = False

    # Hlavní herní smyčka
    running = True
    while running:
        # Události
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_shooting:
                    bullet_x, bullet_y = player_x + TANK_WIDTH // 2, player_y
                    is_shooting = True

        # Pohyb tanku
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= 5
        if keys[pygame.K_RIGHT]:
            player_x += 5

        # Pohyb střely
        if is_shooting:
            bullet_y -= bullet_speed
            if bullet_y < 0:
                is_shooting = False

        # Detekce kolize střely s tankem
        if bullet_x and bullet_y:
            if (enemy_x < bullet_x < enemy_x + TANK_WIDTH) and (enemy_y < bullet_y < enemy_y + TANK_HEIGHT):
                is_shooting = False
                bullet_x, bullet_y = None, None

        # Vykreslení
        WINDOW.fill(WHITE)
        draw_tank(PLAYER_TANK, player_x, player_y)
        draw_tank(ENEMY_TANK, enemy_x, enemy_y)
        if is_shooting:
            draw_bullet(bullet_x, bullet_y)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
