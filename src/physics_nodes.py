# Importing modules-------------------------------------------------------------
import pygame, fuel
from pygame import *
pygame.init()

# Body Node---------------------------------------------------------------------
class Body(fuel.Node):

    def __init__(self, name, data):
        super().__init__(name)
        self.image = pygame.image.load(data[0])
        self.speed = [0,0]
        self.collider = self.image.get_rect()
        self.motion = self.collider.move(self.speed)
