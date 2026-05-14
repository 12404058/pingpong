from pygame import *
from random import randint
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()#прямоугольник
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed


white = (255,255,255)

window = display.set_mode((700,500))
display.set_caption('ping-pong')
window.fill(white)

pl1 = Player('platform_l.jpg',10,40,0,100,200)
pl2 = Player('platform_r.jpg',10,570,0,100,200)


clock = time.Clock()        #отслеживает частоту кадров в секунду
FPS = 60            

run = True

while run == True:
    for event1 in event.get(): #перебераем очередь событий
        if event1.type == QUIT: #проверка на закрытие окна
            run = False
    pl1.reset()
    pl1.update_l()
    pl2.reset()
    pl2.update_r()

    display.update()
    clock.tick(FPS)
