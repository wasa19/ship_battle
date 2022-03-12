import pygame as pg
from random import randint, randrange
from os import path

FPS = 50
W = 1000
H = 700

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
pg.font.init()
pg.init()
pg.mixer.init()
sc = pg.display.set_mode((W,H))
font = pg.font.Font(None, 22)
gun_image = pg.image.load(path.join(img_dir, '23-tank-png-image-armored-tank.png')).convert()
ship_image = pg.image.load(path.join(img_dir, 'ship_1.png')).convert()
bullet_image = pg.image.load(path.join(img_dir, '—Pngtree—flying small rocket_966387.png')).convert()
bomb_image = pg.image.load(path.join(img_dir, '2cd43b_e5fa541475f6445f952b947a991991e4_mv2.png')).convert()
sh_gun_snd = pg.mixer.Sound(path.join(snd_dir, 'Laser_Shoot3.wav'))
sh_sh_snd = pg.mixer.Sound(path.join(snd_dir, 'Hit_Hurt.wav'))
hit_snd = pg.mixer.Sound(path.join(snd_dir, 'Explosion9.wav'))
pg.mixer.music.load(path.join(snd_dir, 'airship (online-audio-converter.com).wav'))
pg.mixer.music.set_volume(0.3)
sea_sc = pg.Surface((W,H/2))
road_sc = pg.Surface((W,H/5.5))
pg.display.set_caption('Ship Battle')
clock = pg.time.Clock()

#def draw_text(surf, )

def show_go_screen():
    sc.fill('#F4A460')
    font = pg.font.Font(None, 70)
    text_name = font.render('Ship Battle', True, 'black')
    text_name_place = text_name.get_rect(midtop = (W/2, H/4))
    text_opt = font.render('arrows to move, space to fire', True, 'white')
    text_opt_place = text_opt.get_rect(midtop =(W/2, H/2))
    text_pts = font.render('your points:' + str(count), True, 'red')
    text_pts_place = text_pts.get_rect(midtop = (W/2, H*0.8))
    sc.blit(text_name, text_name_place)
    sc.blit(text_opt, text_opt_place)
    sc.blit(text_pts, text_pts_place)
    pg.display.flip()
    wating = True
    while wating:
        clock.tick(FPS)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
            if i.type == pg.KEYUP:
                wating = False

class Gun(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(gun_image, (90, 40))
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect()
        self.rect.centerx = W / 2
        self.rect.bottom = H - 80
        self.dx_set = 0

    def update(self):
        self.dx_set = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left >= 0:
            self.dx_set = -3
        if keys[pg.K_RIGHT] and self.rect.right <= W:
            self.dx_set = 3
        self.rect.x += self.dx_set

    def shoot(self):
        if len(bullets) == 0:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            sh_gun_snd.play()


class Ship(pg.sprite.Sprite):
    def __init__(self, y, ship_speed):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(ship_image, (60, 20))
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
        self.rect.x = randrange(W - self.rect.width)
        self.rect.y = y
        self.ship_speed = ship_speed

    def update(self):
        self.rect.x += self.ship_speed
        if self.rect.left <= 0 or self.rect.right >= W:
            self.ship_speed = -self.ship_speed
        bomb_place = randrange(W - 100)
        if bomb_place < self.rect.x < (bomb_place + 7):
            bomb = Bomb(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bomb)
            bombs.add(bomb)
            sh_sh_snd.play()


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(bullet_image, (20, 20))
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.bullet_speed = -7

    def update(self):
        self.rect.y += self.bullet_speed
        if self.rect.bottom < 0:
            self.kill()


class Bomb(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(bomb_image, (18, 18))
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.bomb_speed = 3

    def update(self):
        self.rect.y += self.bomb_speed
        if self.rect.top >= H:
            self.kill()


all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
bullets = pg.sprite.Group()
bombs = pg.sprite.Group()
gun = Gun()
all_sprites.add(gun)
ship_1 = Ship((H/2-50), 1)
ship_2 = Ship((H/2-140), -2)
ship_3 = Ship((H/2-250), 3)
all_sprites.add(ship_1, ship_2, ship_3)
mobs.add(ship_1, ship_2, ship_3)
count = 0
lives = 3
pg.mixer.music.play(loops = -1)

running = True
game_over = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pg.sprite.Group()
        mobs = pg.sprite.Group()
        bullets = pg.sprite.Group()
        bombs = pg.sprite.Group()
        gun = Gun()
        all_sprites.add(gun)
        ship_1 = Ship((H/2-50), 1)
        ship_2 = Ship((H/2-140), -2)
        ship_3 = Ship((H/2-250), 3)
        all_sprites.add(ship_1, ship_2, ship_3)
        mobs.add(ship_1, ship_2, ship_3)
        count = 0
        lives = 3
    clock.tick(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_SPACE:
                gun.shoot()

    all_sprites.update()

    hits = pg.sprite.groupcollide(mobs, bullets, False, True)
    for hit in hits:
        hit_snd.play()
        pg.time.delay(300)
        if hit.rect.y == 100:
            count += 5
        elif hit.rect.y == 210:
            count += 2
        elif hit.rect.y == 300:
            count += 1

    bomb_in = pg.sprite.spritecollide(gun, bombs, True)
    for i in bomb_in:
        pg.time.delay(300) # TODO health bar
        lives -= 1
    if lives == 0:
        game_over = True

    sc.fill('#F4A460')
    sea_sc.fill('#00FFFF')
    sc.blit(sea_sc, (0,30))
    road_sc.fill('black')
    sc.blit(road_sc, (0, 550))

    all_sprites.draw(sc)
    text_scr = font.render('pts: ' + str(count), True, 'yellow')
    text_place_scr = text_scr.get_rect(midbottom = (40, H-40))
    text_lv = font.render('lives: ' + str(lives), True, 'red')
    text_place_lv = text_lv.get_rect(midbottom = (W-100, H-40))
    sc.blit(text_scr, text_place_scr)
    sc.blit(text_lv, text_place_lv)
    pg.display.flip()

pg.quit()