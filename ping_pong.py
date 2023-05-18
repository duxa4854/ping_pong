#Создай собственный Шутер!
from random import randint
from turtle import window_height 
from pygame import *
#парпметры окно 
display.set_caption("SpaceWar")
img_back = "galaxy.jpg" 
img_hero = "rocket.png"
img_enemy = "bullet.png" 

#img_bullet = "bullet.png"
window = display.set_mode((700, 500))
background = transform.scale(image.load(img_back), (700, 500))

#класс GameSprite
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
          sprite.Sprite.__init__(self)
          self.image = transform.scale(image.load(player_image), (size_x, size_y))
          self.speed = player_speed
          self.rect = self.image.get_rect()
          self.rect.x = player_x
          self.rect.y = player_y
     def reset(self):
          window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
     def update(self):
          keys = key.get_pressed()
          if keys[K_w] and self.rect.y > 10:
               self.rect.y -= self.speed
          if keys[K_s] and self.rect.y < 420:
               self.rect.y += self.speed
     def update1(self):
          keys = key.get_pressed()
          if keys[K_UP] and self.rect.y > 10:
               self.rect.y -= self.speed
          if keys[K_DOWN] and self.rect.y < 420:
               self.rect.y += self.speed

speed_x =  1
speed_y = 1

packman = Player(img_hero, 5, 500 - 350, 20 ,150, 2 )
packman1 = Player(img_hero, 675, 500 - 350, 20 ,150, 2 )
packman2 = Player(img_hero, 0, 500 - 550, 1 ,550, 2 )
packman3 = Player(img_hero, 2, 500 - 1, 690 ,1, 2 )
packman4 = Player(img_hero, 699, 10 - 10, 1 ,800, 2 )
packman5 = Player(img_hero, 1, 1 - 1, 1000 ,1, 2 )

ball = GameSprite(img_enemy,100,100 ,30,30,1)

#настройка частоты кадров 
clock = time.Clock()
FPS=120

#пожилой цикл 
game = True
finish = False
while game:

     for e in event.get():
          if e.type == QUIT:
               game = False 
          elif e.type == KEYDOWN:
               if e.key == K_SPACE:
                    pass
                    
     if finish != True:
          window.blit(background,(0,0))
          #спрайты
          
          packman.reset()
          packman.update()
          packman1.reset()
          packman2.reset()
          packman3.reset()
          packman4.reset()
          packman5.reset()

          packman1.update1()
          ball.reset()
          

          ball.rect.x += speed_x
          ball.rect.y += speed_y
 
     if ball.rect.y > 500 or ball.rect.y < 0:
          speed_y *= -1
     if sprite.collide_rect(packman,ball) or sprite.collide_rect(packman1,ball) or sprite.collide_rect(packman2,ball) or sprite.collide_rect(packman3,ball) or sprite.collide_rect(packman4,ball) or sprite.collide_rect(packman5,ball):
          speed_x *= -1

     #clock.tick(FPS)
     #print(clock.get_fps())
     #обновление экрана 
     display.update()
