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
