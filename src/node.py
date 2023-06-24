# Importing modules-------------------------------------------------------------
import pygame
from pygame import *
pygame.init()

# Master Node-------------------------------------------------------------------
class Node:

    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = {}

# Adding/Deleting Children------------------------------------------------------
    def add_child(self, types, name, node, data):
        node = types[node]
        self.children[name] = node(self, name, data)
