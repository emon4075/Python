import pygame

pygame.init()

window = pygame.display.set_mode((430, 630))
pygame.display.set_caption("Rectangle Moving Game")

positionX = 100
positionY = 200

width = 30
height = 30
velocity = 10

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and positionX > velocity:
        positionX -= velocity

    if keys[pygame.K_RIGHT] and positionX < 430 - width - velocity:
        positionX += velocity
    if not (isJump):
        if keys[pygame.K_DOWN] and positionY < 630 - height - velocity:
            positionY += velocity

        if keys[pygame.K_UP] and positionY > velocity:
            positionY -= velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            positionY -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(
        window, (215, 111, 12), (positionX, positionY, width, height), 0, 15
    )
    pygame.display.update()

pygame.quit()
