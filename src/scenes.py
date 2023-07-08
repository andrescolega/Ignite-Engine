# Importing modules-------------------------------------------------------------
import pygame, node
from pygame import *
pygame.init()

# Surface/Escene Node------------------------------------------------------------
class Scene2D(node.Node):
    def __init__(self, parent, name, data):
        super().__init__(parent, name)
        self.canvas = pygame.Surface((data[0], data[1]))

    def draw(self):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children.values():# Drawing Objects
            self.canvas.blit(child.image, child.motion)
