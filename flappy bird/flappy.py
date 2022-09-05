import random     #for generating random nos
import sys                       #use sys.exit to exit the program
import pygame
import pygame.locals import *            #basic pygame imports

#global variables for the game
FPS =32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN =pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))        #forms screen
GROUNDY = SCREENHEIGHT*0.8             #BASE - 80% of ground height
GAME_IMAGES ={}
GAME_SOUNDS={}
PLAYER = '/gallery/images/bird1.png'
BACKGROUND='/gallery/images/bg3.png'
PIPE='/gallery/images/pipe.png'

if __name__ =='__main__':
    #from here game will start
    pygame.init()       #initialises all modules of pygame
    FPSCLOCK = pygame.time.Clock()  #for controllling game fps
    pygame.display.set_caption("Flappy Bird by me")
    GAME_IMAGES['numbers']=(
        # convert_alpha is used for game optimisation...changes pixels +alpha of images
    pygame.image.load('gallery/images/0.jpg').convert_alpha(),
    pygame.image.load('gallery/images/1.jpg').convert_alpha(),
    pygame.image.load('gallery/images/2.jpg').convert_alpha(),
    pygame.image.load('gallery/images/3.jpg').convert_alpha(),
    pygame.image.load('gallery/images/4.jpg').convert_alpha(),
    pygame.image.load('gallery/images/5.jpg').convert_alpha(),
    pygame.image.load('gallery/images/6.jpg').convert_alpha(),
    pygame.image.load('gallery/images/7.jpg').convert_alpha(),
    pygame.image.load('gallery/images/8.jpg').convert_alpha(),
    pygame.image.load('gallery/images/9.jpg').convert_alpha()
    )
    GAME_IMAGES['message'] = pygame.image.load('gallery/images/msg.jpg').convert_alpha()
    