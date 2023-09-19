# INITIALIZE
from math import pi, sin, cos, atan2
import random
import pygame


def get_angle(origin, destination):
    """Returns angle in radians from origin to destination.
        This is the angle that you would get if the points were
        on a cartesian grid. Arguments of (0,0), (1, -1)
        return pi/4 (45 deg) rather than  7/4.
        """
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return atan2(-y_dist, x_dist) % (2 * pi)


def project(pos, angle, distance):
    """
    Returns tuple of pos projected distance at angle
    adjusted for pygame's y-axis.

    EXAMPLES

    Move a sprite using it's angle and speed
    new_pos = project(sprite.pos, sprite.angle, sprite.speed)

    Find the relative x and y components of an angle and speed
    x_and_y = project((0, 0), angle, speed)
    """
    return (pos[0] + (cos(angle) * distance),
            pos[1] - (sin(angle) * distance))


pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

clock = pygame.time.Clock()
FPS = 60

white = (255,255,255)
black = (000,000,000)
RED = (255,000,000)
green = (000,255,000)
blue = (000,000,255)
purple = (255,000,255)

npcHitSound = 'sound.mp3'
enemyHitSound = 'tePeguei.mp3'

displayWidth = 900
displayHeight = 900
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('SpaceBrodar')

#Rand enemys POS
rand_x = random.randint(20,850)
rand_y = random.randint(20,850)
rand_x_2 = random.randint(20,850)
rand_y_2 = random.randint(20,850)

# CLASSES

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):

    player_x_change = 0
    player_y_change = 0

    def __init__(self, x, y, width, height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y):
        self.player_x_change = x
        self.player_y_change = y

    def checkCollision(self, walls, npcs, enemies, RandEnemy):

        # Walls

        self.rect.x += self.player_x_change

        wallHitList = pygame.sprite.spritecollide(self, walls, False)
        for wall in wallHitList:
            if self.player_x_change > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

        self.rect.y += self.player_y_change

        wallHitList = pygame.sprite.spritecollide(self, walls, False)
        for wall in wallHitList:
            if self.player_y_change > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom

        # NPCs

        npcHitList = pygame.sprite.spritecollide(self, npcs, True)
        if npcHitList:
            effect = pygame.mixer.Sound(npcHitSound)
            effect.set_volume(.25)
            effect.play()
            print("HIT")

        # Enemies

        enemyHitList = pygame.sprite.spritecollide(self, enemies, False)
        if enemyHitList:
            effect = pygame.mixer.Sound(enemyHitSound)
            effect.set_volume(.01)
            effect.play()
            self.rect.x = 450
            self.rect.y = 450
            print("HIT")

        RandEnemyHitList = pygame.sprite.spritecollide(self, RandEnemy,False)
        if RandEnemyHitList:
            effect = pygame.mixer.Sound(enemyHitSound)
            effect.set_volume(.20)
            effect.play()
            self.rect.x = 450
            self.rect.y = 450
            print("HIT")


    def getPosition(self, x, y):
        print(x, y)
        return x, y


class Npc(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(purple)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):

    enemy_x_change = 0
    enemy_y_change = 0

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.pos = self.rect.center
        self.speed = .2 #pixels per millisecond

    def update(self, dt, player):
        angle = get_angle(self.rect.center, player.rect.center)
        self.pos = project(self.pos, angle, self.speed * dt)
        self.rect.center = self.pos

    def getPosition(self, x, y):
        return x, y


class RandEnemy(pygame.sprite.Sprite):

    enemy_x_change = 0
    enemy_y_change = 0

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.pos = self.rect.center
        self.speed = .2 #pixels per millisecond

    def update(self, dt, player):
        angle = get_angle(self.rect.center, player.rect.center)
        self.pos = project(self.pos, angle, self.speed * dt)
        self.rect.center = self.pos

    def getPosition(self, x, y):
        return x, y


# DEFINE POSTITIONS AND SPEEDS

player_POS_x = displayWidth/2
player_POS_y = displayHeight/2
player_x_change = 0
player_y_change = 0
movementSpeed = 4
# enemy POS and speed
enemy_x_change = 0
enemy_y_change = 0
enemy_x = 20
enemy_y = 20
enemySpeed = 2


# CREATE SPRITES
# Sprite groups
playerList = pygame.sprite.Group()
randEnemysList = pygame.sprite.Group()
wallList = pygame.sprite.Group()
npcList = pygame.sprite.Group()
enemyList = pygame.sprite.Group()
allSpriteList = pygame.sprite.Group()

# Walls
# mid bars
wall = Wall(170,150,600,15)
wallList.add(wall)
allSpriteList.add(wall)
wall = Wall(170,800,600,15)
wallList.add(wall)
allSpriteList.add(wall)
#end mid bars
# top main bar
wall = Wall(0,0,900,10)
wallList.add(wall)
allSpriteList.add(wall)
# left main bar
wall = Wall(0,0,10,900)
wallList.add(wall)
allSpriteList.add(wall)
# left main bar
wall = Wall(890,0,10,900)
wallList.add(wall)
allSpriteList.add(wall)
#bottom bar
wall = Wall(0,890,900,10)
wallList.add(wall)
allSpriteList.add(wall)

    #NPCs

npc1 = Npc(rand_x,670,10,10)
npcList.add(npc1)
allSpriteList.add(npc1)
npc2 = Npc(700,rand_y,10,10)
npcList.add(npc2)
allSpriteList.add(npc2)

# Enemies
enemy = Enemy(enemy_x,enemy_y,30,30)
enemyList.add(enemy)
allSpriteList.add(enemy)

#randEnemys
enemy1 = RandEnemy(rand_x,400,30,30)
randEnemysList.add(enemy1)
allSpriteList.add(enemy1)
enemy2 = RandEnemy(300,rand_y,70,70)
randEnemysList.add(enemy2)
allSpriteList.add(enemy2)

# Player
player1 = Player(player_POS_x,player_POS_y,10,10)
playerList.add(player1)
allSpriteList.add(player1)

# star = pygame.image.load('man.png').convert_alpha()
# star.pygame.pygame.transform.scale(Surface, 30, 40)


# MAIN GAME LOOP
gameExit = False
while not gameExit:
    dt = clock.tick(FPS)
    # Event Handling

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                movementSpeed = 3
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0


    key = pygame.key.get_pressed()

    if key[pygame.K_LSHIFT]:
        movementSpeed = 8
    if key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
        player_x_change = -movementSpeed
    if key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
        player_x_change = movementSpeed
    if key[pygame.K_UP] and not key[pygame.K_DOWN]:
        player_y_change = -movementSpeed
    if key[pygame.K_DOWN] and not key[pygame.K_UP]:
        player_y_change = movementSpeed
    # if key[pygame.K_r]:







    player_POS_x += player_x_change
    player_POS_y += player_y_change


    #if enemy_x > player_POS_x:
    #    enemy_x_change = -enemySpeed
    #elif enemy_x < player_POS_x:
    #    enemy_x_change = enemySpeed
    #if enemy_y > player_POS_y:
    #    enemy_y_change = -enemySpeed
    #elif enemy_y < player_POS_y:
    #    enemy_y_change = enemySpeed

    #enemy_x += enemy_x_change
    #enemy_y += enemy_y_change


    # Update positions
    enemy.update(dt, player1)
    player1.update(player_x_change,player_y_change)
    player1.checkCollision(wallList, npcList, enemyList,randEnemysList)

    # Draw objects
    gameDisplay.fill(black)
    allSpriteList.draw(gameDisplay)
    # screen.blit(star, (x, y))

    pygame.display.update()
    pygame.display.flip()





pygame.quit()
