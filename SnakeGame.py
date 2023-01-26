import pygame

# Initialize pygame
pygame.init()

# Set window size and title
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Snake block size
block_size = 10

# Font for displaying score
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [size[0] / 2, size[1] / 2])


# Game loop
def gameLoop():
    game_over = False
    game_close = False

    # Starting position of snake
    x1 = 300
    y1 = 300

    # Snake movement speed
    x1_change = 0
    y1_change = 0

    # Clock
    clock = pygame.time.Clock()

    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Boundaries
        if x1 >= size[0] or x1 < 0 or y1 >= size[1] or y1 < 0:
            game_close = True

        # Moving the snake
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, white, [x1, y1, block_size, block_size])
        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    quit()


gameLoop()
