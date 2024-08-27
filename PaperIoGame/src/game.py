import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paper.io Inspired Game")

# Game loop
def game_loop():
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        window.fill(BACKGROUND_COLOR)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    game_loop()
