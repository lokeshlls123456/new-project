import pygame
import sys
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Parking Game - Lokesh")
clock = pygame.time.Clock()

# Colors
WHITE, GREEN, RED, BLACK, YELLOW = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0), (255, 255, 0)

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Game variables
level = 1
score = 0
max_level = 100
car_speed = 4
parking_zone_height = 80
car_width, car_height = 50, 90
mirror_width = 10
mirror_height = 20

# Car
car = pygame.Rect(WIDTH//2 - car_width//2, HEIGHT - 100, car_width, car_height)

# Mirrors
def draw_mirrors(car):
    left_mirror = pygame.Rect(car.left - mirror_width, car.centery - mirror_height//2, mirror_width, mirror_height)
    right_mirror = pygame.Rect(car.right, car.centery - mirror_height//2, mirror_width, mirror_height)
    rear_mirror = pygame.Rect(car.centerx - 20, car.top - 20, 40, 10)
    pygame.draw.rect(screen, YELLOW, left_mirror)
    pygame.draw.rect(screen, YELLOW, right_mirror)
    pygame.draw.rect(screen, YELLOW, rear_mirror)

# Parking Zone
def create_parking_zone(level):
    margin = 50
    x = random.randint(margin, WIDTH - car_width - margin)
    y = random.randint(margin, HEIGHT // 3)
    return pygame.Rect(x, y, car_width + 10, parking_zone_height)

parking_zone = create_parking_zone(level)

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Car controls
    if keys[pygame.K_LEFT] and car.left > 0:
        car.x -= car_speed
    if keys[pygame.K_RIGHT] and car.right < WIDTH:
        car.x += car_speed
    if keys[pygame.K_UP] and car.top > 0:
        car.y -= car_speed
    if keys[pygame.K_DOWN] and car.bottom < HEIGHT:
        car.y += car_speed

    # Draw parking zone
    pygame.draw.rect(screen, GREEN, parking_zone, 3)

    # Draw car
    pygame.draw.rect(screen, RED, car)
    draw_mirrors(car)

    # Check if car is fully inside the parking zone
    if parking_zone.contains(car):
        score += 100
        level += 1
        if level > max_level:
            msg = font.render("You completed all 100 levels!", True, GREEN)
            screen.blit(msg, (WIDTH//2 - 150, HEIGHT//2))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False
        else:
            # Increase difficulty every 10 levels
            if level % 10 == 0 and car_speed < 10:
                car_speed += 1

            parking_zone = create_parking_zone(level)
            car.topleft = (WIDTH//2 - car_width//2, HEIGHT - 100)

    # UI
    screen.blit(font.render(f"Level: {level}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 40))
    screen.blit(font.render("Use Arrow Keys to Park the Car", True, WHITE), (WIDTH//2 - 150, HEIGHT - 30))

    pygame.display.update()

pygame.quit()
