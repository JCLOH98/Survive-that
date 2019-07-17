import math
from math import *
import pygame
import sys
from pygame.locals import *

screenwidth = 450
screenheight = 600
setfps = 30

pygame.init()
Display = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Shoot some bullets")

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

#The Gun Rect
RectSurf = pygame.Surface((50,30))
RectSurf.set_colorkey(GREY)
RectSurf.fill(RED)

screencenter = (screenwidth/2, screenheight/2)

#The Bullet Rect
BulletSurf = pygame.Surface((50,20))
BulletSurf.set_colorkey(GREY)
BulletSurf.fill(BLACK)

#angle
angle = 0

#the moment when the bullet is shoot
themousepos = ()
theplayercenter = (screenwidth/2, screenheight/2)
theangle = 0
xspeed = 0
yspeed = 0
thespeed = 20

#shoot
shoot = False

#bullet amount
bulletnum = 3
anglelist = []
mouseposlist = []
xspeedlist = []
yspeedlist = []

while True:
    Display.fill(GREY)

    #mouse position
    mousepos = pygame.mouse.get_pos()

    #rect for rotation
    #angle
    if (abs(mousepos[0] - screenwidth/2) != 0):
        #1st quad
        if (mousepos[0] > theplayercenter[0] and mousepos[1] < theplayercenter[1]):
            angle = math.atan2(abs(mousepos[1] - screenheight/2) , abs(mousepos[0] - screenwidth/2))
        #2nd quad
        if (mousepos[0] < theplayercenter[0] and mousepos[1] < theplayercenter[1]):
            angle = math.pi - math.atan2(abs(mousepos[1] - screenheight/2) , abs(mousepos[0] - screenwidth/2))
        #3rd quad
        if (mousepos[0] < theplayercenter[0] and mousepos[1] > theplayercenter[1]):
            angle = math.pi  + math.atan2(abs(mousepos[1] - screenheight/2) , abs(mousepos[0] - screenwidth/2))
        #4th quad
        if (mousepos[0] > theplayercenter[0] and mousepos[1] > theplayercenter[1]):
            angle = 2*math.pi - math.atan2(abs(mousepos[1] - screenheight/2) , abs(mousepos[0] - screenwidth/2))
        
    else:
        #90 degree
        if (mousepos[1] < theplayercenter[1]):
            angle = math.pi/2
        #270 degree
        if (mousepos[1] > theplayercenter[1]):
            angle = 2*math.pi - math.pi/2

    #print("Angle (degree): ",angle/math.pi*180)

    #player settings
    newImage = pygame.transform.rotate(RectSurf,angle/math.pi*180)
    newRect = newImage.get_rect()
    newRect.center = screencenter
    
    
    for event in pygame.event.get():        
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == LEFT_CLICK and shoot == False:
                    print("shoot bullet")
                    themousepos = mousepos
                    theplayercenter = screencenter
                    theangle = angle
                    
                    shoot = True
                    #A,S,T,C
                    #1st quad
                    if (themousepos[0] > theplayercenter[0] and themousepos[1] < theplayercenter[1]):
                        xspeed = thespeed * cos(theangle) #+ve speed
                        yspeed = -thespeed * sin(theangle) #-ve speed
                        print(1)
                    #2nd quad
                    if (themousepos[0] < theplayercenter[0] and themousepos[1] < theplayercenter[1]):
                        xspeed = thespeed * cos(theangle) #-ve speed
                        yspeed = -thespeed * sin(theangle) #-ve speed
                        print(2)
                    #3rd quad
                    if (themousepos[0] < theplayercenter[0] and themousepos[1] > theplayercenter[1]):
                        xspeed = thespeed * cos(theangle) #-ve speed
                        yspeed = -thespeed * sin(theangle) #+ve speed
                        print(3)
                    #4th quad
                    if (themousepos[0] > theplayercenter[0] and themousepos[1] > theplayercenter[1]):
                        xspeed = thespeed * cos(theangle) #+ve speed
                        yspeed = -thespeed * sin(theangle) #+ve speed
                        print(4)

                    #on x-axis
                    if (themousepos[1] ==  theplayercenter[1]):
                        if (themousepos[0] > theplayercenter[0]):
                            xspeed = thespeed
                            yspeed = 0
                            #print("right side")
                        elif (themousepos[0] < theplayercenter[0]):
                            xspeed = -thespeed
                            yspeed = 0
                            #print("left side")
                    #on y-axis
                    if (themousepos[0] == theplayercenter[0]):
                        if (themousepos[1] < theplayercenter[1]):
                            yspeed = -thespeed
                            xspeed = 0
                            #print("up side")
                        elif (themousepos[1] > theplayercenter[1]):
                            yspeed = thespeed
                            xspeed = 0
                            #print("down side")
                    
                    
                    #starting position bullet
                    TheBullet = pygame.transform.rotate(BulletSurf,angle/math.pi*180)
                    BulletRect = TheBullet.get_rect()
                    BulletRect.center = screencenter

                    #print("Xspeed: ",xspeed)
                    #print("Yspeed: ",yspeed)

                if pygame.mouse.get_pressed() == RIGHT_CLICK:
                    print("throw grenade")

    #show the player
    Display.blit(newImage,newRect)
    
    #draw  x-axis
    pygame.draw.line(Display,WHITE,(0, screenheight/2), (screenwidth, screenheight/2), 3)
    #draw y-axis
    pygame.draw.line(Display,WHITE,(screenwidth/2, 0), (screenwidth/2, screenheight), 3)

    #draw the aiming line
    pygame.draw.line(Display,BLUE,(screenwidth/2,screenheight/2),mousepos,3)

    #shoot the bullet
    if shoot == True:
        Display.blit(TheBullet,BulletRect)
        BulletRect.centerx += xspeed
        BulletRect.centery += yspeed
        #print("BulletRect.centerx: ",BulletRect.centerx)
        #print("BulletRect.centery: ",BulletRect.centery)
        if (BulletRect.centerx >= screenwidth or BulletRect.centerx < 0 or BulletRect.centery > screenheight or BulletRect.centery < 0):
            shoot = False
    
    
    pygame.display.update()
    pygame.time.Clock().tick(setfps);#fps
    
