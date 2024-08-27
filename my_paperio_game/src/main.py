import pygame
import sys


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)  # Black background

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paper.io-inspired Game")


# Import the Player class

from player import Player

# Constants
PLAYER_COLOR = (255, 0, 0)  # Red player
PLAYER_SIZE = (50, 50)
PLAYER_SPEED = 5

# Create a player instance
player = Player(PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Draw
    screen.fill(BG_COLOR)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()
