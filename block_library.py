import pygame
import random
from art import *
import constants

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, image_location, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        #Get block art
        self._art = Art()
        # Load the image
        self.image = self._art.get_image(image_location)
        # Set our transparent color
        self.image.set_colorkey(constants.WHITE)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
