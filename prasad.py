import pygame
import random
import time
import sys

# Initialize pygame
pygame.init()

# Game window
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game by Lokesh")

# Colors
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Draw text
def draw_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [x, y])

# Main game function
def game_loop():
    snake_pos = [100, 50]
    snake_body = [[100, 50]]
    snake_length = 1
    food_pos = [random.randrange(20, width - 20, 10), random.randrange(20, height - 20, 10)]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    start_time = time.time()

    level = 1

    running = True
    while running:
        game_screen.fill(black)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to

        # Move snake
        if direction == 'UP':
            snake_pos[1] -= 10
        elif direction == 'DOWN':
            snake_pos[1] += 10
        elif direction == 'LEFT':
            snake_pos[0] -= 10
        elif direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 10
            food_pos = [random.randrange(20, width - 20, 10), random.randrange(20, height - 20, 10)]
        else:
            snake_body.pop()

        # Draw snake and food
        for block in snake_body:
            pygame.draw.rect(game_screen, green, pygame.Rect(block[0], block[1], 10, 10))
        pygame.draw.rect(game_screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Score, level and time
        elapsed_time = int(time.time() - start_time)
        level = min(100, score // 50 + 1)
        draw_text(f"Score: {score}", white, 10, 10)
        draw_text(f"Level: {level}", white, 10, 40)
        draw_text(f"Time: {elapsed_time}s", white, 10, 70)

        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
            draw_text("Game Over! Hit the wall.", red, 180, 300)
            pygame.display.update()
            pygame.time.wait(2000)
            break

        if snake_pos in snake_body[1:]:
            draw_text("Game Over! Hit yourself.", red, 180, 300)
            pygame.display.update()
            pygame.time.wait(2000)
            break

        pygame.display.update()
        clock.tick(10 + level)  # Increase speed with level

# Run the game
game_loop()
pygame.quit()
