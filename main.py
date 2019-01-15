import pygame
import random
import block_library
import goodblock_library
import badblock_library
from level_manager import *
from title_level import *
import constants

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

level_manager = LevelManager()
level_manager.load_level(TitleLevel())

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
 
# -------- Main Program Loop -----------
while not done:
    current_level = level_manager.get_current_level()

    #We've left the TitleScreen - Exit the game
    if current_level == None:
        break

    #Needs Game Logic
    #screen.fill(constants.WHITE)
    current_level.update()
    current_level.draw(screen)
 
    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            #done = True
            break
        current_level.handle_keyboard_event(event)
        

pygame.quit()



