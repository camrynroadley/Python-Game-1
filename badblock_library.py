import pygame
import random
from block_library import Block

class Bad_Block(Block):
    #inherits from the Block class in block_library
    def update(self):
        self.rect.y = self.rect.y + 2
        
        if self.rect.y > 385:
            self.rect.y = 0
