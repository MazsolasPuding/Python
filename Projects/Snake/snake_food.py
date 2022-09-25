"""Managing the food for the sanke."""

import pygame
import random

from settings import Settings

class SnakeFood():
    """Create food for the snake."""

    def __init__(self, snake_game):
        """Ininitalize snake food."""
        self.settings = Settings()
        self.scale = self.settings.scale
        self.screen = snake_game.screen

        self.food_rect = pygame.Rect(0, 0, self.scale-1, self.scale-1)
        self.food_color = self.settings.food_color

    def snake_food_placement(self, snake_game):
        """Placing random rects on the screen as snake food."""
        #Number of possible positions on the x axis.
        x_positions = int(snake_game.screen_width // self.scale)
        y_positions = int(snake_game.screen_height // self.scale)
        #Setting random x and y position values
        x_value = random.randint(0, x_positions-1)
        y_value = random.randint(0, y_positions-1)
        #Giving the random values to the rect
        self.food_rect.x = x_value * self.scale
        self.food_rect.y = y_value * self.scale
    
    
    def draw_snake_food(self):
        """Drawing the snake food to the screen."""
        pygame.draw.rect(self.screen, self.settings.food_color, self.food_rect)
