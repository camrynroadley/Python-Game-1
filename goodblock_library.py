import pygame
import random
from block_library import Block

class Good_Block(Block):
    #inherits from the Block class in block_library
    def update(self):
        self.rect.x += int(random.uniform(-4,4))
        self.rect.y += int(random.uniform(-4,4))
