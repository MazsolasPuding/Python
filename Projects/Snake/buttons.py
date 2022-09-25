"""Making buttons in Snake."""

import pygame.font

class Button:
    """Store all button attributes."""
    
    def __init__(self, snake_game, msg):
        """initialize button attributes."""
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set dimensions and properties of the play button
        self.width, self.height = 200, 50
        self.button_color = (150, 150, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the buttons rectobject and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a render image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the blank button and draw the message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
