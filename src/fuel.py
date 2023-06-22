# Importing modules-------------------------------------------------------------
import pygame
from pygame import *
pygame.init()

# Master Node-------------------------------------------------------------------
class Node:

    def __init__(self, name):
        self.name = name
        self.children = {}

# Adding/Deleting Children------------------------------------------------------
    def add_child(self, types, name, node, data):
        node = types[node]
        self.children[name] = node(name, data)

# Surface/Level Node------------------------------------------------------------
class Level(Node):
    def __init__(self, name, data):
        super().__init__(name)
        self.canvas = pygame.Surface((data[0], data[1]))

    def draw(self, image, motion):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children.values():# Drawing Objects
            self.canvas.blit(child.image, child.motion)
