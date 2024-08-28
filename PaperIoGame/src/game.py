import pygame
import sys
from player import Player
from camera import Camera
from collisions import Grid

class Game:
    def __init__(self):
        pygame.init()
        self.background_color = (0, 0, 0)  # Black
        self.window_width = 800
        self.window_height = 600
        self.world_width = 1600
        self.world_height = 1200
        self.fullscreen = True
        self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Paper.io Inspired Game")

        # Create the grid for collision detection
        self.grid = Grid(cell_size=50, world_width=self.world_width, world_height=self.world_height)

        # Create the player and pass the grid to the Player class
        self.player = Player(
            color=(255, 0, 0),
            size=(50, 50),
            initial_position=(self.world_width // 2, self.world_height // 2),
            world_width=self.world_width,
            world_height=self.world_height,
            grid=self.grid  # Pass the grid object here
        )


        # Create the camera
        self.camera = Camera(self.window_width, self.window_height, self.world_width, self.world_height)

        # Create the grid for collision detection
        self.grid = Grid(cell_size=50, world_width=self.world_width, world_height=self.world_height)
        self.grid.add_object(self.player.get_rect())

        # Add static rectangles for testing
        self.static_rect1 = pygame.Rect(300, 300, 100, 100)
        self.static_rect2 = pygame.Rect(600, 500, 150, 150)
        self.grid.add_object(self.static_rect1)
        self.grid.add_object(self.static_rect2)

        # Add the static rectangles to a list for easier collision checking
        self.static_objects = [self.static_rect1, self.static_rect2]

        # Set up the clock
        self.clock = pygame.time.Clock()
        self.fps = 60

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.window = pygame.display.set_mode((self.window_width, self.window_height))
        else:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
        # Update camera dimensions based on the new window size
        self.window_width, self.window_height = self.window.get_size()
        self.camera.resize(self.window_width, self.window_height)
        
        self.fullscreen = not self.fullscreen

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.toggle_fullscreen()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Check for collisions with the trail
        if self.player.check_collision_with_trail():
            print("Collision with trail!")
            pygame.quit()
            sys.exit()

        # Check for collisions with static objects
        if self.player.check_collision_with_objects(self.static_objects):
            print("Collision with object!")
            pygame.quit()
            sys.exit()

        # Update the camera to follow the player
        self.camera.update(self.player.get_rect())

        # Update the player's position in the grid
        self.grid.update_object_position(self.player.get_rect())

    def draw(self):
        # Fill the background
        self.window.fill(self.background_color)

        # Draw the static objects
        for rect in self.static_objects:
            rect_drawn = self.camera.apply(rect)
            pygame.draw.rect(self.window, (0, 0, 255), rect_drawn)  # Blue for static rectangles

        # Draw the player's trail
        self.player.draw(self.window, self.camera)

        # Draw the player
        player_rect = self.camera.apply(self.player.get_rect())
        pygame.draw.rect(self.window, self.player.color, player_rect)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

            # Update the screen
            pygame.display.flip()

            # Cap the framerate
            self.clock.tick(self.fps)

if __name__ == "__main__":
    game = Game()
    game.run()
