"""A Snake style game."""

import sys
from time import sleep

import pygame

from snake import Snake
from settings import Settings
from snake_food import SnakeFood
from buttons import Button
from score import Score

class SnakeGame:
    """Overall class to merge assetts and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #Setting up the main window
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        pygame.display.set_caption("Snake")

        self.snake_food = SnakeFood(self)
        self.snake_food.snake_food_placement(self)

        #A dictionary containing all of the individual snake blocks.
        self.snake_dict = {}
        self.snake_dict[0] = Snake(self)

        #Create the play button
        self.play_button = Button(self, "Play")

        #Create a scoreboard.
        self.sb = Score(self)

    def run_game(self):
        """Start running the game."""
        while True:
            self._check_events()

            if self.settings.game_active:
                self._check_food_collisions()            
                self._check_edges()
                self._check_self_collisions()
                self.snake_dict[0].movement_direction()
                self.block_position_update()
                for block in self.snake_dict.values():
                    block.position_flag_set()

            self._update_screen()
            sleep(self.settings.game_tempo)

            if not self.settings.game_active:
                pygame.mouse.set_visible(True)

    def _check_events(self):
        """Check for all events during gameplay."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)
    
    def _check_buttons(self, mouse_pos):
        """Check if a button was pressed."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.settings.game_active:
            #Set the game mode to active:
            self.settings.game_active = True

            self.sb.prep_score()
            self.sb.prep_high_score()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Checking for keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP and not self.snake_dict[0].moving_down:
            self.snake_dict[0].movement_flag_reset()
            self.snake_dict[0].moving_up = True
        elif event.key == pygame.K_DOWN and not self.snake_dict[0].moving_up:
            self.snake_dict[0].movement_flag_reset()
            self.snake_dict[0].moving_down = True
        elif event.key == pygame.K_LEFT and not self.snake_dict[0].moving_right:
            self.snake_dict[0].movement_flag_reset()
            self.snake_dict[0].moving_left = True
        elif event.key == pygame.K_RIGHT and not self.snake_dict[0].moving_left:
            self.snake_dict[0].movement_flag_reset()
            self.snake_dict[0].moving_right = True

    def _check_keyup_events(self, event):
        """Check for key releases."""

    def _check_edges(self):
        """Checking if the snake is trying to escape the screen."""
        #The snake only stops, when the head is on the edge
        #and the movement flag points in the wrong direction.
        #Then the game ends.
        if (self.snake_dict[0].snake_rect.left < self.settings.scale
            and self.snake_dict[0].moving_left):
            self.snake_dict[0].movement_flag_reset()
            self.settings.game_active = False
        elif (self.snake_dict[0].snake_rect.right > self.screen_width
            - self.settings.scale and self.snake_dict[0].moving_right):
            self.snake_dict[0].movement_flag_reset()
            self.settings.game_active = False
        elif (self.snake_dict[0].snake_rect.top < self.settings.scale
            and self.snake_dict[0].moving_up):
            self.snake_dict[0].movement_flag_reset()
            self.settings.game_active = False
        elif (self.snake_dict[0].snake_rect.bottom > self.screen_height
            - self.settings.scale and self.snake_dict[0].moving_down):
            self.snake_dict[0].movement_flag_reset()
            self.settings.game_active = False

    def _check_food_collisions(self):
        """Checking the collision between the snake and the food."""
        #When the snakes head hits the food, a new block appears,
        #and the snake gets longer by one block.
        if (self.snake_food.food_rect.center ==
                self.snake_dict[0].snake_rect.center):
            
            self.snake_food.snake_food_placement(self)
            index = len(self.snake_dict)
            self.snake_dict[index] = Snake(self)

            #Update the scoreboard
            self.sb.score += self.settings.point
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_high_score()
    
    def _check_self_collisions(self):
        """Check if the snake has hit itself."""
        for block in self.snake_dict.values():
            if self.snake_dict[0].snake_rect.center == block.snake_rect.center:
                if not block == self.snake_dict[0]:
                    self.settings.game_active = False
                else:
                    pass

    def block_position_update(self):
        """Update each block's position after the first one."""
        #Change the new blocks position equal to the previous blocks last pos.,
        #The first block is set near the center of the screen.
        #This should be left as is.
        for num in range(1, len(self.snake_dict)):
            self.snake_dict[num].snake_rect.center = (
                self.snake_dict[num-1].last_position
            )

    def _update_screen(self):
        """Update images and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        #Draw the play button if the game hasn't started yet.
        if not self.settings.game_active:
            self.play_button.draw_button()
        else:
            for block in self.snake_dict.values():
                block.draw_snake()
            self.snake_food.draw_snake_food()
            self.sb.show_score()
        
        pygame.display.flip()
        

if __name__ == '__main__':
    sn = SnakeGame()
    sn.run_game()
