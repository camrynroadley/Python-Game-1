import pygame
import constants
import random
import block_library
import goodblock_library
import badblock_library
import player
from level_manager import *
from screen import *
from music import *
from art import *
from read_file import *

class GameScreen(Screen): 
    def __init__(self):

        self._size = 50
        self._rect_x = 50
        self._rect_y = 50
        self._rect_change_x = 2
        self._rect_change_y = 2
        
        self._score = 0

        # Create a BLUE player block
        self._player = player.Player(350, 200)

        # Set the height and width of the screen
        self._screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

        #set x_speed, y_speed, player_keyboard_x, and player_keyboard_y for player
        self._x_speed = 0
        self._y_speed = 0
         
        # This is a list of 'sprites.' Each block in the program is
        # added to this list. The list is managed by a class called 'Group.'
        self._good_block_list = pygame.sprite.Group()
        self._bad_block_list = pygame.sprite.Group()
         
        # This is a list of every sprite. 
        # All blocks and the player block as well.
        self._all_sprites_list = pygame.sprite.Group()

        self._all_sprites_list.add(self._player)

        self._music = Music()
        self._art = Art()

        # Open and read from text files
        self._objects_file = File('objects.txt')
        self._sounds_file = File('sounds.txt')

        self._background_image = self._art.get_image(self._objects_file.get_item_name("game_background"))
        

        for i in range(50):
            # This represents a block
            good_block = goodblock_library.Good_Block(self._objects_file.get_item_name("good_block"), 20, 15)
            bad_block = badblock_library.Bad_Block(self._objects_file.get_item_name("bad_block"), 20, 15)
         
            # Set a random location for the block
            good_block.rect.x = random.randrange(constants.SCREEN_WIDTH)
            good_block.rect.y = random.randrange(constants.SCREEN_HEIGHT)

            bad_block.rect.x = random.randrange(constants.SCREEN_WIDTH)
            bad_block.rect.y = random.randrange(constants.SCREEN_HEIGHT)
         
            # Add the block to the list of objects
            self._good_block_list.add(good_block)
            self._bad_block_list.add(bad_block)
            
            self._all_sprites_list.add(good_block)
            self._all_sprites_list.add(bad_block)

        

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                self._music.stop_repeat(self._sounds_file.get_item_name("game_music"))
                self._music.play_repeat(self._sounds_file.get_item_name("title_credits_music"))

            elif event.key == pygame.K_LEFT:
                self._x_speed = -2
                self._player.changespeed(self._x_speed, 0)
                    
            elif event.key == pygame.K_RIGHT:
                self._x_speed = 2
                self._player.changespeed(self._x_speed, 0)
                    
            elif event.key == pygame.K_UP:
                self._y_speed = -2
                self._player.changespeed(0, self._y_speed)
                    
            elif event.key == pygame.K_DOWN:
                self._y_speed = 2
                self._player.changespeed(0, self._y_speed)
     
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self._x_speed = -2
                self._player.changespeed(self._x_speed, 0)
                
            elif event.key == pygame.K_DOWN:
                self._y_speed = -2
                self._player.changespeed(0, self._y_speed)

            elif event.key == pygame.K_UP:
                self._y_speed = 2
                self._player.changespeed(0, self._y_speed)

            elif event.key == pygame.K_LEFT:
                self._x_speed = 2
                self._player.changespeed(self._x_speed, 0)

                    

    def update(self):

        #add sounds for hitting barriers in these if statements!
        if self._player.rect.x < 0:
            self._x_speed = 2
            self._player.rect.x = 0
                
        if self._player.rect.x > 687:
            self._x_speed = 0
            self._player.rect.x = 687

        if self._player.rect.y < 0:
            self._y_speed = 2
            self._player.rect.y = 0

        if self._player.rect.y > 378:
            self._y_speed = -2
            self._player.rect.y = 378
        
        #Move the object based on the speed
        self._rect_x += self._rect_change_x
        self._rect_y += self._rect_change_y
     
        # Bounce the square if needed
        if self._rect_y > constants.SCREEN_HEIGHT - self._size or self._rect_y < 0:
            self._rect_change_y = self._rect_change_y * -1
        if self._rect_x > constants.SCREEN_WIDTH - self._size or self._rect_x < 0:
            self._rect_change_x = self._rect_change_x * -1

        #update all sprites
        self._all_sprites_list.update()

        # See if the player block has collided with anything.
        good_blocks_hit_list = pygame.sprite.spritecollide(self._player, self._good_block_list, True)
        bad_blocks_hit_list = pygame.sprite.spritecollide(self._player, self._bad_block_list, True)

        # Check the list of collisions.
        for block in good_blocks_hit_list:      #positive sound for getting a good block
            self._score += self._objects_file.get_points("good_block")
            self._music.play_once(self._sounds_file.get_item_name("good_sound"))

        for block in bad_blocks_hit_list:       #negative sound for getting a bad block
            self._score += self._objects_file.get_points("bad_block")
            self._music.play_once(self._sounds_file.get_item_name("bad_sound"))

        
    def draw(self, screen):
        # Clear the screen
        #screen.fill(constants.WHITE)
        screen.blit(self._background_image, [0,0])
        

        #place text assigning place for score
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text = font.render("Score: " + str(self._score), True, constants.WHITE)
        screen.blit(text, [30, 20])

        #place instructions text
        font = pygame.font.SysFont('Calibri', 15, True, False)
        instructions_text = font.render("Press esc to go back", True, constants.WHITE )
        screen.blit(instructions_text, [0, 0])
     
        # Draw all the spites
        self._all_sprites_list.draw(screen)
