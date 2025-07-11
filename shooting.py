import pygame
import random
import time
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Game by Lokesh")
clock = pygame.time.Clock()

# Colors
WHITE, RED, BLACK, GREEN, YELLOW = (255, 255, 255), (255, 0, 0), (0, 0, 0), (0, 255, 0), (255, 255, 0)

# Sounds (use try-except if files not found)
try:
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    enemy_hit_sound = pygame.mixer.Sound('hit.wav')
    player_hit_sound = pygame.mixer.Sound('player_hit.wav')
except:
    shoot_sound = enemy_hit_sound = player_hit_sound = None

# Font
font = pygame.font.SysFont("Arial", 25)

# Game variables
score = 0
level = 1
kills = 0
kills_required = 5
max_level = 100
start_time = time.time()
gun_index = 0  # default gun

# Guns list (damage or speed upgrades can be added)
gun_colors = [WHITE, RED, GREEN, YELLOW, (0, 255, 255), (255, 0, 255), (100, 100, 255), (255, 255, 100), (200, 200, 200), (255, 150, 0)]

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        self.speed = 7

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, color):
        super().__init__()
        self.image = pygame.Surface((6, 12))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10 * direction

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH-40), random.randint(50, 150)))
        self.shoot_delay = random.randint(60, 180)

    def update(self):
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, 1, RED)
            enemy_bullets.add(bullet)
            self.shoot_delay = random.randint(60, 180)

# Groups
player = Player()
player_group = pygame.sprite.Group(player)
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

def spawn_enemies(num):
    for _ in range(num):
        enemies.add(Enemy())

spawn_enemies(kills_required)

# Game loop
running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gun selection (1 to 0 keys)
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                gun_index = event.key - pygame.K_1
            elif event.key == pygame.K_0:
                gun_index = 9

            # Shoot
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top, -1, gun_colors[gun_index])
                bullets.add(bullet)
                if shoot_sound:
                    shoot_sound.play()

    # Update
    player_group.update(keys)
    bullets.update()
    enemies.update()
    enemy_bullets.update()

    # Check collisions
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, enemies, True)
        for _ in hits:
            bullet.kill()
            if enemy_hit_sound:
                enemy_hit_sound.play()
            score += 10
            kills += 1

    if pygame.sprite.spritecollide(player, enemy_bullets, True):
        if player_hit_sound:
            player_hit_sound.play()
        msg = font.render("GAME OVER! You got shot!", True, RED)
        screen.blit(msg, (WIDTH//2 - 120, HEIGHT//2))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False
        continue

    # Level up
    if kills >= kills_required and level < max_level:
        level += 1
        kills = 0
        kills_required += 5
        spawn_enemies(kills_required)

    # Draw
    screen.fill(BLACK)
    player_group.draw(screen)
    bullets.draw(screen)
    enemies.draw(screen)
    enemy_bullets.draw(screen)

    # HUD
    elapsed_time = int(time.time() - start_time)
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (10, 40))
    screen.blit(font.render(f"Time: {elapsed_time}s", True, WHITE), (10, 70))
    screen.blit(font.render(f"Gun: {gun_index+1}", True, YELLOW), (10, 100))

    pygame.display.update()

pygame.quit()
