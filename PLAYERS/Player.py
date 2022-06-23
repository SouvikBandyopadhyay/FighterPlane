import pygame
# pygame.init()
from PLAYERS.Person import Person


class Player(Person):
    player1 = pygame.image.load("player1.png")

    player1 = pygame.transform.scale(player1, (Person.player1Width, Person.player1Hight))
    player1X = 230
    player1Y = 390
    speed = 0.07

    def doMovement(self,key,winx,winy):
        
        if key[pygame.K_LEFT] and self.player1X > self.speed:
            self.player1X -= self.speed
        if key[pygame.K_RIGHT] and self.player1X + self.player1Width < winx:
            self.player1X += self.speed
        if key[pygame.K_UP] and self.player1Y > self.speed:
            self.player1Y -= self.speed
        if key[pygame.K_DOWN] and self.player1Y + self.player1Hight < winy:
            self.player1Y += self.speed

    def restoreDefaults(self):
        self.player1X = 230
        self.player1Y = 390

