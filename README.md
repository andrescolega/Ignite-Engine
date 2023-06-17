# Ignite-Engine
Game engine powered by the Pygame library.

It's meant to be a simple and qualified tool for developing games in Python, using "Pygame" that is a "Python extension library
that wraps the SDL library and its helpers."

# Creator Message
This game engine was not meant for distribution purposes, it is just a personal project, so, if you find this repo'
searching for a high level game engine, you should seek somewhere else.

In other hand, if you have come just for curiosity, please feel free to contribute and share your opinion about my work.

# Dependencies
As said in the description; "Ignite" uses the Pygame library to work, that's why requires the next dependencies (for the moment):

- Python3
- Pygame Library

# Development Road-Map
I got confused about what is exactly a game engine, so i started to research more about the structure and components of them. I realized i was driving on the wrong way, and now there are many changes to do:

                               Main  
                                |
       ___________________ node_handler_________________
       |                 |             |               |
    Physics            Audio        Sprites         Interface

                           'Main' Loop
                                 |
      Update Nodes ----> Apply Physics ----> Render Images

Having this basic understanding, we can say: the Pygame (as a SDL wrapper) already does a huge part of the work, so i need to focus on developing the node system. For now i have a basic understanding about node developing, because of my experience with the Godot engine.

I really don't like this kind of radical changes, but i think this helped me to have a better understanding of what im doing, knowing this is a personal project to 'learn'.
