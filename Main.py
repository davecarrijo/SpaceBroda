import pygame


pygame.init()
win = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()  # A clock to limit the frame rate.
BLACK = (0, 0, 0)
WHITE = (255,255,255)
SQUARECOLOR = (20, 60, 120)
x = 20
y = 30


man = pygame.image.load('man.png')
man = pygame.transform.scale(man, (200, 200))


# The player variables have been replaced by a pygame.Rect.
player = pygame.Rect(40, 45, 10, 10)
vel = 7
# The walls are now pygame.Rects as well. Just put them into a list.
walls = [
    pygame.Rect(0, 0, 1200, 5),
    pygame.Rect(0, 0, 5, 600),
    pygame.Rect(0, 295, 1200, 5),
    pygame.Rect(295, 0, 5, 600),
    ]

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

    # Draw everything.
    win.fill(BLACK)
    pygame.draw.rect(win, SQUARECOLOR, player,)
    rect = man.get_rect()
    rect = rect.move((x, y))

    # Use a for loop to draw the wall rects.
    for wall in walls:
        pygame.draw.rect(win, WHITE, wall)

    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS.

pygame.quit()