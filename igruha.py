import pygame

pygame.init()
okno = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

x, y = 200, 200
speed = 5
running = True

circles = [(100, 100), (300, 100), (100, 300), (300, 300)]

while running:
    okno.fill((0, 0, 0))
    pygame.draw.rect(okno, (255, 0, 0), (x, y, 40, 40))

    for cx, cy in circles:
        pygame.draw.circle(okno, (255, 255, 0), (cx, cy), 15)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: y -= speed
    if keys[pygame.K_s]: y += speed
    if keys[pygame.K_a]: x -= speed
    if keys[pygame.K_d]: x += speed

    rect = pygame.Rect(x, y, 40, 40)
    circles = [(cx, cy) for (cx, cy) in circles if not rect.collidepoint(cx, cy)]

    clock.tick(60)

pygame.quit()