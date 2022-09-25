"""A module for the snake blocks."""

from time import sleep

import pygame
import random

from settings import Settings

class Snake():
    """A class for handling the snake sprites."""

    def __init__(self, snake_game):
        """initialize and create the blocks."""
        super().__init__()
        self.settings = Settings()
        self.scale = self.settings.scale
        self.screen = snake_game.screen

        #Initialize the snake block
        self.snake_rect = pygame.Rect(0, 0, self.scale-1, self.scale-1)
        self.snake_rect.topleft = self.screen.get_rect().center
        self.snake_color = self.settings.snake_color

        #Initializing the movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        #Initialize last_position flag.
        self.last_position = (0, 0)

    def movement_flag_reset(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    def movement_direction(self):
        """Setting the direction for the movement of the blocks."""
        if self.moving_up:
            self.snake_rect.y -= self.scale
        elif self.moving_down:
            self.snake_rect.y += self.scale
        elif self.moving_left:
            self.snake_rect.x -= self.scale
        elif self.moving_right:
            self.snake_rect.x += self.scale

    def position_flag_set(self):
        """Record the last position of the current snake block."""
        self.last_position = self.snake_rect.center

    def draw_snake(self):
        """Drawing the snake blocks to the screen."""
        pygame.draw.rect(self.screen, self.snake_color, self.snake_rect)
