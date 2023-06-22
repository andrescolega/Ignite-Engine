# Importing modules-------------------------------------------------------------
import pygame, sys, fuel, interface_nodes, physics_nodes, audio_nodes, sprite_nodes
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
class Root(fuel.Node):# Root node

    def __init__(self, settings):
        super().__init__(settings['name'])
        self.size = settings['width'], settings['height']
        self.running = True

    def init(self):
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)
        self.run()

# Main Loop---------------------------------------------------------------------
    def run(self):
        while self.running:

            self.check_close_event()
            self.update()

        self.close_program()


# Closing program-----------------------------------------------------------------
    def check_close_event(self):
        for event in pygame.event.get():# Checking QUIT event
            if event.type == QUIT:
                self.running = False

    def close_program(self):
        pygame.quit()

# Updating Children-------------------------------------------------------------
    def update(self):
        try:
            pass
        except: pass

# Drawing Children--------------------------------------------------------------
    def draw(self, image, motion):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children.values():# Drawing Objects
            self.canvas.blit(child)

        window.flip()# Displaying Canvas
