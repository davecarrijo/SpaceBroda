import pygame
import sys
import random
import math
from pygame.locals import *




pygame.display.set_caption('SPACEBRODAR')

#Color definitions
BLUE = (10,10,128)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SQUARECOLOR = (20,60,120)

#Screen width

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400


##POS's
x = 20
y = 30
F_enemy_x = 170
F_Enemy_y = 45

#Rand enemys POS
rand_x = random.randint(20,280)
rand_y = random.randint(20,280)
rand_x_2 = random.randint(20,280)
rand_y_2 = random.randint(20,280)

# # # Load image
man = pygame.image.load('man.png')
man = pygame.transform.scale(man, (200, 200))
image = pygame.image.load('man.png')
# Set the size for the image
DEFAULT_IMAGE_SIZE = (35, 60)
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)
enemyRect = image.get_rect(topleft = DEFAULT_IMAGE_POSITION )


# The walls are now pygame.Rects as well. Just put them into a list.
walls = [
    pygame.Rect(0, 0, 1200, 5),
    pygame.Rect(0, 0, 5, 600),
    pygame.Rect(0, 295, 1200, 5),
    pygame.Rect(295, 0, 5, 600),
    ]
enemys  = [
    pygame.Rect(rand_x, rand_y, 10, 10),
    pygame.Rect(rand_x_2, rand_y_2, 10, 10),
    pygame.Rect(170, rand_y_2, 10, 10),
    pygame.Rect(50, rand_y_2, 10, 10),
    ]

# The player variables have been replaced by a pygame.Rect.
player1 = pygame.Rect(40, 45, 10, 10)
FolowerEnemy = pygame.Rect(F_enemy_x, F_Enemy_y, 10, 10)

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.score = 0

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x


        block_hit_list = pygame.sprite.spritecollide(self,self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self,self.walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Player2(pygame.sprite.Sprite):
    def __init__(self,x,y,human):
        super().__init__()
        self.human = human
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.score = 0

        self.rect.x = 400
        self.rect.y = 40

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y

    def update(self):
        if self.human.rect.x > self.rect.x :
            self.rect.x += 1
        if self.human.rect.x < self.rect.x :
            self.rect.x -= 1
        if self.human.rect.y > self.rect.y :
            self.rect.y += 1
        if self.human.rect.y < self.rect.y :
            self.rect.y -= 1





class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



#Wall init

wall_list = pygame.sprite.Group()

#Pygame definitions

win = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# pygame.display.set_caption('test!')
all_sprite_list = pygame.sprite.Group()





#Left wall
wall = Wall(0,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)
#top wall
wall = Wall(10,0,790,10)
wall_list.add(wall)
all_sprite_list.add(wall)

#Right wall
wall = Wall (790,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

#Bottom wall
wall = Wall (0,590,1000,300)
wall_list.add(wall)
all_sprite_list.add(wall)

enemies = [
    Player(50,50),
    Player(10,10),
    Player(10,50),
]

#Create the player
player = Player(50,50)
all_sprite_list.add(player)
player.walls = wall_list

player2 = Player2(50,50, player)
all_sprite_list.add(player2)
player2.walls = wall_list


clock = pygame.time.Clock()

#?Loop
pygame.init()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(3,0)
            elif event.key == pygame.K_w:
                player.changespeed(0,-3)
            elif event.key == pygame.K_s:
                player.changespeed(0,3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3,0)
            elif event.key == pygame.K_d:
                player.changespeed(-3,0)
            elif event.key == pygame.K_w:
                player.changespeed(0,3)
            elif event.key == pygame.K_s:
                player.changespeed(0,-3)

        # Game logic.
        for enemy in enemys:
                # Check if the player rect collides with a enemy rect.
                if player1.colliderect(enemy):
                    player1 = pygame.Rect(40, 45, 10, 10)
                    print('Game over')
                    # Then quit or restart.

        if player1.colliderect(enemyRect):
            player1 = pygame.Rect(40, 45, 10, 10)
            print('Game over')
            win.fill(RED)




        # ##main char
        # pygame.draw.rect(win, SQUARECOLOR, player)
        # # Show the image and vilain
        # pygame.draw.rect(win, RED, FolowerEnemy)

        # # Use a for loop to draw the wall rects.
        # for wall in walls:
        #     pygame.draw.rect(win, WHITE, wall)
        # # Use a for loop to draw the wall rects.
        # for enemy in enemys:
        #     pygame.draw.rect(win, WHITE, enemy)


    win.blit(image, DEFAULT_IMAGE_POSITION)

    win.fill(BLACK)
    all_sprite_list.draw(win)
    all_sprite_list.update()



    pygame.display.flip()
    clock.tick(60)





pygame.quit()