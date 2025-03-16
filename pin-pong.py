from pygame import *
from random import randint
image_ping_pong = transform.scale(image.load('i.webp'),(700,500))
window = display.set_mode((700,500))
window.blit(image_ping_pong,(0,0))
display.set_caption('ping-pong')

class GameSprite (sprite.Sprite):
    def __init__(self,image_name,x,y,speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if self.rect.y < 450 :
            if keys_pressed[K_UP]:
                self.rect.y+= self.speed
        if self.rect.x >= 0 :
            if keys_pressed[K_DOWN]:
                self.rect.y -= self.speed

class Player2(GameSprite):    
    def __init__(self,image_name,x,y,speed,w,h):
        super().__init__(image_name,x,y,speed,w,h)
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

sosiska1_right = Player('sosiska1.webp',100,250,10,100,80)
sosiska2_left = Player('sosiska2.jpg',600,250,10,100,80)
bulochka = Player2('bulochka.webp',350,250,15,130,80)

clock = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    sosiska1_right.reset()
    sosiska2_left.reset()
    bulochka.reset()
    sosiska1_right.update() 
    sosiska2_left.update() 
    bulochka.update() 
    clock.tick(60)
    display.update()