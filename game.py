from random import randint
from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, img, width, height, speed, x, y):
        super().__init__()
        self.image = transform.scale( image.load(img), (width, height) )
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        mouse_x, y = mouse.get_pos()
        self.rect.centerx = mouse_x

    def fire(self):
        #laser_sound.play()
        laser = Laser(img='laser.png', width=5, height=100, speed=10,
                               x=player.rect.centerx, y=player.rect.y)
        lasers.add(laser)

class Laser(GameSprite):
    def update(self):
        self.rect.y -= self.speed 

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0, 700)

player = Player(img='player.png',width=100, height=100, speed=5, x=350, y=400)
lasers = sprite.Group()
enemys = sprite.Group()
for i in range(5):
    enemy = Enemy(img='enemy.png', width=100, height=100,
                       speed=randint(1,5), x=randint(0, 700), y=0)
    enemys.add(enemy)

window = display.set_mode( (800,500) )
display.set_caption('Шутер')
background = transform.scale( image.load('background.png'), (800,500) )
clock = time.Clock()

#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()
#laser_sound = mixer.Sound('laser.mp3')

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
        elif some_event.type == MOUSEBUTTONDOWN and some_event.button == BUTTON_LEFT:
            player.fire()

    if sprite.groupcollide(lasers, enemys, True, True):
        enemy = Enemy(img='enemy.png', width=100, height=100,
                       speed=randint(1,5), x=randint(0, 700), y=0)
        enemys.add(enemy)
        
            
    window.blit(background, (0, 0))

    player.show()
    lasers.draw(window)
    enemys.draw(window)

    player.move()
    lasers.update()
    enemys.update()
    
    display.update()
    clock.tick(100)
