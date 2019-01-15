import pygame
import constants
from level_manager import *
from game_screen import *
from credits_level import *
from read_file import *

class TitleLevel():

    def __init__(self):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self._title_text = font.render("Our Game", True, constants.WHITE )
        
        font = pygame.font.SysFont('Calibri', 15, True, False)
        self._instructions_text = font.render("Press p to play game, c to go to credits screen, or esc to quit", True, constants.WHITE )

        self._objects_file = File('objects.txt')
        self._sounds_file = File('sounds.txt')

        self._art = Art()
        self._background_image = self._art.get_image(self._objects_file.get_item_name("title_background"))

        self._music = Music()
        self._music.play_repeat(self._sounds_file.get_item_name("title_credits_music"))

    def handle_keyboard_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                self._music.stop_repeat(self._sounds_file.get_item_name("title_credits_music"))
            elif event.key == pygame.K_p:
                LevelManager().load_level(GameScreen())
                self._music.stop_repeat(self._sounds_file.get_item_name("title_credits_music"))
                self._music.play_repeat(self._sounds_file.get_item_name("game_music"))
            elif event.key == pygame.K_c:
                LevelManager().load_level(CreditsLevel())

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self._background_image, [0,0])

        screen.blit(self._title_text, [100, 100] )

        screen.blit(self._instructions_text, [0, 0] )
