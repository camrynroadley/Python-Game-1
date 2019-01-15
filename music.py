import pygame
from pygame import mixer

class Music():

    def __init__(level):
        pass

    def play_once(self, id):
        #pygame.mixer.music.load(id)
        #pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        #pygame.mixer.music.play()
        pygame.mixer.Sound(id).play()

    def play_repeat(self, id):
        pygame.mixer.music.load(id)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play(-1)

    def stop_repeat(self, id):
        pygame.mixer.music.load(id)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.stop()
        
