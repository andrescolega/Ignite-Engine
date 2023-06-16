# Importing modules
import pygame, sys
from pygame import *
window = pygame.display# Making alias "window" for "display"
pygame.init()# Initializing Pygame

# Color Pallete
black = 0,0,0

# Physics classes
class Body():
    def __init__(self, name, image):
        # Setting variables
        self.name = name
        self.image = pygame.image.load(image)
        # Setting physics
        self.speed = [0,0]
        self.collider = self.image.get_rect()

    def move(self):
        self.collider.move(self.speed)

# UI classes
class Screen():
    def __init__(self, name, size):# Creating Screen
        # Setting sariables
        self.name = name
        self.size = size
        # Initializing Screen
        self.canvas = window.set_mode(self.size)
        window.set_caption(self.name)

    def is_closed(self):# Killing program
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, objects):# Drawing Objects
        # Erasing Canvas
        self.canvas.fill(black)
        # Drawing Objects
        for object in objects:
            self.canvas.blit(object.image, object.collider)
        # Displaying Canvas
        window.flip()

class Macro():
    def __init__(self, name, key):# Creating key macro
        # Setting Variables
        self.name = name
        self.key = self.alias[key]

    alias = {
    # Letters keys
    'a':pygame.K_a,
    'b':pygame.K_b,
    'c':pygame.K_c,
    'd':pygame.K_d,
    'e':pygame.K_e,
    'f':pygame.K_f,
    'g':pygame.K_g,
    'h':pygame.K_h,
    'i':pygame.K_i,
    'j':pygame.K_j,
    'k':pygame.K_k,
    'l':pygame.K_l,
    'm':pygame.K_m,
    'n':pygame.K_n,
    'o':pygame.K_o,
    'p':pygame.K_p,
    'q':pygame.K_q,
    'r':pygame.K_r,
    's':pygame.K_s,
    't':pygame.K_t,
    'u':pygame.K_u,
    'v':pygame.K_v,
    'w':pygame.K_w,
    'x':pygame.K_x,
    'y':pygame.K_y,
    'z':pygame.K_z,
    # Numbers keys
    '1':pygame.K_1,
    '2':pygame.K_2,
    '3':pygame.K_3,
    '4':pygame.K_4,
    '5':pygame.K_5,
    '6':pygame.K_6,
    '7':pygame.K_7,
    '8':pygame.K_8,
    '9':pygame.K_9,
    '0':pygame.K_0,
    # Special characters keys
    '\q':pygame.K_QUOTE,
    '\dq':pygame.K_QUOTEDBL,
    '\c':pygame.K_COMMA,
    '!':pygame.K_EXCLAIM,
    '?':pygame.K_QUESTION,
    '&':pygame.K_AMPERSAND,
    '(':pygame.K_LEFTPAREN,
    ')':pygame.K_RIGHTPAREN,
    '*':pygame.K_ASTERISK,
    '#':pygame.K_HASH,
    '^':pygame.K_CARET,
    '`':pygame.K_BACKQUOTE,
    ':':pygame.K_COLON,
    ';':pygame.K_SEMICOLON,
    '.':pygame.K_PERIOD,
    '<':pygame.K_LESS,
    '>':pygame.K_GREATER,
    '/':pygame.K_SLASH,
    '\\':pygame.K_BACKSLASH,
    '-':pygame.K_MINUS,
    '_':pygame.K_UNDERSCORE,
    '+':pygame.K_PLUS,
    '=':pygame.K_EQUALS,
    '[':pygame.K_LEFTBRACKET,
    ']':pygame.K_RIGHTBRACKET,
    # Special keys
    '\b':pygame.K_BACKSPACE,
    '\t':pygame.K_TAB,
    '\r':pygame.K_RETURN,
    '\e':pygame.K_ESCAPE,
    '\s':pygame.K_SPACE,
    '\d':pygame.K_DELETE,
    '\p':pygame.K_PAUSE,
    '\i':pygame.K_INSERT,
    '\pu':pygame.K_PAGEUP,
    '\pd':pygame.K_PAGEDOWN,
    '\h':pygame.K_HOME,
    '\f':pygame.K_END,
    '\nl':pygame.K_NUMLOCK,
    '\cl':pygame.K_CAPSLOCK,
    '\sl':pygame.K_SCROLLOCK,
    '\rs':pygame.K_RSHIFT,
    '\ls':pygame.K_LSHIFT,
    '\rc':pygame.K_RCTRL,
    '\lc':pygame.K_LCTRL,
    '\ra':pygame.K_RALT,
    '\la':pygame.K_LALT,
    '\rw':pygame.K_RSUPER,
    '\lw':pygame.K_LSUPER,
    '\pr':pygame.K_PRINT,
    '\sr':pygame.K_SYSREQ,
    '\br':pygame.K_BREAK,
    '\sd':pygame.K_POWER,
    'up':pygame.K_UP,
    'down':pygame.K_DOWN,
    'right':pygame.K_RIGHT,
    'left':pygame.K_LEFT,
    # Functions keys
    'f1':pygame.K_F1,
    'f2':pygame.K_F2,
    'f3':pygame.K_F3,
    'f4':pygame.K_F4,
    'f5':pygame.K_F5,
    'f6':pygame.K_F6,
    'f7':pygame.K_F7,
    'f8':pygame.K_F8,
    'f9':pygame.K_F9,
    'f10':pygame.K_F10,
    'f11':pygame.K_F11,
    'f12':pygame.K_F12,
    }
