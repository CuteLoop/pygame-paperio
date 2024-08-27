import pygame
import sys
from player import Player
from camera import Camera
from collisions import Grid

class Game:
    def __init__(self):
        pygame.init()
        self.background_color = (0, 0, 0)  # Negro
        self.window_width = 800
        self.window_height = 600
        self.world_width = 1600
        self.world_height = 1200
        self.fullscreen = True
        self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Paper.io Inspired Game")

        # Crear el jugador
        self.player = Player(
            color=(255, 0, 0),
            size=(50, 50),
            initial_position=(self.world_width // 2, self.world_height // 2),
            world_width=self.world_width,
            world_height=self.world_height
        )

        # Crear la cámara
        self.camera = Camera(self.window_width, self.window_height, self.world_width, self.world_height)

        # Crear la cuadrícula para detección de colisiones
        self.grid = Grid(cell_size=50, world_width=self.world_width, world_height=self.world_height)
        self.grid.add_object(self.player.get_rect())

        # Agregar rectángulos estáticos para prueba
        self.static_rect1 = pygame.Rect(300, 300, 100, 100)
        self.static_rect2 = pygame.Rect(600, 500, 150, 150)
        self.grid.add_object(self.static_rect1)
        self.grid.add_object(self.static_rect2)

        # Configuración del reloj
        self.clock = pygame.time.Clock()
        self.fps = 60

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

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Actualizar la cámara para seguir al jugador
        self.camera.update(self.player.get_rect())

        # Actualizar la posición del jugador en la cuadrícula
        self.grid.update_object_position(self.player.get_rect())

    def draw(self):
        # Llenar el fondo
        self.window.fill(self.background_color)

        # Dibujar la cuadrícula
        for rect in [self.static_rect1, self.static_rect2]:
            rect_drawn = self.camera.apply(rect)
            pygame.draw.rect(self.window, (0, 0, 255), rect_drawn)  # Azul para los rectángulos estáticos

        # Dibujar la ruta del jugador
        self.player.draw(self.window, self.camera)

        # Dibujar al jugador
        player_rect = self.camera.apply(self.player.get_rect())
        pygame.draw.rect(self.window, self.player.color, player_rect)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()

            # Actualizar la pantalla
            pygame.display.flip()

            # Limitar la velocidad de fotogramas
            self.clock.tick(self.fps)

if __name__ == "__main__":
    game = Game()
    game.run()
