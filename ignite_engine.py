# Importing modules
import pygame, sys
from pygame import *
window = pygame.display# Making alias "window" for "display"
pygame.init()# Initializing Pygame

# Color Pallete
black = 0,0,0

# Physics classes
class Body():
    def __init__(self, name, image):
        # Setting Variables
        self.name = name
        self.image = pygame.image.load(image)
        self.speed = [0,0]
        # Setting Physics
        self.collider = self.image.get_rect()

# UI classes
class Screen():
    def __init__(self, name, size):# Generating Screen
        # Setting variables
        self.name = name
        self.size = size
        # Initializing the screen
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

    def is_closed(self):# Killing program
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, objects):# Drawing Objects
        # Erasing Canvas
        self.canvas.fill(black)
        # Drawing Objects
        for object in objects:
            self.canvas.blit(object.image, object.collider)
        # Displaying Canvas
        window.flip()
