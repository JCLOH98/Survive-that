import math
from math import *
import pygame,sys
from pygame.locals import *

screenwidth = 450
screenheight = 600
setfps = 30

pygame.init()
Display = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Survive That! (proto)")

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)

#print(Display.get_size())
#screenwidth, screenheight = Display.get_size()

#Set Cursor
#pygame.mouse.set_cursor(*pygame.cursors.tri_left)
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

        #if (self.width > self.height):
            #self.playerrect = Rect(0,0,self.width,self.width)
        #if (self.height > self.width):
            #self.playerrect = Rect(0,0,self.height,self.height)
        #if (self.width == self.height):
            #self.playerrect = Rect(0,0,
                                   #2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))),
                                   #2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))))
            
        self.playerrect = Rect(0,0,2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))),2*sqrt(((self.width/2)*(self.width/2)) + ((self.height/2)*(self.height/2))))
        self.playerrect.center = (screenwidth/2, screenheight/2)

    def PlayerRect(self):
        return self.playerrect

    def MoveUp(self):
        self.playerrect.centery -= 5
        pass

    def MoveDown(self):
        self.playerrect.centery += 5
        pass

    def MoveLeft(self):
        self.playerrect.centerx -= 5
        pass

    def MoveRight(self):
        self.playerrect.centerx += 5
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
        
        pass

#bullet class
class Bullet:
    
    def __init__(self,number):
        self.BAmount = number
        self.BList = []
        self.BRectList = []
        self.BMousePos = []
        self.BAngle = []
        self.BXspeed = []
        self.BYspeed = []

        self.BCurrent = 0

    def SetBulletRect(self,width,height):
        self.bulletsurf = pygame.Surface((width,height))
        self.bulletsurf.set_colorkey(GREY)
        self.bulletsurf.fill(AQUA)
        
        self.bulletrect = self.bulletsurf.get_rect()

