import pygame

class Player:
    def __init__(self, color, size, initial_position, world_width, world_height, grid):
        self.color = color
        self.size = size
        self.rect = pygame.Rect(initial_position[0], initial_position[1], size[0], size[1])
        self.world_width = world_width
        self.world_height = world_height
        self.trail = []
        self.grid = grid
        self.grid.add_object(self.rect)
        self.trail_delay = 5  # Delay before trail becomes active for collisions

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

        # Update the player's position in the grid
        self.grid.update_object_position(self.rect)

    def update_trail(self):
        """Update the trail with the current position."""
        new_trail_rect = self.rect.copy()
        self.trail.append(new_trail_rect)
        
        # Add to grid only if trail is old enough
        if len(self.trail) > self.trail_delay:
            self.grid.add_object(self.trail[-self.trail_delay])

        # Keep the trail size reasonable
        if len(self.trail) > 50:
            old_trail_rect = self.trail.pop(0)
            old_cells = self.grid.get_cells_for_rect(old_trail_rect)
            for cell in old_cells:
                if old_trail_rect in self.grid.grid[cell]:
                    self.grid.grid[cell].remove(old_trail_rect)

    def draw(self, surface, camera):
        """Draw the player and the trail on the screen."""
        # Draw player
        player_rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, player_rect)

        # Draw trail
        for rect in self.trail[self.trail_delay:]:  # Skip the first few rectangles in the trail
            trail_rect = camera.apply(rect)
            pygame.draw.rect(surface, (0, 255, 0), trail_rect)  # Green trail

    def check_collision_with_trail(self):
        """Check if the player collides with its own trail."""
        collisions = self.grid.check_collisions(self.rect)
        for collision in collisions:
            if collision in self.trail[:-self.trail_delay]:  # Exclude the most recent trail rectangles
                return True
        return False

    def check_collision_with_objects(self, objects):
        """Check if the player collides with other objects."""
        collisions = self.grid.check_collisions(self.rect)
        for collision in collisions:
            if collision in objects:
                return True
        return False

    def get_rect(self):
        """Return the player's rect."""
        return self.rect
