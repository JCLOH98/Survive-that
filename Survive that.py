import pygame,sys
from pygame.locals import *

screenwidth = 450
screenheight = 600
setfps = 30

pygame.init()
Display = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Survive That!")

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

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

#player sprite
class Player:
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def InitPlayerRect(self):
        self.playerrect = Rect(self.x,self.y,self.width,self.height)

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

def background(camerax,cameray,MoveRect):
    Display.fill(GREY)
    thebackgroundRect.centerx += camerax
    thebackgroundRect.centery += cameray

    #both the 50 is the player width, and player height
    #it is also a referenct for the border
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
    player = Player(0,0,50,50)
    player.InitPlayerRect()
    player.SetRectCenter(screenwidth/2,screenheight/2)

    #player movable area
    MoveRect = Rect(0,0,150,150)
    MoveRect.center = (screenwidth/2,screenheight/2)

    #camera
    camerax = 0
    cameray = 0

    while True:
        background(camerax,cameray,MoveRect)
        key = pygame.key.get_pressed()
        
        #init player
        player.PlayerRect()
        #mouse position
        mousepos = pygame.mouse.get_pos()
        
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
                    print("shoot bullet")

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
        pygame.draw.rect(Display,BLUE,player.PlayerRect())

        #draw move area
        pygame.draw.rect(Display,RED,MoveRect,1)

        #mouse if not within the playerrect
        if (player.PlayerRect().collidepoint(mousepos) == False):
            #draw a line between mousepos and playerrect center
            pygame.draw.line(Display,GREEN,(player.GetRectCenter()),mousepos,3)

        pygame.display.update()
        pygame.time.Clock().tick(setfps);#fps

main()
