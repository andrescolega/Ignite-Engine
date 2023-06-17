import pygame
from pygame import *
pygame.init()

class body():
    def __init__(self, image):# Creating target
        # Setting variables
        self.image = pygame.image.load(image)
        # Setting physics
        self.speed = [0,0]
        self.collider = self.image.get_rect()
        self.collider_list = []

    def move(self):
        self.motion = self.collider.move(self.speed)
