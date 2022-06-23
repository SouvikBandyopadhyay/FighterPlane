import time
from EnemyPos import enemypos
from PLAYERS.Player import Player
from PLAYERS.Enemy import Enemy
from BULLET.Bullet import Bullet
import helperFunctions
from Lobby import Text


import pygame
pygame.init()
winx=winy=500
screen =pygame.display.set_mode((winx,winy))
pygame.display.set_caption("CARSZ")



# ENEMY

enemyCountPerLine=10
# enemylist={x:0 for x in range(enemyCountPerLine)}
enemylist={i:(enemypos[0][i][0],enemypos[0][i][1]) for i in range(len(enemypos[0]))}

for i in enemylist:
    enemylist[i]=Enemy(winx,enemylist[i][0],enemylist[i][1])
player1=Player()

# DISPLAY
def displayObject(img, posX, posY):
    screen.blit(img, (posX, posY))


# BULLET

bulletlist=[]
lastbullet=0
now=time.time()
timeBtwnBullet=Bullet.timeBtwnBullet


enemybulletlist=list()

# SCORE DEF
score_val=0
level_val=0
k=0
level=Text('LEVEL:'+str(level_val))
# SCORE END

# MAIN INGAME FUNC

def insideLvl():
    global enemylist,bulletlist,now,enemybulletlist,score_val

    # PLAYER---------------------------------------------------------------------
    # CAPTUREING BULLET SHOT
    if key[pygame.K_SPACE] and time.time() - now > timeBtwnBullet:
        bullet1 = Bullet(player1.player1X + (player1.player1Width / 2) - (Bullet.width / 2), player1.player1Y)
        bulletlist.append(bullet1)
        now = time.time()

    # DETECTION COLLISION ON PLAYER BULLET
    prevEnemyLen=len(enemylist)
    enemylist, bulletlist = (helperFunctions.isCollision(enemylist, bulletlist))
    remove_bullet = list()
    for i in bulletlist:
        if (i.posY < 0):
            remove_bullet.append(i)
        else:
            i.doMovement()
            displayObject(i.bullet, i.posX, i.posY)
    bulletlist = [x for x in bulletlist if x not in remove_bullet]

    # PLAYER MOVEMENT
    player1.doMovement(key, winx, winy)
    displayObject(player1.player1, player1.player1X, player1.player1Y)

    # ENEMY----------------------------------------------------------------------

    # SHOOTING ENEMY BULLET
    for i in enemylist:
        enemybullet=helperFunctions.shootEnemyBullet(enemylist[i])
        enemylist[i].doMovement()
        if enemybullet:
            enemybulletlist.append(enemybullet)
    # DISPLAY ENEMY
    for i in enemylist:
        displayObject(enemylist[i].player1, enemylist[i].player1X, enemylist[i].player1Y)
    # DISPLAY ENEMY BULLETS
    for i in enemybulletlist:
        i.doMovement()
        displayObject(i.bullet,i.posX,i.posY)

    # SCORE-------------------------------------------------------------------------

    score_val +=  prevEnemyLen-len(enemylist)
    score = Text('SCORE:' + str(score_val))
    displayObject(level.text,10,20)
    displayObject(score.text, 10, 50)

    # INCASE PLAYER IS DEAD---------------------------------------------------------
    if(helperFunctions.isplayerdead(player1,enemybulletlist)):
        return 0

    if len(enemylist) < 1:
        return 0
    return 1

# IN LOBBY
def inLobby():
    global score_val,enemylist,enemybulletlist,bulletlist,level_val,enemypos,level

    if level_val<1:
        START = Text("START (S) ")
        displayObject(START.text, winx / 2 - 20, winy / 2 - 200)
        if key[pygame.K_s]:
            level_val+=1
            return 1
        return 0
    else:
        enemybulletlist = []
        enemylist = []
        bulletlist = []
        player1.restoreDefaults()
        level = Text('LEVEL:' + str(level_val))
        displayObject(level.text,winx/2-20 ,winy/2-200)
        score=Text("SCORE: "+str(score_val))
        displayObject(score.text, winx / 2 - 20, winy / 2 + 30 - 200)
        if(score_val>=len(enemypos[level_val-1])):
            next_Level = Text("NEXT LEVEL (N)")
            displayObject(next_Level.text, winx / 2 - 100, winy / 2 + 30)
            if key[pygame.K_n]:
                score_val = 0
                if level_val < len(enemypos):
                    level_val += 1

                enemylist = {i: (enemypos[level_val - 1][i][0], enemypos[level_val - 1][i][1]) for i in
                             range(len(enemypos[level_val - 1]))}
                for i in enemylist:
                    enemylist[i] = Enemy(winx, enemylist[i][0], enemylist[i][1])
                return 1
        try_Again = Text("RETRY (R)")
        displayObject(try_Again.text, winx / 2 + 50, winy / 2 + 30)
        if key[pygame.K_r]:
            score_val = 0
            enemylist = {i: (enemypos[level_val-1][i][0], enemypos[level_val-1][i][1]) for i in range(len(enemypos[level_val-1]))}
            for i in enemylist:
                enemylist[i] = Enemy(winx, enemylist[i][0], enemylist[i][1])
            return 1


        return 0


running = True
while running:
    screen.fill((10, 20, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()

    if k==1:
        k=insideLvl()
    if(k==0):
        k=inLobby()

    pygame.display.update()
