# Ignite-Engine
Game engine powered by the Pygame-CE library.

It's meant to be a simple and qualified tool for developing games in Python,
using "Pygame-CE" that is a "Python extension library that wraps the SDL library
and its helpers."

The main purpose is to simplify the scripting, so anyone can develop MORE with
LESS. You can try the 'hello world':

```
import ignite

game = ignite.Root('My Own Game', 300, 300)
level = game.add(ignite.Scene2D, [game.size])
level.current = True
player = level.add(ignite.Body2D, ['image.png'])

if __name__ == "__main__":
    game()
```

# Creator Message
This game engine was not meant for distribution purposes, it is just a personal
project for learning, so, if you find this repo' searching for a high level game
engine, you should seek somewhere else.

In other hand, if you have come just for curiosity, please feel free to
contribute and share your opinion about my work.

# Dependencies
As said in the description; "Ignite" uses the Pygame-CE library to work, that's
why requires the next dependencies (for the moment):

- Python3
- Pygame-CE Library

# Development Road-Map

The Engine is build upon a hierarchical* node model, and it is divided in 4 ranks:

ROOT: It is the main node, and responsible of handling every other node and the
main loop.

SCENE: This node handles the 'objects' that are displayed upon it's surface.

OBJECT: Players, enemies, items, boxes... all are objects.

MODIFIER: This nodes contains the 'rules' that  'object' nodes should follow and
modify how they behave: Gravity, Controls, Animations.

Knowing this, the road map is to develop each rank hieratically.

#