#enemies
class Enemy:
    def __init__(self,width,height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.amount = 0

        self.enemylist = []
        self.enemyangle = []

        self.xspeed = 5
        self.yspeed = 5

        self.enemysurf = pygame.Surface((self.width,self.height))
        self.enemysurf.set_colorkey(GREY) #can be anycolor other than red
        self.enemysurf.fill(RED)

        self.enemyrect = self.enemysurf.get_rect()

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

    if thebackgroundRect.centerx < 0 - MoveRect.left + 50:
        thebackgroundRect.centerx = 0 - MoveRect.left + 50

    if thebackgroundRect.centery > screenheight + MoveRect.top - 50:
        thebackgroundRect.centery = screenheight + MoveRect.top - 50

    if thebackgroundRect.centery < 0 - MoveRect.top + 50:
        thebackgroundRect.centery = 0 - MoveRect.top + 50

    Display.blit(thebackground,thebackgroundRect)

def main():
    #player
    player = Player(0,0,40,50)
    player.InitPlayerRect()
    #player.SetRectCenter(screenwidth/2,screenheight/2)

    #bullet
    bullet = Bullet(4) #player can shoot max 4 bullet
    bullet.SetBulletRect(50,25)

    #enemy
    enemy = Enemy(50,40)#width, height
    enemy.SetEnemyAmount(1)

    #player movable area
    MoveRect = Rect(0,0,150,150)
    MoveRect.center = (screenwidth/2,screenheight/2)    
    
    #camera
    camerax = 0
    cameray = 0

    #the speed
    thespeed = 20

    while True:
        background(camerax,cameray,MoveRect)
        key = pygame.key.get_pressed()
        
        #mouse position
        mousepos = pygame.mouse.get_pos()

        #the angle (from player to mousepos)
        #calculate the angle from +ve x-axis
        if (abs(mousepos[0] - player.GetRectCenter()[0]) != 0):
            #1st quad
            if (mousepos[0] > player.GetRectCenter()[0] and mousepos[1] < player.GetRectCenter()[1]):
                angle = math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            #2nd quad
            if (mousepos[0] < player.GetRectCenter()[0] and mousepos[1] < player.GetRectCenter()[1]):
                angle = math.pi - math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            #3rd quad
            if (mousepos[0] < player.GetRectCenter()[0] and mousepos[1] > player.GetRectCenter()[1]):
                angle = math.pi  + math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            #4th quad
            if (mousepos[0] > player.GetRectCenter()[0] and mousepos[1] > player.GetRectCenter()[1]):
                angle = 2*math.pi - math.atan2(abs(mousepos[1] - player.GetRectCenter()[1]) , abs(mousepos[0] - player.GetRectCenter()[0]))
            
        else:
            #90 degree
            if (mousepos[1] < player.GetRectCenter()[1]):
                angle = math.pi/2
            #270 degree
            if (mousepos[1] > player.GetRectCenter()[1]):
                angle = 2*math.pi - math.pi/2

        #print("Angle (degree): ",angle/math.pi*180)

        #angle from enemy to player
        for i in range(len(enemy.enemylist)):
            pass

        #set player to rotate
        player.SetSurf(pygame.transform.rotate(player.playersurf,angle/math.pi*180))
        #ThePlayer = pygame.transform.rotate(player.playersurf,angle/math.pi*180)
        #ThePlayerRect = ThePlayer.get_rect()
        #ThePlayerRect.center = player.GetRectCenter()
        
        if (key[K_w]):
            #print ("up")
            player.MoveUp()
            
        if (key[K_s]):
            #print("down")
            player.MoveDown()
            
        if (key[K_a]):
            #print("left")
            player.MoveLeft()
            
        if (key[K_d]):
            #print("right")
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
                    #print("shoot bullet")

                    #if the current bullet amount is not the max amount
                    if (bullet.BCurrent < bullet.BAmount):
                        bullet.BMousePos.append(mousepos)
                        bullet.BAngle.append(angle)
                        PlayerCenter = player.GetRectCenter()

                        if (bullet.BMousePos[bullet.BCurrent][0] > PlayerCenter[0] and bullet.BMousePos[bullet.BCurrent][1] < PlayerCenter[1]):
                            bullet.BXspeed.append(thespeed * cos(bullet.BAngle[bullet.BCurrent])) #+ve speed
                            bullet.BYspeed.append(-thespeed * sin(bullet.BAngle[bullet.BCurrent])) #-ve speed
                            #print("1st quad")
                            
                        if (bullet.BMousePos[bullet.BCurrent][0] < PlayerCenter[0] and bullet.BMousePos[bullet.BCurrent][1] < PlayerCenter[1]):
                            bullet.BXspeed.append(thespeed * cos(bullet.BAngle[bullet.BCurrent])) #+ve speed
                            bullet.BYspeed.append(-thespeed * sin(bullet.BAngle[bullet.BCurrent])) #-ve speed
                            #print("2nd quad")
                            
                        if (bullet.BMousePos[bullet.BCurrent][0] < PlayerCenter[0] and bullet.BMousePos[bullet.BCurrent][1] > PlayerCenter[1]):
                            bullet.BXspeed.append(thespeed * cos(bullet.BAngle[bullet.BCurrent])) #+ve speed
                            bullet.BYspeed.append(-thespeed * sin(bullet.BAngle[bullet.BCurrent])) #-ve speed
                            #print("3rd quad")
                            
                        if (bullet.BMousePos[bullet.BCurrent][0] > PlayerCenter[0] and bullet.BMousePos[bullet.BCurrent][1] > PlayerCenter[1]):
                            bullet.BXspeed.append(thespeed * cos(bullet.BAngle[bullet.BCurrent])) #+ve speed
                            bullet.BYspeed.append(-thespeed * sin(bullet.BAngle[bullet.BCurrent])) #-ve speed
                            #print("4th quad")

                        #on x-axis
                        if (bullet.BMousePos[bullet.BCurrent][1] ==  PlayerCenter[1]):
                            if (bullet.BMousePos[bullet.BCurrent][0] > PlayerCenter[0]):
                                bullet.BXspeed.append(thespeed)
                                bullet.BYspeed.append(0)
                                #print("right side")
                            elif (bullet.BMousePos[bullet.BCurrent][0] < PlayerCenter[0]):
                                bullet.BXspeed.append(-thespeed)
                                bullet.BYspeed.append(0)
                                #print("left side")
                                
                        #on y-axis
                        if (bullet.BMousePos[bullet.BCurrent][0] == PlayerCenter[0]):
                            if (bullet.BMousePos[bullet.BCurrent][1] < PlayerCenter[1]):
                                bullet.BXspeed.append(0)
                                bullet.BYspeed.append(-thespeed)
                                #print("up side")
                            elif (bullet.BMousePos[bullet.BCurrent][1] > PlayerCenter[1]):
                                bullet.BXspeed.append(0)
                                bullet.BYspeed.append(thespeed)
                                #print("down side")                    
                    
                    #starting position bullet
                    if (bullet.BCurrent < bullet.BAmount):
                        bullet.BList.append(pygame.transform.rotate(bullet.bulletsurf, bullet.BAngle[bullet.BCurrent]/math.pi*180))
                        bullet.BRectList.append(bullet.BList[bullet.BCurrent].get_rect())
                        bullet.BRectList[bullet.BCurrent].center = player.GetRectCenter()

                        bullet.BCurrent += 1
                        

                if pygame.mouse.get_pressed() == RIGHT_CLICK:
                    print("throw grenade")

        #if the playerrect doesnt contain in the area,
        #the the camera should move
        if MoveRect.contains(player.PlayerRect()) == False:
            #print("out of bound")
            if (player.PlayerRect().right >= MoveRect.right):
                #print("out of right")
                player.SetRectRight(MoveRect.right)
                camerax = -5
                
            if (player.PlayerRect().left <= MoveRect.left):
                #print("out of left")
                player.SetRectLeft(MoveRect.left)
                camerax = +5
                
            if (player.PlayerRect().top <= MoveRect.top):
                #print("out of top")
                player.SetRectTop(MoveRect.top)
                cameray = +5
                
            if (player.PlayerRect().bottom >= MoveRect.bottom):
                #print("out of bottom")
                player.SetRectBottom(MoveRect.bottom)
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
        pygame.draw.rect(Display,RED,MoveRect,1)

        #draw  x-axis
        pygame.draw.line(Display,WHITE,(0, player.GetRectCenter()[1]), (screenwidth, player.GetRectCenter()[1]), 2)
        #draw y-axis
        pygame.draw.line(Display,WHITE,(player.GetRectCenter()[0], 0), (player.GetRectCenter()[0], screenheight), 2)
        
        #mouse if not within the playerrect
        if (player.PlayerRect().collidepoint(mousepos) == False):
            #draw a line between mousepos and playerrect center
            pygame.draw.line(Display,RED,(player.GetRectCenter()),mousepos,2)

        #shoot the bullet
        for i in range(len(bullet.BList)):
            Display.blit(bullet.BList[i],bullet.BRectList[i])
            bullet.BRectList[i].centerx += bullet.BXspeed[i]
            bullet.BRectList[i].centery += bullet.BYspeed[i]
            #print("BulletRect.centerx: ",bulletrectlist[i].centerx)
            #print("BulletRect.centery: ",bulletrectlist[i].centery)

        for i in range(len(bullet.BList)):
            if (bullet.BRectList[i].centerx >= screenwidth or bullet.BRectList[i].centerx < 0 or bullet.BRectList[i].centery > screenheight or bullet.BRectList[i].centery < 0):
                #shoot = False
                bullet.BList.remove(bullet.BList[i])
                bullet.BRectList.remove(bullet.BRectList[i])
                bullet.BAngle.remove(bullet.BAngle[i])
                bullet.BMousePos.remove(bullet.BMousePos[i])
                bullet.BXspeed.remove(bullet.BXspeed[i])
                bullet.BYspeed.remove(bullet.BYspeed[i])
                bullet.BCurrent -= 1
                break

        #enemy
        for i in range(len(enemy.enemylist)):                
            pass
        

        pygame.display.update()
        pygame.time.Clock().tick(setfps);#fps

main()
