from BULLET.EnemyBullet import EnemyBullet
import time

timeBtwnBullet=EnemyBullet.timeBtwnBullet

def shootEnemyBullet(enemy):
    if(time.time() - enemy.lastshot > timeBtwnBullet):
        enemy.lastshot=time.time()
        return EnemyBullet(enemy.player1X,enemy.player1Y)



def isCollision(enemylist,bulletlist):
    collided=list()
    bullet_del=list()
    for i in bulletlist:
        for j in enemylist:
            if i.posX>enemylist[j].player1X-i.width and i.posX<enemylist[j].player1X+enemylist[j].player1Width and i.posY<=enemylist[j].player1Y+enemylist[j].player1Hight and i.posY+i.hight>=enemylist[j].player1Y:
                collided.append(j)
                bullet_del.append(i)
    for i in collided:
        try:
            enemylist.pop(i)
        except:
            print("enemy not found")



    bulletlist=[i for i in bulletlist if i not in bullet_del]
    return (enemylist,bulletlist)


def isplayerdead(player1,enemybulletlist):
    for i in enemybulletlist:
        if i.posX+i.width>player1.player1X and i.posX<player1.player1X+player1.player1Width and i.posY>=player1.player1Y and i.posY<player1.player1Y+player1.player1Hight:
            return True