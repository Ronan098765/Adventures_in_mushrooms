from pygame import *



font.init()
font2 = font.SysFont('Arial', 36)

win = font2.render('You win', True, (0, 200, 200))
lose = font2.render('You lose', True, (180, 0, 0))

img_back = 'Fon.jpg'
img_bul_R = 'Bullet_R.png'
img_player = 'Player.png'
img_bul_L = 'Bullet_L.png'

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
        if keys[K_a] and self.rect.x > 70:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 70:
            self.rect.x += self.speed

win_width = 700
win_height = 500
display.set_caption('Game')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

loh = Player(img_player, 350, 250, 70, 70, 10)


finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




    if not finish:
        window.blit(background,(0, 0))
       
        loh.reset()
        loh.update()







        display.update()

    time.delay(60)








    


    


































