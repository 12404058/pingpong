from pygame import *
from random import randint
font.init()
font1 = font.Font(None,35)


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

pl1 = Player('platform_l.png',10,40,0,50,200)
pl2 = Player('platform_r.png',10,595,0,50,200)
ball = GameSprite('tennis_ball.png',3,315,230,50,50)


clock = time.Clock()        #отслеживает частоту кадров в секунду
FPS = 60            


speed_x = 3
speed_y = 3

score1 = 0
score2 = 0
max_score = 3
match_over = False

finish = False
run = True

score_text = font1.render(str(score1)+ ' : ' + str(score2),True,(0,0,0))

while run == True:
    for event1 in event.get(): #перебераем очередь событий
        if event1.type == QUIT: #проверка на закрытие окна
            run = False
    window.fill(white)
    pl1.reset()
    pl1.update_l()
    pl2.reset()
    pl2.update_r()
    ball.reset()

    if finish != True:
        window.blit(score_text,(310,220))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 450 or ball.rect.y <0:
        speed_y *= -1
    if sprite.collide_rect(pl1, ball) or sprite.collide_rect(pl2, ball):
        speed_x *= -1.01



    display.update()
    clock.tick(FPS)
