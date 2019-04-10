# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Platforming Experiment"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)

# Game loop
done = False

# Classes

class player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 5
    

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic (Check for collisions, update points, etc.)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        pass
    elif pressed[pygame.K_RIGHT]:
        pass
           
    if pressed[pygame.K_UP]:
        pass 
    elif pressed[pygame.K_DOWN]:
        pass
    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
