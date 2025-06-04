from pygame import * 

class GameSprite():
    def __init__(self, img, width, height, speed, x, y):
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

player = Player(img='player.png',width=100, height=100, speed=5, x=350, y=400)

window = display.set_mode( (800,500) )
display.set_caption('Шутер')
background = transform.scale( image.load('background.png'), (800,500) )
clock = time.Clock()

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
        elif some_event.type == MOUSEBUTTONDOWN and some_event.button == BUTTON_LEFT:
            print('выстрел')

    window.blit(background, (0, 0))
    player.show()

    player.move()
    
    display.update()
    clock.tick(100)
