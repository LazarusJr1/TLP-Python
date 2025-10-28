import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemy_circles = []
enemy_radius = 20
spawn_timer = 0

# function to spawn an enemy circle
def spawn_enemy():
    x_pos = random.randint(0, screen.get_width())
    enemy_circles.append(pygame.Vector2(x_pos, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("purple")

    pygame.draw.circle(screen, "blue", (int(player_pos.x), int(player_pos.y)), 20)


    for enemy in enemy_circles:
        enemy.y += 200 * dt  # Move enemy down
        pygame.draw.circle(screen, "red", (int(enemy.x), int(enemy.y)), enemy_radius)

    for enemy in enemy_circles:
        if player_pos.distance_to(enemy) < 40 + enemy_radius:  # Collision detection
            screen.fill("black")  # Change screen to black
            pygame.display.flip()  # Update display
            pygame.time.delay(1000)  # Wait for 1 second
            running = False  # End the game

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    spawn_timer += dt
    if spawn_timer >= 0.1: 
        spawn_enemy()
        spawn_timer = 0


    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()