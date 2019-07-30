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
currentbulletnum = 0 #0 means 1 bullet, 1 means 2 bullet
bulletnum = 4
bulletlist = []
bulletrectlist = []
anglelist = []
mouseposlist = []
xspeedlist = []
yspeedlist = []

while True:
    Display.fill(GREY)

    #mouse position
    mousepos = pygame.mouse.get_pos()

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
                if pygame.mouse.get_pressed() == LEFT_CLICK :#and shoot == False:
                    print("shoot bullet")
                    shoot = True

                    if currentbulletnum < bulletnum:
                        mouseposlist.append(mousepos)
                        theplayercenter = screencenter
                        anglelist.append(angle)
                        #A,S,T,C
                        #1st quad
                        if (mouseposlist[currentbulletnum][0] > theplayercenter[0] and mouseposlist[currentbulletnum][1] < theplayercenter[1]):
                            xspeedlist.append(thespeed * cos(anglelist[currentbulletnum])) #+ve speed
                            yspeedlist.append(-thespeed * sin(anglelist[currentbulletnum])) #-ve speed
                            #print(1)
                        #2nd quad
                        if (mouseposlist[currentbulletnum][0] < theplayercenter[0] and mouseposlist[currentbulletnum][1] < theplayercenter[1]):
                            xspeedlist.append(thespeed * cos(anglelist[currentbulletnum])) #-ve speed
                            yspeedlist.append(-thespeed * sin(anglelist[currentbulletnum])) #-ve speed
                            #print(2)
                        #3rd quad
                        if (mouseposlist[currentbulletnum][0] < theplayercenter[0] and mouseposlist[currentbulletnum][1] > theplayercenter[1]):
                            xspeedlist.append(thespeed * cos(anglelist[currentbulletnum])) #-ve speed
                            yspeedlist.append(-thespeed * sin(anglelist[currentbulletnum])) #+ve speed
                            #print(3)
                        #4th quad
                        if (mouseposlist[currentbulletnum][0] > theplayercenter[0] and mouseposlist[currentbulletnum][1] > theplayercenter[1]):
                            xspeedlist.append(thespeed * cos(anglelist[currentbulletnum])) #+ve speed
                            yspeedlist.append(-thespeed * sin(anglelist[currentbulletnum])) #+ve speed
                            #print(4)

                        #on x-axis
                        if (mouseposlist[currentbulletnum][1] ==  theplayercenter[1]):
                            if (mouseposlist[currentbulletnum][0] > theplayercenter[0]):
                                xspeedlist.append(thespeed)
                                yspeedlist.append(0)
                                print("right side")
                            elif (mouseposlist[currentbulletnum][0] < theplayercenter[0]):
                                xspeedlist.append(-thespeed)
                                yspeedlist.append(0)
                                print("left side")
                        #on y-axis
                        if (mouseposlist[currentbulletnum][0] == theplayercenter[0]):
                            if (mouseposlist[currentbulletnum][1] < theplayercenter[1]):
                                yspeedlist.append(-thespeed)
                                xspeedlist.append(0)
                                #print("up side")
                            elif (mouseposlist[currentbulletnum][1] > theplayercenter[1]):
                                yspeedlist.append(thespeed)
                                xspeedlist.append(0)
                                #print("down side")                    
                    
                    #starting position bullet
                    if currentbulletnum < bulletnum:
                        bulletlist.append(pygame.transform.rotate(BulletSurf,anglelist[currentbulletnum]/math.pi*180))
                        bulletrectlist.append(bulletlist[currentbulletnum].get_rect())
                        bulletrectlist[currentbulletnum].center = screencenter

                    
                        currentbulletnum += 1
                        
                    #print("BL: ",bulletlist)
                    #print("BL rect: ", bulletrectlist)
                    #print("Angle: ",anglelist)
                    #print("Mouse Pos: ",mouseposlist)
                    #print("X speed: ",xspeedlist)
                    #print("Y speed: ",yspeedlist)
                    #print("\n")

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
        for i in range(len(bulletlist)):
            Display.blit(bulletlist[i],bulletrectlist[i])
            bulletrectlist[i].centerx += xspeedlist[i]
            bulletrectlist[i].centery += yspeedlist[i]
            #print("BulletRect.centerx: ",bulletrectlist[i].centerx)
            #print("BulletRect.centery: ",bulletrectlist[i].centery)

        for i in range(len(bulletlist)):
            if (bulletrectlist[i].centerx >= screenwidth or bulletrectlist[i].centerx < 0 or bulletrectlist[i].centery > screenheight or bulletrectlist[i].centery < 0):
                #shoot = False
                bulletlist.remove(bulletlist[i])
                bulletrectlist.remove(bulletrectlist[i])
                anglelist.remove(anglelist[i])
                mouseposlist.remove(mouseposlist[i])
                xspeedlist.remove(xspeedlist[i])
                yspeedlist.remove(yspeedlist[i])
                currentbulletnum -= 1
                break
    
    #print("BL: ",bulletlist)
    #print("BL rect: ", bulletrectlist)
    #print("Angle: ",anglelist)
    #print("Mouse Pos: ",mouseposlist)
    #print("X speed: ",xspeedlist)
    #print("Y speed: ",yspeedlist)
    #print("\n")
    
    pygame.display.update()
    pygame.time.Clock().tick(setfps);#fps
    
