import math
import pygame
import sys
from pygame.locals import *

screenwidth = 450
screenheight = 600
setfps = 30

pygame.init()
Display = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Throw Grenade")

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

#angle from positive x axis
angle = 0

#The Rect
RectSurf = pygame.Surface((50,25))
RectSurf.set_colorkey(GREY)
RectSurf.fill(RED)

RectRect = RectSurf.get_rect()
RectRect.center =(screenwidth/2, screenheight/2)



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

    old_center = RectRect.center

    #angle
    if (abs(mousepos[0] - screenwidth/2) != 0):
        angle = math.atan2(abs(mousepos[1] - screenheight/2) , abs(mousepos[0] - screenwidth/2))
        #print("Angle (rad): ",angle)
        #print("Angle (degree): ",angle/math.pi*180)

        #2nd quad and 4th quad
        if ((mousepos[0] < screenwidth/2 and mousepos[1] < screenheight/2) or (mousepos[0] > screenwidth/2 and mousepos[1] > screenheight/2)):
            angle = math.pi - math.atan2(abs(mousepos[1] - screenheight/2) , abs(mousepos[0] - screenwidth/2))

    else:#90 degree and 270 degree
        angle = math.pi/2 #or 2*math.pi/4*3
    newImage = pygame.transform.rotate(RectSurf,angle/math.pi*180)
    newRect = newImage.get_rect()
    newRect.center = old_center
    Display.blit(newImage,newRect)

    #draw  x-axis
    pygame.draw.line(Display,BLACK,(0, screenheight/2), (screenwidth, screenheight/2), 3)
    #draw y-axis
    pygame.draw.line(Display,BLACK,(screenwidth/2, 0), (screenwidth/2, screenheight), 3)

    #draw the aiming line
    pygame.draw.line(Display,BLUE,(screenwidth/2,screenheight/2),mousepos,3)

    
    pygame.display.update()
    pygame.time.Clock().tick(setfps);#fps
    
