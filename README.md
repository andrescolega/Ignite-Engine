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

The Engine is build upon a hierarchical node model, and it is divided in 4 ranks.

A node of rank 2 only its compatible with a node of rank 1.
A node of rank 3 only its compatible with a node of rank 2.
A node of rank 4 only its compatible with a node of rank 3

Unranked nodes doesn't fall in any of this rules.

Knowing this, the road map is to develop each rank hierarchically.
