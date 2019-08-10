import random
import time
import math
from math import *
import pygame,sys
from pygame.locals import *

screenwidth = 450
screenheight = 600
setfps = 30

pygame.init()
Display = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Enemy System")

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)

#Set Cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

#Mouse click
LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

#background
thebackground = pygame.image.load("./SurviveThat_BG.png").convert_alpha()
thebackgroundRect = Rect(0,0,900,1200)
thebackgroundRect.center = (screenwidth/2, screenheight/2)

#angle from +ve x-axis
angle = 0

#player
playerwidth = 40
playerheight = 50

playerspeed = 5

#enemy
enemywidth = 30
enemyheight = 40

enemyspeed = 1

#player sprite
class Player:
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def InitPlayerRect(self):
        self.playersurf = pygame.Surface((self.width,self.height))
        self.playersurf.set_colorkey(GREY)
        self.playersurf.fill(BLUE)
            
        self.playerrect = Rect(0,0,2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))),2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))))
        self.playerrect.center = (screenwidth/2, screenheight/2)

    def PlayerRect(self):
        return self.playerrect

    def MoveUp(self):
        self.playerrect.centery -= playerspeed
        pass

    def MoveDown(self):
        self.playerrect.centery += playerspeed
        pass

    def MoveLeft(self):
        self.playerrect.centerx -= playerspeed
        pass

    def MoveRight(self):
        self.playerrect.centerx += playerspeed
        pass

    def SetRectCenter(self,x,y):
        self.playerrect.center = (x,y)

    def GetRectCenter(self):
        return self.playerrect.center

    def SetRectLeft(self,left):
        self.playerrect.left = left

    def SetRectRight(self,right):
        self.playerrect.right = right
    
    def SetRectTop(self,top):
        self.playerrect.top = top

    def SetRectBottom(self,bot):
        self.playerrect.bottom = bot

    def SetSurf(self,Surf):
        self.theplayersurf = Surf
        self.theplayerrect = self.theplayersurf.get_rect()
        self.theplayerrect.center = self.playerrect.center
        
#enemies
class Enemy:
    def __init__(self,width,height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.amount = 0

        self.enemysurfacelist = []
        self.enemysurfrectlist = []
        self.enemyrectlist = []
        self.enemyanglelist = []

        self.xspeed = 3
        self.yspeed = 3

        self.enemysurf = pygame.Surface((self.width,self.height))
        self.enemysurf.set_colorkey(GREY) #can be anycolor other than red
        self.enemysurf.fill(RED)

        self.enemyrect = Rect(0,0,2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))),2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))))

    def SetEnemyAmount(self,number):
        self.amount = number
    
    
def background(camerax,cameray,MoveRect):
    Display.fill(GREY)
    thebackgroundRect.centerx += camerax
    thebackgroundRect.centery += cameray

    #both the 50 is the player width, and player height
    #it is also a reference for the border
    if thebackgroundRect.centerx > screenwidth + MoveRect.left - 50 :
        thebackgroundRect.centerx = screenwidth + MoveRect.left - 50
        Display.blit(thebackground,thebackgroundRect)
        return True

    if thebackgroundRect.centerx < 0 - MoveRect.left + 50:
        thebackgroundRect.centerx = 0 - MoveRect.left + 50
        Display.blit(thebackground,thebackgroundRect)
        return True

    if thebackgroundRect.centery > screenheight + MoveRect.top - 50:
        thebackgroundRect.centery = screenheight + MoveRect.top - 50
        Display.blit(thebackground,thebackgroundRect)
        return True

    if thebackgroundRect.centery < 0 - MoveRect.top + 50:
        thebackgroundRect.centery = 0 - MoveRect.top + 50
        Display.blit(thebackground,thebackgroundRect)
        return True

    Display.blit(thebackground,thebackgroundRect)

    return False

