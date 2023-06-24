# Info--------------------------------------------------------------------------
# This is the 'root' node. It is the object that letter is exported as the
# 'game'. It is the reponsible of managing every other node.

# Importing modules-------------------------------------------------------------
import pygame, sys, node, scene, interface, physics, audio, sprites
from pygame import *
pygame.init()
sys.path.append('.')

# Node library------------------------------------------------------------------
types = {
'Body':physics_nodes.Body,
'Level':fuel.Level
}

# Color Pallete-----------------------------------------------------------------
black = 0,0,0

# Aliases-----------------------------------------------------------------------
error = 'something went wrong..'
window = pygame.display

# Root Node---------------------------------------------------------------------
class Root(node.Node):

    def __init__(self, parent, settings):
        super().__init__(parent, settings['name'])
        self.size = settings['width'], settings['height']
        self.running = True
        self.current_scene

# Main functions----------------------------------------------------------------
    def window_init(self):
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

    def start_program(self):
        window_init()
        run_loop()

    def run_loop(self):
        while self.running:

            self.check_close_event()
            self.update()
            self.draw()

        self.close_program()

    def check_close_event(self):# Checking QUIT event
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def close_program(self):
        pygame.quit()

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
