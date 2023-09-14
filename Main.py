import pygame
import random


pygame.init()
win = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()  # A clock to limit the frame rate.

#COLORS
BLACK = (0, 0, 0)
WHITE = (255,255,255)
SQUARECOLOR = (20, 60, 120)
RED = (255,0,0)
# Vel of the player
vel = 7

##POS's
x = 20
y = 30
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


# The player variables have been replaced by a pygame.Rect.
player = pygame.Rect(40, 45, 10, 10)


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

#start the game
run = True
while run:
    # Handle the events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Update the player coordinates.
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= vel
    if keys[pygame.K_RIGHT] and player.x < 1200 - player.width:
        player.x += vel
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= vel
    if keys[pygame.K_DOWN] and player.y < 600 - player.height:
        player.y += vel
    if keys[pygame.K_r]:
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

    if player.colliderect(enemyRect):
        player = pygame.Rect(40, 45, 10, 10)
        print('Game over')
        win.fill(RED)

    # Draw everything.
    win.fill(BLACK)

    ##main char
    pygame.draw.rect(win, SQUARECOLOR, player)

    # Show the image and vilain
    win.blit(image, DEFAULT_IMAGE_POSITION)
    # Use a for loop to draw the wall rects.
    for wall in walls:
        pygame.draw.rect(win, WHITE, wall)
    # Use a for loop to draw the wall rects.
    for enemy in enemys:
        pygame.draw.rect(win, WHITE, enemy)



    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS.

pygame.quit()
