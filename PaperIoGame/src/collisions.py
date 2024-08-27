import pygame


class Grid:
    def __init__(self, cell_size, world_width, world_height):
        self.cell_size = cell_size
        self.world_width = world_width
        self.world_height = world_height
        self.grid = {}
        self.initialize_grid()

    def initialize_grid(self):
        # Initialize grid cells
        num_cells_x = (self.world_width + self.cell_size - 1) // self.cell_size
        num_cells_y = (self.world_height + self.cell_size - 1) // self.cell_size
        for x in range(num_cells_x):
            for y in range(num_cells_y):
                self.grid[(x, y)] = []
    def add_object(self, obj):
        """Add an object to the grid."""
        if isinstance(obj, pygame.Rect):
            # Get grid cell coordinates
            cell_x = obj.x // self.cell_size
            cell_y = obj.y // self.cell_size
            # Ensure the cells exist
            for x in range(cell_x, cell_x + (obj.width // self.cell_size) + 1):
                for y in range(cell_y, cell_y + (obj.height // self.cell_size) + 1):
                    if (x, y) not in self.grid:
                        self.grid[(x, y)] = []
                    self.grid[(x, y)].append(obj)
        else:
            raise TypeError("Object must be a pygame.Rect.")

    def update_object_position(self, obj):
        """Update object position in the grid."""
        if isinstance(obj, pygame.Rect):
            # Remove object from old grid cells
            old_cells = self.get_cells_for_rect(obj)
            for cell in old_cells:
                if cell in self.grid and obj in self.grid[cell]:
                    self.grid[cell].remove(obj)
            
            # Add object to new grid cells
            self.add_object(obj)
        else:
            raise TypeError("Object must be a pygame.Rect.")


    def get_cells_for_rect(self, rect):
        """Get grid cells that a rectangle occupies."""
        cells = set()
        start_x = rect.x // self.cell_size
        start_y = rect.y // self.cell_size
        end_x = (rect.x + rect.width) // self.cell_size
        end_y = (rect.y + rect.height) // self.cell_size
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                cells.add((x, y))
        return cells

    def check_collisions(self, obj):
        """Check for collisions with other objects in the grid."""
        collisions = []
        if isinstance(obj, pygame.Rect):
            cells = self.get_cells_for_rect(obj)
            for cell in cells:
                for other in self.grid.get(cell, []):
                    if other != obj and obj.colliderect(other):
                        collisions.append(other)
        else:
            raise TypeError("Object must be a pygame.Rect.")
        return collisions
