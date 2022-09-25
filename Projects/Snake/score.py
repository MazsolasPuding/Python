"""Keeping score for the game."""

import pygame.font

class Score:
    """A class for keeping score."""

    def __init__(self, snake_game):
        """Initialize scorekeeping attributes."""
        self.screen = snake_game.screen
        self.screen_rect = snake_game.screen_rect
        self.settings = snake_game.settings
        
        self.score = 0
        self.load_high_score()

        #Font settings for scroing information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 58)

        #Prepare the initaial scoring images.
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "Score: " + "{:,}".format(self.score)
        self.score_img = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        
        #Display the score at the top right of the screen.
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn the highscore into a rendered image."""
        high_score_str = "Highscore: " + "{:,}".format(self.high_score)
        self.high_score_img = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        #Display the score at the top right of the screen.
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.left = 20
        self.high_score_rect.top = 20
    

    def load_high_score(self):
        """Load the saved highscore."""
        try:
            file_path = "save/save_game.txt"
            with open(file_path) as save_f:
                save = save_f.read()
        except FileNotFoundError:
            self.high_score = 0
            save = 0
        
        try:
            self.high_score = int(save)
        except ValueError:
            self.high_score = 0
    
    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
    
    def check_high_score(self):
        """Check if there's a new highscore."""
        if self.score > self.high_score:
            self.high_score = self.score

            file_path = "save/save_game.txt"
            with open(file_path, 'w') as save_f:
                save_f.write(str(self.high_score))
            
            self.prep_high_score
