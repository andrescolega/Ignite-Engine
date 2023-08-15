#=============================== Ignite Engine =================================
"""-----------------THIS CODE IS UNDER THE GNU v3.0 LICENSE------------------"""

# Importing Modules-------------------------------------------------------------
import pygame, sys, os
from pygame import *
pygame.init()

# Color Pallete-----------------------------------------------------------------
black = 0,0,0

# Aliases-----------------------------------------------------------------------
error = 'something went wrong..'
window = pygame.display
sprite = pygame.sprite.Sprite

# Node Class--------------------------------------------------------------------
class Node:

    def __init__(self, name, script=None):
        self.name = name
        self.parent = None
        self.children = []
        self.script = script

    def __repr__(self):
        return f'<{self.name} -> children({len(self.children)})>'

    def add(self, node):# Add Child Node
        node.parent = self
        self.children.append(node)
        return node

    def update(self):
        for child in self.children:
            child.update()
        if self.script != None:self.script(self)

# Button Node-------------------------------------------------------------------
'''This node execute a function an specific key event happens'''

class physicButton(Node):
    def __init__(self, button, script=None):
        super().__init__(self.__class__.__name__, script)
        self.combo = button.split('+')
        self.keys = []
        for key in self.combo:
            self.keys.append(self.alias[key])
        self.isPressed = False

    def __call__(self):
        return self.isPressed

    def update(self):
        event = pygame.key.get_pressed()
        keysCheck = []
        for key in self.keys:
            if event[key]:keysCheck.append(key)
        if keysCheck == self.keys:
            self.isPressed = True
            if self.script != None:self.script(self)
        else: self.isPressed = False

    alias = {
# Letters keys------------------------------------------------------------------
    'a':pygame.K_a,'b':pygame.K_b,'c':pygame.K_c,'d':pygame.K_d,'e':pygame.K_e,
    'f':pygame.K_f,'g':pygame.K_g,'h':pygame.K_h,'i':pygame.K_i,'j':pygame.K_j,
    'k':pygame.K_k,'l':pygame.K_l,'m':pygame.K_m,'n':pygame.K_n,'o':pygame.K_o,
    'p':pygame.K_p,'q':pygame.K_q,'r':pygame.K_r,'s':pygame.K_s,'t':pygame.K_t,
    'u':pygame.K_u,'v':pygame.K_v,'w':pygame.K_w,'x':pygame.K_x,'y':pygame.K_y,
    'z':pygame.K_z,
# Numbers keys------------------------------------------------------------------
    '1':pygame.K_1,'2':pygame.K_2,'3':pygame.K_3,'4':pygame.K_4,'5':pygame.K_5,
    '6':pygame.K_6,'7':pygame.K_7,'8':pygame.K_8,'9':pygame.K_9,'0':pygame.K_0,
# Special keys------------------------------------------------------------------
    'quote':pygame.K_QUOTE,'dquote':pygame.K_QUOTEDBL,',':pygame.K_COMMA,
    '!':pygame.K_EXCLAIM,'?':pygame.K_QUESTION,'&':pygame.K_AMPERSAND,
    '(':pygame.K_LEFTPAREN,')':pygame.K_RIGHTPAREN,'*':pygame.K_ASTERISK,
    '#':pygame.K_HASH,'^':pygame.K_CARET,'`':pygame.K_BACKQUOTE,
    ':':pygame.K_COLON,';':pygame.K_SEMICOLON,'.':pygame.K_PERIOD,
    '<':pygame.K_LESS,'>':pygame.K_GREATER,'/':pygame.K_SLASH,
    'b/':pygame.K_BACKSLASH,'-':pygame.K_MINUS,'_':pygame.K_UNDERSCORE,
    '+':pygame.K_PLUS,'=':pygame.K_EQUALS,'[':pygame.K_LEFTBRACKET,
    ']':pygame.K_RIGHTBRACKET,
# Action keys------------------------------------------------------------------
    'backspace':pygame.K_BACKSPACE,'tab':pygame.K_TAB,'return':pygame.K_RETURN,
    'escape':pygame.K_ESCAPE,'space':pygame.K_SPACE,'delete':pygame.K_DELETE,
    'pause':pygame.K_PAUSE,'insert':pygame.K_INSERT,'pageup':pygame.K_PAGEUP,
    'pagedown':pygame.K_PAGEDOWN,'home':pygame.K_HOME,'end':pygame.K_END,
    'numlock':pygame.K_NUMLOCK,'capslock':pygame.K_CAPSLOCK,
    'scrollock':pygame.K_SCROLLOCK,'rshift':pygame.K_RSHIFT,
    'lshift':pygame.K_LSHIFT,'rcontrol':pygame.K_RCTRL,'lcontrol':pygame.K_LCTRL,
    'ralt':pygame.K_RALT,'lalt':pygame.K_LALT,'rsuper':pygame.K_RSUPER,
    'lsuper':pygame.K_LSUPER,'print':pygame.K_PRINT,'sysreq':pygame.K_SYSREQ,
    'break':pygame.K_BREAK,'power':pygame.K_POWER,'up':pygame.K_UP,
    'down':pygame.K_DOWN,'right':pygame.K_RIGHT,'left':pygame.K_LEFT,
# Functions keys----------------------------------------------------------------
    'f1':pygame.K_F1,'f2':pygame.K_F2,'f3':pygame.K_F3,'f4':pygame.K_F4,
    'f5':pygame.K_F5,'f6':pygame.K_F6,'f7':pygame.K_F7,'f8':pygame.K_F8,
    'f9':pygame.K_F9,'f10':pygame.K_F10,'f11':pygame.K_F11,'f12':pygame.K_F12,
    }

