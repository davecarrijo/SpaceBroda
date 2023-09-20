import pygame
import random
import math
from pygame.locals import *

#COLORS
BLUE = (10,10,128)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SQUARECOLOR = (20,60,120)

#Screen width
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# Vel of the player,game
PlayerSpeed = 8
EnemySpeed = 5

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


pygame.init()
win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()  # A clock to limit the frame rate.


<<<<<<< HEAD
man_png = pygame.image.load("man.png").convert()
man = man_png.get_rect()
# Load image
=======
# # # Load image
man = pygame.image.load('man.png')
man = pygame.transform.scale(man, (200, 200))
>>>>>>> e00d5801438c2d4fceb1eb6373ca99e580e77a9f
image = pygame.image.load('man.png')
# Set the size for the image
DEFAULT_IMAGE_SIZE = (35, 60)
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)
enemyRect = image.get_rect(topleft = DEFAULT_IMAGE_POSITION )


# The player variables have been replaced by a pygame.Rect.
player = pygame.Rect(40, 45, 10, 10)
FolowerEnemy = pygame.Rect(F_enemy_x, F_Enemy_y, 10, 10)


# !
class Tile(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = GREEN
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=position)

    def change_color(self, color):
        self.color = color
        self.image.fill(self.color)

def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    # Create the tiles and add them to the all_sprites group.
    for y in range(10):
        for x in range(12):
            all_sprites.add(Tile((x*51, y*51)))
# !

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

#?Loop
#start the game
run = True
while run:
    # Handle the events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the player coordinates.
    keys = pygame.key.get_pressed()pull
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PlayerSpeed
    elif keys[pygame.K_RIGHT] and player.x < 1200 - player.width:
        player.x += PlayerSpeed
    elif keys[pygame.K_UP] and player.y > 0:
        player.y -= PlayerSpeed
    elif keys[pygame.K_DOWN] and player.y < 600 - player.height:
        player.y += PlayerSpeed
    elif keys[pygame.K_r]:
        player = pygame.Rect(40, 45, 30, 30)


    # Game logic.
    for wall in walls:
        # Check if the player rect collides with a wall rect.
        if player.colliderect(wall):
            player = pygame.Rect(40, 45, 10, 10)
            print('Game over')
            # Then quit or restart.
    # Game logic.
    for enemy in enemys:
        # Check if the player rect collides with a enemy rect.
        if player.colliderect(enemy):
            player = pygame.Rect(40, 45, 10, 10)
            print('Game over')
            # Then quit or restart.

<<<<<<< HEAD
        if player.Rect() == man.Rect() :
            player = pygame.Rect(40, 45, 10, 10)
            print('Game over')


    # Draw everything.
    win.fill(BLACK)
    pygame.draw.rect(win, SQUARECOLOR, player)
=======
    if player.colliderect(enemyRect):
        player = pygame.Rect(40, 45, 10, 10)
        print('Game over')
        win.fill(RED)



    ##main char
    pygame.draw.rect(win, SQUARECOLOR, player)
    # Show the image and vilain
    pygame.draw.rect(win, RED, FolowerEnemy)
>>>>>>> e00d5801438c2d4fceb1eb6373ca99e580e77a9f


    win.blit(image, DEFAULT_IMAGE_POSITION)
    # Use a for loop to draw the wall rects.
    for wall in walls:
        pygame.draw.rect(win, WHITE, wall)
    # Use a for loop to draw the wall rects.
    for enemy in enemys:
        pygame.draw.rect(win, WHITE, enemy)

<<<<<<< HEAD
=======

>>>>>>> e00d5801438c2d4fceb1eb6373ca99e580e77a9f
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS.

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()