#Создай собственный Шутер!
from random import randint 
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

propusk = 0 
ybit = 0 
ball_r = 10
ball_speed = 6 
ball_d = 10*2

ball_start_x = screen_x/2 - ball_r







packman = Player(img_hero, 5, 500 - 350, 20 ,150, 2 )
packman1 = Player(img_hero, 675, 500 - 350, 20 ,150, 2 )



bullets = sprite.Group()


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
          packman1.update1()


          bullets.update()
          bullets.draw(window )   





     #clock.tick(FPS)
     #print(clock.get_fps())
     #обновление экрана 
     display.update()
