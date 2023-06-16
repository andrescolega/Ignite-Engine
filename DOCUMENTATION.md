# Installing & Initializing

Supposing that you have the required dependencies (README.md), you need to download the  'ignite_engine.py' file, and 'import' the module. That's all!

I highly recommend to import the module with a shorter name, for faster development, in this case i going to use the 'IE' alias.

# Body & Physics

I made the class 'Body' to contain useful methods for physics handling. A body can be anything: a player, an object, etc.:

- INIT(); The constructor method for 'Body', it requires an image. SYNTAX: 'name = IE.Body('image')'

- MOVE(); This method updates the 'motion' variable of the 'Body'. The 'motion' is modified by the 'speed' variable. SYNTAX: 'name.move()' 'name.speed[axis]'

# User Interface

The 'Screen' class is the required to initialize a window.:

- INIT(); The constructor method for 'Screen', it requires a title and the width and height of the window. SYNTAX: 'name = IE.Screen(title, (width,height))'

- DRAW(); This method draws every object in the given list. SYNTAX: 'name.draw([object1, object2, object3, ...])'

- IS_CLOSED(); This method checks if the window is begin closed. SYNTAX: 'name.is_closed()'

The class 'Macro' is simple, it checks the events for a given button.

- INIT(); The constructor method for 'Macro', it requires the button for monitoring. SYNTAX: 'name = IE.Macro('button')'

- IS_PRESSED(); It returns a boolean if the button is pressed. SYNTAX: 'name.is_pressed()'
