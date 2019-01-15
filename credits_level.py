import pygame
from level_manager import *
from game_screen import *
from title_level import *
from read_file import *

class CreditsLevel():

    def __init__(self):
        font = pygame.font.SysFont('Calibri', 25, True, False)

        self._authors_text = font.render("Made by Christian Bowlinger, Carrie Mannila, and Camryn Roadley", True, constants.WHITE )

        self._sources_text1 = font.render("Sound effects from www.freesoundeffects.com", True, constants.WHITE )
        self._sources_text2 = font.render("Background music from http://incompetech.com", True, constants.WHITE )
        self._sources_text3 = font.render("Background & Character Images made with www.piskelapp.com", True, constants.WHITE)

        
        font = pygame.font.SysFont('Calibri', 15, True, False)
        self._instructions_text = font.render("Press esc to go back", True, constants.WHITE )

        # Open and read from text files
        self._objects_file = File('objects.txt')
        self._objects_list = self._objects_file.read_file()
        
        self._art = Art()
        self._background_image = self._art.get_image(self._objects_list[4])

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self._background_image, [0,0])

        screen.blit(self._authors_text, [7, 100] )

        screen.blit(self._sources_text1, [95, 150] )
        screen.blit(self._sources_text2, [90, 180] )
        screen.blit(self._sources_text3, [15, 210] )

        screen.blit(self._instructions_text, [0, 0] )

        