def main():
    
    TheTime = 0
    Start = time.time()#start time
    
    #player
    player = Player(0,0,playerwidth,playerheight)
    player.InitPlayerRect()

    #enemy
    enemy = Enemy(enemywidth,enemyheight)#width, height
    enemy.SetEnemyAmount(2) #amount of enemy

    #player movable area
    MoveRect = Rect(0,0,150,150)
    MoveRect.center = (screenwidth/2,screenheight/2)    
    
    #camera
    camerax = 0
    cameray = 0

    #the speed
    thespeed = 20

    #enemyspawnset
    enemyspawnset = 0
    enemyspawnset2 = 0
    randx = 0
    randy = 0
    NewRect = enemy.enemyrect
    enemyangle = 0

    while True:
        #use background to determine the camerax and cameray, so that when it reaches border, enemy can catch up
        if background(camerax,cameray,MoveRect):
            camerax = 0
            cameray = 0
            
        key = pygame.key.get_pressed()

        End = time.time()#end time
        if (int(End) - int(Start) == 1):
                        TheTime += 1
                        Start = time.time()
                        #print(TheTime)
                        if TheTime % 5 == 0: #every 5 seconds
                            if (len(enemy.enemyrectlist) < enemy.amount): #if the enemy on screen is not the enemy.amount
                                #print(len(enemy.enemylist))
                                enemyspawnset = random.randint(1,2)
                                enemyspawnset2 = random.randint(1,2)

                                if (enemyspawnset == 1):
                                    randx = random.randint(0,screenwidth)
                                    if enemyspawnset2 == 1:
                                        randy = random.randint(-enemyheight, 0)#-enemy.enemyrect.height
                                    else: # enemyspawnset2 == 2
                                        randy = random.randint(screenheight, screenheight + enemyheight)#+ enemy.enemyrect.height
                                    
                                else: # enemyspawnset== 2
                                    randy = random.randint(0,screenheight)
                                    if enemyspawnset2 == 1:
                                        randx = random.randint(-enemywidth, 0)#-enemy.enemyrect.width
                                    else:
                                        randx = random.randint(screenwidth, screenwidth + enemywidth)#+ enemy.enemyrect.width

                                NewRect = Rect(randx,randy,enemy.enemyrect.width, enemy.enemyrect.height) #the outer box size
                                enemy.enemyrectlist.append(NewRect)
                                print(randx,randy)
        
        #mouse position
        mousepos = pygame.mouse.get_pos()

        #angle from enemy to playercenter
        for i in range(len(enemy.enemyrectlist)):
            if (abs(player.GetRectCenter()[0] - enemy.enemyrectlist[i].centerx) != 0):
                #1st quad
                if (player.GetRectCenter()[0] > enemy.enemyrectlist[i].centerx and player.GetRectCenter()[1] <= enemy.enemyrectlist[i].centery):
                    enemyangle = math.atan2(abs(player.GetRectCenter()[1] - enemy.enemyrectlist[i].centery) , abs(player.GetRectCenter()[0] - enemy.enemyrectlist[i].centerx))
                #2nd quad
                if (player.GetRectCenter()[0] < enemy.enemyrectlist[i].centerx and player.GetRectCenter()[1] <= enemy.enemyrectlist[i].centery):
                    enemyangle = math.pi - math.atan2(abs(player.GetRectCenter()[1] - enemy.enemyrectlist[i].centery) , abs(player.GetRectCenter()[0] - enemy.enemyrectlist[i].centerx))
                #3rd quad
                if (player.GetRectCenter()[0] < enemy.enemyrectlist[i].centerx and player.GetRectCenter()[1] >= enemy.enemyrectlist[i].centery):
                    enemyangle = math.pi  + math.atan2(abs(player.GetRectCenter()[1] - enemy.enemyrectlist[i].centery) , abs(player.GetRectCenter()[0] - enemy.enemyrectlist[i].centerx))
                #4th quad
                if (player.GetRectCenter()[0] > enemy.enemyrectlist[i].centerx and player.GetRectCenter()[1] >= enemy.enemyrectlist[i].centery):
                    enemyangle = 2*math.pi - math.atan2(abs(player.GetRectCenter()[1] - enemy.enemyrectlist[i].centery) , abs(player.GetRectCenter()[0] - enemy.enemyrectlist[i].centerx))
                
            else:
                #90 degree
                if (player.GetRectCenter()[1] < enemy.enemyrectlist[i].centery):
                    enemyangle = math.pi/2
                #270 degree
                if (player.GetRectCenter()[1] > enemy.enemyrectlist[i].centery):
                    enemyangle = 2*math.pi - math.pi/2

            #enemy angle list
            if (len(enemy.enemyanglelist) != len(enemy.enemyrectlist)):
                if (len(enemy.enemyrectlist) > len(enemy.enemyanglelist)):
                    enemy.enemyanglelist.append(enemyangle/math.pi*180)
            else:
                enemy.enemyanglelist[i] = enemyangle/math.pi*180

            #enemy surface list
            if (len(enemy.enemysurfacelist) != len(enemy.enemyrectlist)):
                if (len(enemy.enemyrectlist) > len(enemy.enemysurfacelist)):
                    enemy.enemysurfacelist.append(pygame.transform.rotate(enemy.enemysurf,enemy.enemyanglelist[i]))
            else:
                enemy.enemysurfacelist[i] = pygame.transform.rotate(enemy.enemysurf,enemy.enemyanglelist[i])

            #enemy surface list de rect
            TheEnemyRect = enemy.enemysurfacelist[i].get_rect()
            TheEnemyRect.center = enemy.enemyrectlist[i].center
            if (len(enemy.enemysurfrectlist) != len(enemy.enemyrectlist)):
                if (len(enemy.enemyrectlist) > len(enemy.enemysurfrectlist)):
                    enemy.enemysurfrectlist.append(TheEnemyRect)
            else:
                enemy.enemysurfrectlist[i] = TheEnemyRect
        
        #the angle (from player to mousepos)
        #calculate the angle from +ve x-axis
        if (abs(mousepos[0] - player.GetRectCenter()[0]) != 0):
            #1st quad
            if (mousepos[0] > player.GetRectCenter()[0] and mousepos[1] <= player.GetRectCenter()[1]):
                angle = math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            #2nd quad
            if (mousepos[0] < player.GetRectCenter()[0] and mousepos[1] <= player.GetRectCenter()[1]):
                angle = math.pi - math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            #3rd quad
            if (mousepos[0] < player.GetRectCenter()[0] and mousepos[1] >= player.GetRectCenter()[1]):
                angle = math.pi  + math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            #4th quad
            if (mousepos[0] > player.GetRectCenter()[0] and mousepos[1] >= player.GetRectCenter()[1]):
                angle = 2*math.pi - math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            
        else:
            #90 degree
            if (mousepos[1] < player.GetRectCenter()[1]):
                angle = math.pi/2
            #270 degree
            if (mousepos[1] > player.GetRectCenter()[1]):
                angle = 2*math.pi - math.pi/2

        #print("Angle (degree): ",angle/math.pi*180)
        
        #set player to rotate
        player.SetSurf(pygame.transform.rotate(player.playersurf,angle/math.pi*180))

        #enemy goes to the direction of player
        for i in range(len(enemy.enemysurfacelist)):
            #A,S,T,C
            #1st quad
            if (enemy.enemyrectlist[i].centerx > player.GetRectCenter()[0] and enemy.enemyrectlist[i].centery < player.GetRectCenter()[1]):
                enemy.enemyrectlist[i].centerx -= enemyspeed - camerax #-ve xspeed
                enemy.enemyrectlist[i].centery += enemyspeed + cameray #+ve yspeed
            #2nd quad
            if (enemy.enemyrectlist[i].centerx < player.GetRectCenter()[0] and enemy.enemyrectlist[i].centery < player.GetRectCenter()[1]):
                enemy.enemyrectlist[i].centerx += enemyspeed + camerax #+ve xspeed
                enemy.enemyrectlist[i].centery += enemyspeed + cameray #+ve yspeed
                pass
            #3rd quad
            if (enemy.enemyrectlist[i].centerx < player.GetRectCenter()[0] and enemy.enemyrectlist[i].centery > player.GetRectCenter()[1]):
                enemy.enemyrectlist[i].centerx += enemyspeed + camerax #+ve xspeed
                enemy.enemyrectlist[i].centery -= enemyspeed - cameray#-ve yspeed
                pass
            #4th quad
            if (enemy.enemyrectlist[i].centerx > player.GetRectCenter()[0] and enemy.enemyrectlist[i].centery > player.GetRectCenter()[1]):
                enemy.enemyrectlist[i].centerx -= enemyspeed - camerax #-ve xspeed
                enemy.enemyrectlist[i].centery -= enemyspeed - cameray #-ve yspeed
                pass

            #on x axis (got problem)
            if (enemy.enemyrectlist[i].centery ==  player.GetRectCenter()[1]):
                #+ve x axis
                if (enemy.enemyrectlist[i].centerx >  player.GetRectCenter()[0]):
                    enemy.enemyrectlist[i].centerx -= enemyspeed
                    if cameray != 0:
                        enemy.enemyrectlist[i].centery += enemyspeed + cameray
                #-ve x axis
                elif (enemy.enemyrectlist[i].centerx <  player.GetRectCenter()[0]):
                    enemy.enemyrectlist[i].centerx += enemyspeed
                    if cameray != 0:
                        enemy.enemyrectlist[i].centery -= enemyspeed - cameray

            #on y axis (got problem)
            if (enemy.enemyrectlist[i].centerx ==  player.GetRectCenter()[0]):
                #+ve y axis
                if (enemy.enemyrectlist[i].centery >  player.GetRectCenter()[1]):
                    enemy.enemyrectlist[i].centery -= enemyspeed - cameray
                    if camerax != 0:
                        enemy.enemyrectlist[i].centerx += enemyspeed + camerax

                #-ve y axis
                elif (enemy.enemyrectlist[i].centery <  player.GetRectCenter()[1]):
                    enemy.enemyrectlist[i].centery += enemyspeed + cameray
                    if camerax != 0:
                        enemy.enemyrectlist[i].centerx -= enemyspeed - camerax

                
                    
        if (key[K_w]):
            player.MoveUp()
            
        if (key[K_s]):
            player.MoveDown()
            
        if (key[K_a]):
            player.MoveLeft()
            
        if (key[K_d]):
            player.MoveRight()
        
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

        #if the playerrect doesnt contain in the area,
        #the the camera should move
        if MoveRect.contains(player.PlayerRect()) == False:
            #print("out of bound")
            if (player.PlayerRect().right >= MoveRect.right):
                #print("out of right")
                player.SetRectRight(MoveRect.right-1)
                camerax = -5
                
            if (player.PlayerRect().left <= MoveRect.left):
                #print("out of left")
                player.SetRectLeft(MoveRect.left+1)
                camerax = +5
                
            if (player.PlayerRect().top <= MoveRect.top):
                #print("out of top")
                player.SetRectTop(MoveRect.top+1)
                cameray = +5
                
            if (player.PlayerRect().bottom >= MoveRect.bottom):
                #print("out of bottom")
                player.SetRectBottom(MoveRect.bottom-1)
                cameray = -5
        else:
            camerax = 0
            cameray = 0

        #DRAW
        #draw player
        #pygame.draw.rect(Display,YELLOW,player.playerrect)
        #pygame.draw.rect(Display,GREEN,player.theplayerrect)
        Display.blit(player.theplayersurf, player.theplayerrect)

        #draw move area
        pygame.draw.rect(Display,RED,MoveRect,3)

        #draw  x-axis
        pygame.draw.line(Display,WHITE,(0, player.GetRectCenter()[1]), (screenwidth, player.GetRectCenter()[1]), 2)
        #draw y-axis
        pygame.draw.line(Display,WHITE,(player.GetRectCenter()[0], 0), (player.GetRectCenter()[0], screenheight), 2)

        #enemy
        for i in range(len(enemy.enemysurfacelist)):                
            pass
        
        for i in range(len(enemy.enemyrectlist)):
            #pygame.draw.rect(Display,YELLOW,enemy.enemyrectlist[i])
            #pygame.draw.rect(Display,GREEN,enemy.enemysurfrectlist[i])
            Display.blit(enemy.enemysurfacelist[i],enemy.enemysurfrectlist[i])
            
            pygame.draw.line(Display,GREEN,(enemy.enemyrectlist[i].center),(player.GetRectCenter()),5)
            
        
        pygame.display.update()
        pygame.time.Clock().tick(setfps);#fps

main()
