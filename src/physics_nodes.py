# Importing modules-------------------------------------------------------------
import pygame
from pygame import *
import node_handler as nh
pygame.init()

# Body Node---------------------------------------------------------------------
class Body(nh.Node):

    def __init__(self, name, image):
        super().__init__(name)
        self.image = pygame.image.load(image)
        self.speed = [0,0]
        self.collider = self.image.get_rect()
        self.motion = self.collider.move(self.speed)