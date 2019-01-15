"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4

Program updated and modified by Christian Bowlinger
"""
import pygame
import random
import block_library
import goodblock_library
import badblock_library
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (0,     0, 255)
GREEN = (0,   255,   0)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
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


# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

#set x_speed, y_speed, player_keyboard_x, and player_keyboard_y for player
x_speed = 0
y_speed = 0
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    good_block = goodblock_library.Good_Block(GREEN, 20, 15)
    bad_block = badblock_library.Bad_Block(RED, 20, 15)
 
    # Set a random location for the block
    good_block.rect.x = random.randrange(screen_width)
    good_block.rect.y = random.randrange(screen_height)

    bad_block.rect.x = random.randrange(screen_width)
    bad_block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    good_block_list.add(good_block)
    bad_block_list.add(bad_block)
    
    all_sprites_list.add(good_block)
    all_sprites_list.add(bad_block)
 
# Create a BLUE player block
player = Player(350, 200)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        #place for sound bytes for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -2
                player.changespeed(x_speed, 0)
                    
            elif event.key == pygame.K_RIGHT:
                x_speed = 2
                player.changespeed(x_speed, 0)
                    
            elif event.key == pygame.K_UP:
                y_speed = -2
                player.changespeed(0, y_speed)
                    
            elif event.key == pygame.K_DOWN:
                y_speed = 2
                player.changespeed(0, y_speed)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_speed = -2
                player.changespeed(x_speed, 0)
                
            elif event.key == pygame.K_DOWN:
                y_speed = -2
                player.changespeed(0, y_speed)

            elif event.key == pygame.K_UP:
                y_speed = 2
                player.changespeed(0, y_speed)

            elif event.key == pygame.K_LEFT:
                x_speed = 2
                player.changespeed(x_speed, 0)

    #add sounds for hitting barriers in these if statements!
    if player.rect.x < 0:
        x_speed = 2
        player.rect.x = 0
            
    if player.rect.x > 685:
        x_speed = 0
        player.rect.x = 685

    if player.rect.y < 0:
        y_speed = 2
        player.rect.y = 0

    if player.rect.y > 385:
        y_speed = -2
        player.rect.y = 385

    #update all sprites
    all_sprites_list.update()
 
    # Clear the screen
    screen.fill(WHITE)

 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)

    #place text assigning place for score
    font = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [30, 5])
 
    # Check the list of collisions.
    for block in good_blocks_hit_list:      #positive sound for getting a good block
        score += 1

    for block in bad_blocks_hit_list:       #negative sound for getting a bad block
        score -= 1
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
