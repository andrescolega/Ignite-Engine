# Importing modules-------------------------------------------------------------
import pygame, node
from pygame import *
pygame.init()

# Body Node---------------------------------------------------------------------
class Body(node.Node):

    def __init__(self, parent, name, data):
        super().__init__(parent, name)
        self.image = pygame.image.load(data[0])
        self.speed = [0,0]
        self.collider = self.image.get_rect()
        self.motion = self.collider.move(self.speed)