# Sprite2D Node-----------------------------------------------------------------
'''This node manages images and animations'''

class Sprite2D(Node):
    def __init__(self, images, script=None):
        super().__init__(self.__class__.__name__, script)
        self.frames = []
        self.load_images(images)
        self.currentFrame = self.frames[0]


    def load_images(self, images):
        for image in images:
            self.frames.append(pygame.image.load(image))

    def update(self):
        super().update()
        self.set_parent_image()

    def set_parent_image(self):
        self.parent.image = self.currentFrame
        self.parent.imageSize = self.currentFrame.get_rect()[2], self.currentFrame.get_rect()[3]
# Body2D Node-------------------------------------------------------------------
'''Kinematic object for 2D enviroments'''

class Body2D(Node):

    def __init__(self, script=None):
        super().__init__(self.__class__.__name__, script)
        self.Xspeed = 0
        self.Yspeed = 0
        self.position = (0,0)
        self.collisionBoxpadding = 0
        self.isColliding = False
        self.bodyColliding = None
        self.isSolid = False
        self.motion_init()

    def motion_init(self):# Defines collisionBox and motion variables (also called when there is no sprite)
        self.collisionBox = pygame.Rect((self.position),(1,1))
        self.motion = self.collisionBox.move((self.Xspeed, self.Yspeed))
        self.position = self.motion[0], self.motion[1]

    def update(self):
        super().update()
        self.apply_collision()
        self.apply_speed()

    def apply_speed(self):# Update position and collisionBox variables
        try:
            self.collisionBox = pygame.Rect((self.position), (self.imageSize))
            self.motion = self.collisionBox.move((self.Xspeed, self.Yspeed))
            self.position = self.motion[0], self.motion[1]
        except (AttributeError):
            self.motion_init()

    def apply_collision(self):
        if self.bodyColliding != None and self.isColliding:
            # X speed stopping
            if self.collisionBox.right >= self.bodyColliding.position[0]: # Moving Right
                self.Xspeed -= self.Xspeed
            if self.collisionBox.left <= self.bodyColliding.collisionBox.right: # Moving Left
                self.Xspeed += self.Xspeed*-1
            # Y speed stopping
            if self.collisionBox.top <= self.bodyColliding.collisionBox.bottom: # Moving Up
                self.Yspeed += self.Yspeed*-1
            if self.collisionBox.bottom >= self.bodyColliding.collisionBox.top: # Moving down
                self.Yspeed -= self.Yspeed
                print('a')

# Scene2D Node------------------------------------------------------------------
'''This node manages other 2D objects in a single stage'''

class Scene2D(Node):
    def __init__(self, size, script=None):
        super().__init__(self.__class__.__name__, script)
        self.canvas = pygame.Surface(size)
        self.position = self.canvas.get_rect()
        self.current = False

    def update(self):
        super().update()
        self.check_current()
        self.check_collision()
        self.draw()

    def check_current(self):# Check if self is tagged as the current scene
        if self.current == True:
            self.parent.currentScene = self

    def check_collision(self):# Check for collisions between children
        for childA in self.children:
            for childB in self.children:
                try:
                    if childA != childB:
                        xoffset = childA.collisionBox[0] - childB.collisionBox[0]
                        yoffset = childA.collisionBox[1] - childB.collisionBox[1]
                        leftmask = pygame.mask.from_surface(childA.image)
                        rightmask = pygame.mask.from_surface(childB.image)
                        check = leftmask.overlap(rightmask, (xoffset, yoffset))
                        print(check)
                        #check = pygame.Rect.colliderect(childA.collisionBox, childB.collisionBox)
                        childA.isColliding = check
                        if check == True and childB.isSolid == True:
                            childA.bodyColliding = childB
                        else:
                            childA.bodyColliding = None
                except (AttributeError): pass

    def draw(self):
        self.canvas.fill(black)# Erasing Canvas

        for child in self.children:# Drawing Objects
            try:self.canvas.blit(child.image, child.motion)
            except (AttributeError): pass

# Root Node---------------------------------------------------------------------
"""
This is the 'root' node. It is the object that letter is exported as the 'game'.
It is the reponsible of managing every other node.
"""

class Root2D(Node):

    def __init__(self, name, size, script=None):
        super().__init__(name, script)
        self.size = size
        self.running = True
        self.currentScene = None

    def __call__(self):# Run the game
        self.window_init()
        self.process()

# Main functions----------------------------------------------------------------

    def window_init(self):#Create 'canvas' variable.
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

    def process(self):# Main game loop.
        while self.running:

            self.check_events()
            super().update()
            self.draw()

        self.kill_process()

# Checking Events---------------------------------------------------------------
    def check_events(self):
        for event in pygame.event.get():# Check 'QUIT' event.
            if event.type == QUIT:
                self.running = False

# Drawing-----------------------------------------------------------------------
    def draw(self):# Draw children
        self.canvas.fill(black)# Erasing canvas
        if self.currentScene != None:
            self.canvas.blit(self.currentScene.canvas, self.currentScene.position)
            window.flip()# Displaying Canvas
# Closing Program---------------------------------------------------------------
    def kill_process(self):# Securely close program
        pygame.quit()
        sys.exit()
