# Importing modules-------------------------------------------------------------
import pygame, sys
from pygame import *
pygame.init()

# Variables---------------------------------------------------------------------
list = []

# Color Pallete-----------------------------------------------------------------
black = 0,0,0

# Aliases-----------------------------------------------------------------------
error = 'something went wrong..'
window = pygame.display

# Node Class--------------------------------------------------------------------
class Node:

    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []

    def add(self, node_class, data):# Add Child Node
        new_child = node_class(self, data)
        self.children.append(new_child)
        return new_child

# Scene2D Node------------------------------------------------------------------
class Scene2D(Node):
    def __init__(self, parent, data):
        super().__init__(parent, 'Scene2D')
        self.canvas = pygame.Surface((data[0], data[1]))

    def draw(self):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children.values():# Drawing Objects
            self.canvas.blit(child.image, child.motion)

# Body2D Node-------------------------------------------------------------------
class Body2D(Node):

    def __init__(self, parent, data):
        super().__init__(parent, 'Body2D')
        self.image = pygame.image.load(data[0])
        self.speed = [0,0]
        self.collider = self.image.get_rect()
        self.motion = self.collider.move(self.speed)

# Root Node---------------------------------------------------------------------
# This is the 'root' node. It is the object that letter is exported as the 'game'
# It is the reponsible of managing every other node.

class Root(Node):

    def __init__(self, settings):
        super().__init__(None, settings['name'])
        self.size = settings['width'], settings['height']
        self.running = True
        self.current_scene

    def __call__(self):# Run the game
        window_init()
        run_loop()

# Main functions----------------------------------------------------------------
    def window_init(self):# Create 'canvas' variable.
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

    def run_loop(self):# Main loop.
        while self.running:

            self.check_events()
            self.update()
            self.draw()

        self.close_program()

    def check_events(self):
        for event in pygame.event.get():# Check 'QUIT' event.
            if event.type == QUIT:
                self.running = False

    def close_program(self):# Securely close program
        pygame.quit()
        sys.exit()

# Updating----------------------------------------------------------------------
    def update(self):
        try:
            pass
        except: pass

# Drawing-----------------------------------------------------------------------
    def draw(self, image, motion):
        self.canvas.fill(black)# Erasing Canvas
        self.canvas.blit(current_scene)
        window.flip()# Displaying Canvas
