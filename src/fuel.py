# Master Node-------------------------------------------------------------------
class Node:

    def __init__(self, name):
        self.name = name
        self.children = {}

# Adding/Deleting Children------------------------------------------------------
    def add_child(self, name, node):
        node = node_types[node]
        self.children[name] = node(name)
        pass
