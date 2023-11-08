import time

from pygame import *
from random import randint

font.init()

window = display.set_mode((1000, 1000))
display.set_caption("aphex twin versus metaL")

pic = image.load("back.jpg")
picture = transform.scale(image.load("back.jpg"), (1000, 1000))

RED = (201, 32, 32)
GREEN = (0, 233, 50)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 70, 255)
back = DARK_BLUE
window.fill(back)


class Area():
    def __init__(self, x=0, y=0, width=0, height=0, color=None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = font.SysFont('Comic Sans MS', 50).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        hit = sprite.spritecollide(aphex, monster, False)
        if hit:
            pic = image.load("back2.jpg")
            picture = transform.scale(image.load("back2.jpg"), (1000, 1000))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        chekoty = 0
        chekotx = 0

        if chekotx == 0 and chekoty == 0:

            platforms_touchd = sprite.spritecollide(self, barriers, False)
            self.rect.x += self.x_speed
            if self.x_speed > 0:
                if e.key == K_RIGHT or e.key == K_d:
                    for p in platforms_touchd:
                        self.x_speed = 0
                        self.rect.right -= 12
            elif self.x_speed < 0:
                if e.key == K_LEFT or e.key == K_a:
                    for p in platforms_touchd:
                        self.x_speed = 0
                        self.rect.left += 12

            self.rect.y += self.y_speed
            if self.y_speed > 0:
                if e.key == K_UP or e.key == K_w:
                    for p in platforms_touchd:
                        self.y_speed = 0
                        self.rect.top -= 12
            elif self.y_speed < 0:
                if e.key == K_DOWN or e.key == K_s:
                    for p in platforms_touchd:
                        self.y_speed = 0
                        self.rect.bottom -= 12


# razmer player


class Enemy(GameSprite):
    def __init__(self, enemy_image, enemy_x, enemy_y, size_x, size_y, speed):
        GameSprite.__init__(self, enemy_image, enemy_x, enemy_y, size_x, size_y)
        self.speed = speed
        self.direction = 'left'

    def update(self):
        if self.rect.x > 400:
            self.direction = 'right'
        elif self.rect.x < 300:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed


class Bullet(GameSprite):
    def __init__(self, bullet_image, bullet_x, bullet_y, size_x, size_y, speed):
        GameSprite.__init__(self, bullet_image, bullet_x, bullet_y, size_x, size_y)
        self.speed = speed

    def update(self):
        self.speed = self.speed
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()


a = Enemy('enemy.jpg', 5, 100, 80, 80, 5)
monster = sprite.Group()

pew = Bullet('pew.jpg', 115, 115, 115, 115, 115)
pewsprite = sprite.Group()

win_width = 700
win_height = 500

aphex = Player("aphex.jpg", 5, win_height - 180, 180, 180, 0, 0)

final = GameSprite('final.jpg', 600, 400, 80, 80)
run = True


def komnata():
    global w2, w1
    num = randint(1, 3)
    if num == 1:
        w1 = GameSprite("platform2.png", win_width / 2 - win_width / 3, win_height / 4, 300, 50)
        w2 = GameSprite("platform2_v.png", 370, 100, 50, 400)


    elif num == 2:
        w1 = GameSprite("platform2.png", 200, 66, 300, 50)
        w2 = GameSprite("platform2_v.png", 100, 100, 50, 400)

    elif num == 3:
        w1 = GameSprite("platform2.png", 0, 0, 0, 0)
        w2 = GameSprite("platform2_v.png", 0, 0, 0, 0)


komnata()

complete = sprite.collide_rect(aphex, final)
compcount = 0

barriers = sprite.Group()
barriers.add(w1)
barriers.add(w2)
font = font.SysFont('Comic Sans MS', 40)
win = font.render('YOU WIN', True, GREEN)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_LEFT or e.key == K_a:
                aphex.x_speed = -5
            elif e.key == K_RIGHT or e.key == K_d:
                aphex.x_speed = 5
            elif e.key == K_UP or e.key == K_w:
                aphex.y_speed = -5
            elif e.key == K_DOWN or e.key == K_s:
                aphex.y_speed = 5

        elif e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_a:
                aphex.x_speed = 0
            elif e.key == K_RIGHT or e.key == K_d:
                aphex.x_speed = 0
            elif e.key == K_UP or e.key == K_w:
                aphex.y_speed = 0
            elif e.key == K_DOWN or e.key == K_s:
                aphex.y_speed = 0
    window.blit(picture, (0, 0))

    final.reset()
    barriers.draw(window)
    aphex.reset()
    a.reset()

    a.update()
    aphex.update()
    time.delay(50)

    if complete == True:
        window.blit(win, (300, 300))
        if compcount <= 3:
            komnata()
            compcount += 1

        else:
            run = False

    display.update()
