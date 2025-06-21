from pygame import*
from math import hypot
from random import randint


init()
win = display.set_mode((500, 500))
clock = time.Clock()

a = 1

you = [250, 250, 1, 0]


class Food:
    def __init__ (self, x, y, r, c):
        self.x = x
        self.y = y
        self.radius = r
        self.color = c
    def check_collision(self, player_x, player_y, player_r):
        dx = self.x - player_x
        dy = self.y - player_y
        return hypot(dx, dy) <= self.radius + player_r

eats = [Eat(rendint(-2000, 2000), randint(-2000, 2000), 10,
            (randint(0, 255), randint(0, 255), randint, 0, 255)))
        for _ in  range(300)]



running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    win.fill((255,255,255))


    scale = max(0.3, min(50 / you[2], 1.5))
    draw.circle(win, (you[3],0,0), (250,250), int(you[2]* scale))

    for eat in eats:
        if eat.check_collision
        sx =
        sy =

        draw.circle(win, eat.color, (sx,sy),radius))

    display.update()

    keys = key.get_pressed()
    if keys[K_w]: you[1] -= 5
    if keys[K_s]: you[1] += 5
    if keys[K_a]: you[0] -= 5
    if keys[K_d]: you[0] += 5

    if you[3] != 255:
        you[3] += 3

    if a != 20:
        you[2] += 0.5
        a += 0.5




    clock.tick(60)