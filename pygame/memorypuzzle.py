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
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAAL = 'oval'

ALLCOLORS = (RED, GREEN, WHITE, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,'Board is too big for the numbers/shapes defined'

def main():
    global FPSCLOCK, DISPLAYSUR
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSUR = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')
    
    mainBoard = getRanddomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    DISPLAYSUR.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:#main game loop 
        mouseClicked = False

        DISPLAYSUR.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():#event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex,mousey)
        if boxx != None and boxy != None:
#the mouse is in the box
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx,boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxAnimation(mainBoard, [(boxx,boxy)])
                revealBoxes[boxx,boxy] = True #set the box as revealed

            if firstSelection == None:
                firstSelection = (boxx,boxy)
            else:
                #check if the two boxes are matched
                icon1shape, icon1color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                icon2shape, icon2color = getShapeAndColor(mainBoard, mousex, mousey)
                
                if icon1shape != icon2shape or icon1color != icon2color:
#icon does not match each other
                    pygame.time.wait(1000)#1000 millisecond = 1sec
                    coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                    revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                    revealedBoxes[boxx][boxy] = False
                elif hasWon(revealedBoxes):
                    gameWonAnimation(mainBoard)
                    pygame.time.wait(2000)
                #reset the main board
                    mainBoard = getRandomizedBoard()
                    revealedBoxes = generateRevealBoxesData(False)

                    drawBoard(mainBoard, revealedBoxes)
                    pygame.display.update()
                    pygame.time.wait(1000)

                    startGameAnimation(mainBoard)
                firstSelection = None

            pygame.display.update()
            FPSCLOCK.tick(FPS)


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
        return revealedBoxes

def getRandomizedBoard():

    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))

    random.shuffle(icons)
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2 )
    icons  = icons[:numIconsUsed] * 2
    random.shuffle(icons)

    board = []
    for x in range(BOARDHEIGHT):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def splitIntoGroupOf(groupSize, theList):

    result = []
    for i in range(0,len(theList),groupSize):
        result.append(theList[i:i + groupSized])
    return result

def leftTopCoordsOfBox(boxx,boxy):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top  = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left,top)

def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return(boxx, boxy)
    return(None, None)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.25)
    
    left, top = lefTopCoordsOfBox(boxx,boxy)

    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half),half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter -5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND :
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top),(left + BOXSIZE - 1,top + half)))
    elif shape == LINES:
        for  i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i,top + BOXSIZE-1),(left + BOXSIZE -1,top + 1))
    elif shape == OVAL:
            pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))
def getShapeAndColor(board, boxx, boxy):

    return boardp[boxx][boxy][0], board[boxx][boxy][1]

def drawBoxCovers(board, boxes, coverage):
    for box in boxes:

