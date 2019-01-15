import constants
import pygame
from art import *
from read_file import *

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Open and read from files
        self._objects_file = File('objects.txt')
        self._objects_list = self._objects_file.read_file()

        #Get player art
        self._art = Art()
        # Load the image
        self.image = self._art.get_image(self._objects_list[7])
        # Set our transparent color
        self.image.set_colorkey(constants.WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
