#!/usr/bin/python2
#Memory puzzle 
#By Al Sweight al
import pygame, sys, random
from pygame.locals import *

FPS = 30
windowwidth = 640 
windowheight = 480
revealspeed = 40
gapsize = 10

boardwidth = 10
boardweight = 7
assert( boardwidth * boardweight) % 2 == 0,'Board needs to have an even number of boxes for pairs of matches'
xmargin = int((windowwidth - (boardwidth * (boxsize + gapsize)))/2)
ymargin = int((windoweight - (boardeight * (boxsize + gapsize)))/2)

GRAY = (100,100,100)
NAVYBLUE = (60,60,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)

BGCOLOR = NAVYBLUE 
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'

