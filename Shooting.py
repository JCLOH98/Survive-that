import pygame
import sys
from pygame.locals import *



screenwidth = 450
screenheight = 600
setfps = 30

pygame.init()
Display = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Shooting motion")

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Set Cursor
#pygame.mouse.set_cursor(*pygame.cursors.tri_left)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

#Mouse click
LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

def bullet(mousepos):
    xchange = abs(mousepos[0] - screenwidth/2)
    ychange = abs(mousepos[1] - screenheight/2)
    pass

while True:
    Display.fill(GREY)

    #mouse position
    mousepos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():        
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == LEFT_CLICK:
                    print("shoot bullet")

                if pygame.mouse.get_pressed() == RIGHT_CLICK:
                    print("throw grenade")
    
    pygame.draw.line(Display,BLUE,(screenwidth/2,screenheight/2),mousepos,3)
    pygame.display.update()
    pygame.time.Clock().tick(setfps);#fps
    
