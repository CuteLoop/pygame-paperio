import pygame

class Player:
    def __init__(self, color, size, initial_position, world_width, world_height):
        self.color = color
        self.size = size
        self.rect = pygame.Rect(initial_position[0], initial_position[1], size[0], size[1])
        self.world_width = world_width
        self.world_height = world_height
        self.trail = []

    def update(self, keys):
        """Update the player's position based on key presses."""
        speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed

        # Constrain player within the world bounds
        self.rect.x = max(0, min(self.rect.x, self.world_width - self.size[0]))
        self.rect.y = max(0, min(self.rect.y, self.world_height - self.size[1]))

        # Update the trail
        self.update_trail()

    def update_trail(self):
        """Update the trail with the current position."""
        self.trail.append(self.rect.copy())
        # Keep the trail size reasonable
        if len(self.trail) > 50:
            self.trail.pop(0)

    def draw(self, surface, camera):
        """Draw the player and the trail on the screen."""
        # Draw player
        player_rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, player_rect)

        # Draw trail
        for rect in self.trail:
            trail_rect = camera.apply(rect)
            pygame.draw.rect(surface, (0, 255, 0), trail_rect)  # Green trail

    def get_rect(self):
        """Return the player's rect."""
        return self.rect
