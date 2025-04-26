import pygame as pg
pg.init()
from time import time as tm

def get_events():
    global run
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_w:
                player_1.speed = -5
            if e.key == pg.K_s:
                player_1.speed = 5
            if e.key == pg.K_UP:
                player_2.speed = -5
            if e.key == pg.K_DOWN:
                player_2.speed = 5
        if e.type == pg.KEYUP:
            if e.key == pg.K_w:
                player_1.speed = 0
            if e.key == pg.K_s:
                player_1.speed = 0
            if e.key == pg.K_UP:
                player_2.speed = 0
            if e.key == pg.K_DOWN:
                player_2.speed = 0

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image,  x, y, w, h, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        self.rect.y += self.speed

class Ball(GameSprite):
    def init(self):
        self.speed_x = self.speed
        self.speed_y = self.speed
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 520:
            self.speed_y *= -1
        if self.rect.colliderect(player_1.rect) or self.rect.colliderect(player_2.rect):
            self.speed_x *= -1

win = pg.display.set_mode((1200,600))
pg.display.set_caption('PingPong')
win.fill((20, 184, 184))

run = True
finish = False
clock = pg.time.Clock()
start_game = False

player_1 = Player('pp_left.png', 20, 200, 50, 50, 0)
player_2 = Player('pp_right.png', 1080, 200, 50, 50, 0)
ball = Ball('ppball.png', 560, 220, 80, 80, 5)
ball.init()
label = pg.font.SysFont('verdana', 65)

start = tm()
while run:
    get_events()
    if not finish:
        end = tm()
        if end - start > 3:
            start_game = True
        win.fill((152,235,187))
        player_1.move()
        player_1.update()
        player_2.move()
        player_2.update()
        if start_game:
            ball.move()
            ball.update()
        if ball.rect.x < 5:
            res = "Player 1 lose"
            finish = True
        if ball.rect.x > 1115:
            res = "Player 2 lose"
            finish = True
    else:
        label = pg.font.SysFont('verdana', 65).render(res, True, (253,254,255))
        win.blit(label, (200, 200))
    pg.display.update()
    clock.tick(60)