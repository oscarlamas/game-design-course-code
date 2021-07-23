import random, pygame, sys
import time
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

# Define Colors
# Name = (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BLUE = (0, 0, 255)
BGCOLOR = BLACK

# KEY INPUT = worm direction
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # The index of the worm's head
HEAD2 = 0

def main():
    global FPSCLOCK, TIMER, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    #Spawn at a random starting point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)

    startx_2 = random.randint(5, CELLWIDTH - 6)
    starty_2 = random.randint(5, CELLHEIGHT - 6)

    direction = RIGHT #CALLOUT
    direction2 = RIGHT
    wormCoords = [{'x': startx, 'y': starty},
                 {'x': startx - 1, 'y': starty},
                 {'x': startx - 2, 'y': starty}]

    wormCoords_two = [{'x': startx_2, 'y': starty_2},
                 {'x': startx_2 - 1, 'y': starty_2},
                 {'x': startx_2 - 2, 'y': starty_2}]

    apple = getRandomLocation()
    apple2 = getRandomLocation()

    #Game loop (while)
    while True:

        #Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
                elif (event.key == K_a) and direction2 != RIGHT:
                    direction2 = LEFT
                elif (event.key == K_d) and direction2 != LEFT:
                    direction2 = RIGHT
                elif (event.key == K_w) and direction2 != DOWN:
                    direction2 = UP
                elif (event.key == K_s) and direction2 != UP:
                    direction2 = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        #Detect "collisions"
        #check to see if the worm has hit itself or a wall

        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return
        for wormSegment in wormCoords[3:]:
            if wormSegment['x'] == wormCoords[HEAD]['x'] and wormSegment['y'] == wormCoords[HEAD]['y']:
                return
        #collisions for second worm
        if wormCoords_two[HEAD2]['x'] == -1 or wormCoords_two[HEAD2]['y'] == -1 or wormCoords_two[HEAD2]['x'] == CELLWIDTH or wormCoords_two[HEAD2]['y'] == CELLHEIGHT:
            return
        for wormSegment_2 in wormCoords_two[3:]:
            if wormSegment_2['x'] == wormCoords_two[HEAD2]['x'] and wormSegment_2['y'] == wormCoords_two[HEAD2]['y']:
                return

        #check to see if the worm has eaten the apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()
        else:
            del wormCoords[-1]

        if wormCoords_two[HEAD2]['x'] == apple2['x'] and wormCoords_two[HEAD2]['y'] == apple2['y']:
            apple2 = getRandomLocation()
        else:
            del wormCoords_two[-1]

        #move the worm
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}

        if direction2 == UP:
            newHead2 = {'x': wormCoords_two[HEAD2]['x'], 'y': wormCoords_two[HEAD2]['y'] - 1}
        elif direction2 == DOWN:
            newHead2 = {'x': wormCoords_two[HEAD2]['x'], 'y': wormCoords_two[HEAD2]['y'] + 1}
        elif direction2 == LEFT:
            newHead2 = {'x': wormCoords_two[HEAD2]['x'] - 1, 'y': wormCoords_two[HEAD2]['y']}
        elif direction2 == RIGHT:
            newHead2 = {'x': wormCoords_two[HEAD2]['x'] + 1, 'y': wormCoords_two[HEAD2]['y']}

        wormCoords.insert(0, newHead)
        wormCoords_two.insert(0, newHead2)

    # LAST THING WE DO
    # Paint on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawWorm2(wormCoords_two) # coords defined later
        drawApple(apple)
        drawApple2(apple2)
        drawScore(len(wormCoords) - 3)
        drawScore2(len(wormCoords_two) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0), (x,WINDOWHEIGHT))
    for y in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def drawWorm(wormCoords):
    #code for worm 1
    for segment in wormCoords:
        x = segment['x'] * CELLSIZE
        y = segment['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, BLUE, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x+4, y+4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)

#code for worm 2
def drawWorm2(wormCoords_two):
    for segment_2 in wormCoords_two:
        x2 = segment_2['x'] * CELLSIZE
        y2 = segment_2['y'] * CELLSIZE
        wormSegment_2Rect = pygame.Rect(x2, y2, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormSegment_2Rect)
        wormInnerSegment_2Rect = pygame.Rect(x2+4, y2+4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegment_2Rect)
    

def drawApple(apple):
    x = apple['x'] * CELLSIZE
    y = apple['y'] * CELLSIZE
    appleSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleSegmentRect)

def drawApple2(apple2):
    x2 = apple2['x'] * CELLSIZE
    y2 = apple2['y'] * CELLSIZE
    appleSegmentRect = pygame.Rect(x2, y2, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, GREEN, appleSegmentRect)

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawScore2(score2):
    scoreSurf = BASICFONT.render('Score: %s' % (score2), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (10, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def terminate():
    pygame.quit()
    sys.exit()

def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2, 10)
    overRect.midtop = (WINDOWWIDTH/2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)

    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while(True):
        if checkForKeyPress():
            pygame.event.get()
            return # clear the event cache

def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            else:
                return True
    return False

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, BLUE)
    titleSurf2 = titleFont.render('Wormy!', True, RED)
    
    degrees1 = 0
    degrees2 = 0
    while(True): #looks like a game loop
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get() #clear the event cache
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

if __name__ == '__main__':
    main()