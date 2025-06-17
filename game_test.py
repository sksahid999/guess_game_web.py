import pygame
import sys

# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))  # Fill screen with blue
    pygame.display.flip()

pygame.quit()
sys.exit()
