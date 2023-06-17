# Importing modules
import pygame, interface_nodes, physics_nodes, audio_nodes, sprite_nodes
from pygame import *
window = pygame.display# Making alias "window" for "display"
pygame.init()# Initializing Pygame


# Color Pallete
black = 0,0,0

class root():
    def __init__(self, name, width, height):# Creating Screen
        # Setting sariables
        self.name = name
        self.size = width, height
        # Initializing Screen
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
            self.canvas.blit(object.image, object.motion)
        # Displaying Canvas
        window.flip()
