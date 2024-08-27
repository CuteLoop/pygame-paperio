import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.background_color = (0, 0, 0)  # Black
        self.window_width = 800
        self.window_height = 600
        self.fullscreen = True
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Paper.io Inspired Game")

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.window = pygame.display.set_mode((self.window_width, self.window_height))
        else:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fullscreen = not self.fullscreen

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.toggle_fullscreen()

    def run(self):
        while True:
            self.handle_events()
            self.window.fill(self.background_color)
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
