import random

import pygame
import time
from PLAYERS.Person import Person

# pygame.init()


class Enemy(Person):
    player1 = pygame.image.load("enemy.png")

    player1 = pygame.transform.scale(player1, (Person.player1Width, Person.player1Hight))
    player1X = 10
    player1Y = 50
    speed = 0.05
    flag=random.randint(0,1)
    winx=0
    lastshot=time.time()

    def __init__(self,winx,x,y):
        self.player1X+=x-(self.player1Width/2)
        self.player1Y=y
        self.winx=winx


    def doMovement(self):
        if(self.flag==0):
            self.player1X=self.player1X-self.speed
            if(self.player1X<30):
                self.player1Y += 10
                self.flag=1
        else:
            self.player1X=self.player1X+self.speed
            if (self.player1X > self.winx-self.player1Width-30 ):
                self.player1Y+=10
                self.flag = 0

    def move(self,dir):
        for i in dir:
            i.doMovement()




