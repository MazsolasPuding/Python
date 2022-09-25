"""Store all the settings for Snake."""

class Settings:
    """Settings for Snake."""

    def __init__(self):
        """Initialize the game's static settings."""
        
        #Main display background color
        self.bg_color = (100, 100, 180)
        #The color of the snake
        self.snake_color = (100, 200, 100)
        #The color of the food
        self.food_color = (200, 100, 100)
        #Time between each step
        self.game_tempo = 0.08
        #The size of the snake's building blocks
        self.scale = 20
        #The activation flag for the game.
        self.game_active = False
        #Points for each ate snakefood.
        self.point = 1