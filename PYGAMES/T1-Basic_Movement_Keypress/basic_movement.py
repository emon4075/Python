import pygame

pygame.init()

window = pygame.display.set_mode((430, 630))
pygame.display.set_caption("Circle Moving Game")

position_X = 50
position_Y = 50

width = 30
height = 30
velocity = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        position_X -= velocity

    if keys[pygame.K_RIGHT]:
        position_X += velocity

    if keys[pygame.K_DOWN]:
        position_Y += velocity

    if keys[pygame.K_UP]:
        position_Y -= velocity

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (147, 230, 230), (position_X, position_Y), 30.0, 30)
    pygame.display.update()
pygame.quit()
