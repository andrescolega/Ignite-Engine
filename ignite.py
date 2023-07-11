#=============================== Ignite Engine =================================
                """THIS CODE IS UNDER THE GNU 3.0 LICENSE"""


#============================ NO OBJECT-BASED CODE =============================
# Importing modules-------------------------------------------------------------
import pygame, sys
from pygame import *
pygame.init()

# Color Pallete-----------------------------------------------------------------
black = 0,0,0

# Aliases-----------------------------------------------------------------------
error = 'something went wrong..'
window = pygame.display

#==================================== SEED =====================================

# Node Class--------------------------------------------------------------------
class Node:

    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = []

    def add(self, node_class, data: list):# Add Child Node
        new_child = node_class(self, data)
        self.children.append(new_child)
        return new_child

# RANK 3 ======================== OBJECT NODES =================================

# Body2D Node-------------------------------------------------------------------
class Body2D(Node):

    def __init__(self, parent, data):
        super().__init__(parent, 'Body2D')
        self.image = pygame.image.load(data[0])
        self.speed = [0,0]
        self.collider = self.image.get_rect()
        self.motion = self.collider.move(self.speed)

# RANK 2 ========================= SCENE NODES =================================

# Scene2D Node------------------------------------------------------------------
class Scene2D(Node):
    def __init__(self, parent, data):
        super().__init__(parent, 'Scene2D')
        self.canvas = pygame.Surface(data[0])
        self.position = self.canvas.get_rect()
        self.current = False

    def check_current(self):# Check if self is tagged as the current scene
        if self.current == True:
            self.parent.current_scene = self

    def update(self):# Update node and children
        self.check_current()
        self.draw()

    def draw(self):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children:# Drawing Objects
            self.canvas.blit(child.image, child.motion)



# RANK 1 ========================== ROOT NODE ==================================

# Root Node---------------------------------------------------------------------
"""
This is the 'root' node. It is the object that letter is exported as the 'game'.
It is the reponsible of managing every other node.
"""

class Root(Node):

    def __init__(self, name, width, height):
        super().__init__(None, name)
        self.size = width, height
        self.running = True
        self.current_scene = None

    def __call__(self):# Run the game
        self.window_init()
        self.run_loop()

# Main functions----------------------------------------------------------------
"""
This is actually the game.
"""

    def window_init(self):# Create 'canvas' variable.
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

    def run_loop(self):# Main game loop.
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
    def update(self):# Update children
        for child in self.children:
            child.update()

# Drawing-----------------------------------------------------------------------
    def draw(self):# Draw children
        self.canvas.fill(black)# Erasing canvas
        self.canvas.blit(self.current_scene.canvas, self.current_scene.position)
        window.flip()# Displaying Canvas
