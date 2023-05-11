from pygame import *
from random import randint
from time import time as timer

mixer.init()
mixer.music.load('Music_fon.mp3')
mixer.music.play()
mixer.music.stop()
pick_money = mixer.Sound('Pick_money.ogg')
music_win = mixer.Sound('Music_win.ogg')
music_lose = mixer.Sound('Music_lose.ogg')
pick_mush = mixer.Sound('Pick_mush.ogg')
pick_mush_evil = mixer.Sound('Pick_mush_evil.ogg')
font.init()
font2 = font.SysFont('Arial', 36)
#Бабушкины яблоки
win = font2.render('You win', True, (30, 89, 69))
#Бургундский
lose = font2.render('You lose', True, (144, 0,32 ))

img_mush_evil = 'Mush_evil.png'
img_mush = 'Mushroom.png'
img_back = 'Fon.jpg'
img_bul_R = 'Bullet_R.png'
img_player = 'Player.png'
img_bul_L = 'Bullet_L.png'
img_money = 'Money.png'
money_num = 0
heart_loh = 10

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 70:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global bullets_num
        if self.rect.x < 0:
            self.kill()
            bullet = Bullet(img_bul_L, 700, randint(50, win_height - 50), 30, 10, randint(5,15))
            bullets.add(bullet)

class Bullet_r(GameSprite):
    def update(self):
        self.rect.x += self.speed
        global bullets_num
        if self.rect.x > 700:
            self.kill()
            bullet_r = Bullet_r(img_bul_R, 0, randint(50, win_height - 50), 30, 10, randint(5,15))
            bullets_r.add(bullet_r)  

class Money(GameSprite):
    def update(self):
        pass

class Mushroom(GameSprite):
    def update(self):
        pass

win_width = 700
win_height = 500
display.set_caption('Game')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

loh = Player(img_player, 350, 250, 60, 80, 10)

bullets = sprite.Group()
bullets_r = sprite.Group()
moneys = sprite.Group()

for i in range(1, 6):
    bullet = Bullet(img_bul_L, 700, randint(50, win_height - 50), 30, 10, randint(5,15))
    bullets.add(bullet)
for i in range(1, 6):
    bullet_r = Bullet_r(img_bul_R, 0, randint(50, win_height - 50), 30, 10, randint(5,15))
    bullets_r.add(bullet_r) 

for i in range(0, 7):
    money_loh = Money(img_money, randint(50, win_width - 50), randint(50, win_height - 50), 50, 50, 0)
    moneys.add(money_loh)

mushroom = Mushroom(img_mush, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)
mush_evil = Mushroom(img_mush_evil, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)
finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(loh, mushroom):
        pick_mush.play()
        heart_loh += 1
        mushroom.kill()
        mushroom = Mushroom(img_mush, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)

    if sprite.collide_rect(loh, mush_evil):
        pick_mush_evil.play()
        heart_loh -= 1
        mush_evil.kill()
        mush_evil = Mushroom(img_mush_evil, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)

    if not finish:
        window.blit(background,(0, 0))
        score = font2.render('Score:' + str(money_num), 1, (255, 255, 255))
        window.blit(score, (10, 10))
        hearts_loh = font2.render('Hp:' + str(heart_loh), 1, (168, 228, 160))
        window.blit(hearts_loh, (630, 10))

        if sprite.spritecollide(loh, moneys, True):
            money_num += 1 
            pick_money.play()
            money_loh = Money(img_money, randint(50, win_width - 50), randint(50, win_height - 50), 50, 50, 0)
            moneys.add(money_loh)
            
        if sprite.spritecollide(loh, bullets, True) or sprite.spritecollide(loh, bullets_r, True):
            heart_loh -= 1

        if heart_loh <= 0:
            finish = True
            window.blit(lose, (290, 220))
            music_lose.play()

        if money_num >= 20:
            finish = True
            window.blit(win, (290, 220))
            music_win.play()
        
        loh.update()
        loh.reset()
        bullets.update()
        bullets_r.update()
        bullets_r.draw(window)
        bullets.draw(window)
        moneys.draw(window)
        mushroom.reset()
        mush_evil.reset()
        display.update()
    time.delay(60)