import pygame

class Camera:
    def __init__(self, width, height, world_width, world_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.world_rect = pygame.Rect(0, 0, world_width, world_height)

    def apply(self, rect):
        """Translate a pygame.Rect object's position based on the camera's position."""
        return rect.move(self.camera.topleft)

    def update(self, target):
        """Center the camera on the target entity and constrain within the world bounds."""
        if hasattr(target, 'rect'):
            # Target has a rect attribute
            target_rect = target.rect
        else:
            # Target is a pygame.Rect
            target_rect = target

        x = -target_rect.centerx + int(self.camera.width / 2)
        y = -target_rect.centery + int(self.camera.height / 2)

        # Constrain the camera to the bounds of the world
        x = max(-(self.world_rect.width - self.camera.width), min(0, x))
        y = max(-(self.world_rect.height - self.camera.height), min(0, y))

        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)
