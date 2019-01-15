import pygame

class Art():

    def __init__(level):
        pass

    def get_image(self, location):
        image = pygame.image.load(location).convert()
        return image
