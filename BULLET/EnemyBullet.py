import pygame
from BULLET.BulletMain import BulletMain
pygame.init()

class EnemyBullet(BulletMain):
    posX=posY=0
    bullet = pygame.image.load('enemyBullet.png')
    bullet = pygame.transform.scale(bullet, (BulletMain.width, BulletMain.hight))
    timeBtwnBullet = 3

    def __init__(self,posX,posY):
        self.posX=posX
        self.posY=posY

    def doMovement(self):
        self.posY+=BulletMain.speed