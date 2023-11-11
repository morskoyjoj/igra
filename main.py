

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


chasi = time.Clock()
kljglkersjgtlkdfskljgkjlsedrfjklgslkjdefg = 30
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



class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        global e
        chekoty = 0
        chekotx = 0

        if chekotx == 0 and chekoty == 0:

            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            platforms_touchd = sprite.spritecollide(self, barriers, False)
            if platforms_touchd:
                self.rect.x -= self.x_speed
                self.rect.y -= self.y_speed
    def shoot(self):
        global bullet
        bullet = Bullet(self.rect.x + 90, self.rect.y + 90, 19, 19, self.x_speed * 1.4 or self.y_speed * 1.4)
        all_sprites.add(bullet)
        bullets.add(bullet)

# razmer player


class Enemy(GameSprite):
    def __init__(self, enemy_image, enemy_x, enemy_y, size_x, size_y, speed):
        GameSprite.__init__(self, enemy_image, enemy_x, enemy_y, size_x, size_y)
        self.speed = speed
        self.direction = 'left'

    def update(self):
        global ax1, ax2, ay1, ay2
        ax1 = self.speed
        ax2 = self.speed
        ay1 = self.speed
        ay2 =pos
        if self.rect.x > ax1:
            self.rect.x += self.speed
        elif self.rect.x < ax2:
            self.rect.x -= self.speed
        if self.rect.y > ay1:
            self.rect.y += self.speed
        elif self.rect.y < ay2:
            self.rect.y -= self.speed



class Bullet(GameSprite):
    def __init__(self, bullet_x, bullet_y, size_x, size_y, speed):
        GameSprite.__init__(self, "bullet.jpg", bullet_x, bullet_y, size_x, size_y)
        self.speed = speed

    def update(self):
        self.speed = self.speed
        self.rect.x += self.speed
        if self.rect.x > 1000 + 10:
            self.kill()

all_sprites = sprite.Group()


monster = sprite.Group()



bullets = sprite.Group()

aphex = Player("aphex.jpg", 5, 50, 180, 180, 0, 0)
a = Enemy('enemy.jpg', 5, 100, 80, 80, 5)
run = True

pos = aphex.image.get_rect()

def komnata():
    # noinspection PyGlobalUndefined
    global w2, w1, final, aphex, barriers, a
    num = randint(1, 3)
    if num == 1:
        global ax1, ax2,ay1,ay2
        w1 = GameSprite("platform2.png", 253, 414, 80, 586)
        w2 = GameSprite("platform2_v.png", 586, 0, 80, 586)
        final = GameSprite('final.jpg', 765, 100, 80, 80)
        aphex = Player("aphex.jpg", 25, 700, 190, 190, 0, 0)
        a = Enemy('enemy.jpg', 5, 100, 80, 80, 5)
        ax1 = 20
        ax2 = 220
        ay1 = 600
        ay2 = 600

    elif num == 2:

        w1 = GameSprite("platform2.png", 151, 310, 500, 80)
        w2 = GameSprite("platform2_v.png", 151, 620, 500, 80)
        final = GameSprite('final.jpg', 600, 400, 80, 80)
        aphex = Player("aphex.jpg", 25, 25, 190, 190, 0, 0)
        a = Enemy('enemy.jpg', 5, 100, 80, 80, 5)
        ax1 = 20
        ax2 = 220
        ay1 = 600
        ay2 = 600

    elif num == 3:

        w1 = GameSprite("platform2.png", 250, 250, 250, 250)
        w2 = GameSprite("platform2_v.png", 650, 650, 250, 250)
        final = GameSprite('final.jpg', 600, 400, 80, 80)
        aphex = Player("aphex.jpg", 25, 750, 190, 190, 0, 0)
        a = Enemy('enemy.jpg', 5, 100, 80, 80, 5)
        ax1 = 20
        ax2 = 220
        ay1 = 600
        ay2 = 600

    barriers = sprite.Group()
    barriers.add(w1)
    barriers.add(w2)
    all_sprites.empty()

    all_sprites.add(aphex)

    all_sprites.add(a)


komnata()


compcount = 0

count = Label(380, 0, 50, 50, back)
count.set_text("rooms:", 45, RED)
count.draw(20, 20)


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
            if e.key == K_SPACE:
                if aphex.x_speed > 0 or aphex.y_speed > 0 or aphex.x_speed < 0 or aphex.y_speed < 0:
                    aphex.shoot()

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

    if sprite.spritecollide(a, bullets, False):
        a.kill()

    final.reset()
    barriers.draw(window)
    aphex.reset()
    a.reset()

    all_sprites.update()

    all_sprites.draw(window)

    chasi.tick(kljglkersjgtlkdfskljgkjlsedrfjklgslkjdefg)

    complete = sprite.collide_rect(aphex, final)

    if complete:
        window.blit(win, (300, 300))
        if compcount <= 1:
            komnata()
            barriers.draw(window)



            compcount += 1

        else:
            run = False

    display.update()

quit()
