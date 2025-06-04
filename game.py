from pygame import * 

window = display.set_mode( (800,500) )
display.set_caption('Шутер')
background = transform.scale( image.load('background.png'), (800,500) )

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    window.blit(background, (0, 0))

    display.update()
