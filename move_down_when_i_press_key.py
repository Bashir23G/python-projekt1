import pygame
import sys
# initialize Pygame
pygame.init()

# set the screen dimensions
screen_width = 800
screen_height = 600

# create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# set the initial position of the mouse
mouse_x = screen_width / 2
mouse_y = screen_height / 2

# set the movement speed of the mouse
mouse_speed = 5

# create a boolean flag to track whether the "g" key is held down
g_key_down = False

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # exit the game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                # set the "g" key flag to True
                g_key_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_g:
                # set the "g" key flag to False
                g_key_down = False

    # update the mouse position if the "g" key is held down
    if g_key_down:
        mouse_y += mouse_speed

    # draw the screen
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(mouse_x), int(mouse_y)), 10)
    pygame.display.update()

    # limit the frame rate to 60 FPS
    pygame.time.Clock().tick(60)