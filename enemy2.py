import pygame
import constants as c 
import random
from bullet import Bullet

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.img_explosion_01 = pygame.image.load('Explosion_01.png').convert()
        self.img_explosion_01 = pygame.transform.scale(self.img_explosion_01, (self.img_explosion_01.get_width()*2, self.img_explosion_01.get_height()*2))
        
        self.img_explosion_02 = pygame.image.load('Explosion_02.png').convert()
        self.img_explosion_02 = pygame.transform.scale(self.img_explosion_02, (self.img_explosion_02.get_width()*2, self.img_explosion_02.get_height()*2))

        
        self.img_explosion_03 = pygame.image.load('Explosion_03.png').convert()
        self.img_explosion_03 = pygame.transform.scale(self.img_explosion_03, (self.img_explosion_03.get_width()*2, self.img_explosion_03.get_height()*2))
        
        
        self.img_explosion_04 = pygame.image.load('Explosion_04.png').convert()
        self.img_explosion_04 = pygame.transform.scale(self.img_explosion_04, (self.img_explosion_04.get_width()*2, self.img_explosion_04.get_height()*2))
        
        
        self.img_explosion_05 = pygame.image.load('Explosion_05.png').convert()
        self.img_explosion_05 = pygame.transform.scale(self.img_explosion_05, (self.img_explosion_05.get_width()*2, self.img_explosion_05.get_height()*2))

        self.anim_explosion = [self.img_explosion_01, self.img_explosion_02, self.img_explosion_03, self.img_explosion_04, self.img_explosion_05]
        
        
        self.anim_index = 0
        self.frame_length_max = 8
        self.frame_length = self.frame_length_max
        
        #loads the picture into the 'image' object and put the image to the screen with convert_alpha
        self.image = pygame.image.load('Red Ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.is_destroyed = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 3
        self.bullets = pygame.sprite.Group()
        self.bullet_timer_max = 60
        self.bullet_timer = self.bullet_timer_max
        self.states = {'FLY_DOWN': 'FLY_DOWN',
                        'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3, 4)
        
    def update(self):
        self.bullets.update()
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        elif self.state == 'ATTACK':
                self.state_attack()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.is_destroyed:
            max_index = len(self.anim_explosion) - 1
            if self.frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.kill()
                else:
                    self.image = self.anim_explosion[self.anim_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1
            
    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= -50:
            self.state = self.states['ATTACK']
            self.init_states = True
    
    def state_attack(self):
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = random.randrange(-4, 4)
            self.init_state = False
        if self.bullet_timer == 0:
            self.shoot()
            self.bullet_timer = self.bullet_timer_max
        else:
            self.bullet_timer -= 1
        if self.rect.x <= 0:
            self.vel_x *= -1
        elif self.rect.x + self.rect.width >= c.DISPLAY_WIDTH:
            self.vel_x *= 1
            
    def shoot(self):
        new_bullet = Bullet()
        new_bullet.vel_y = 5
        new_bullet.rect.x = self.rect.x + (self.rect.width - 55 // 2)
        new_bullet.rect.y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)

    def get_hit(self):
        if not self.is_invincible:
            self.hp -= 1
            if self.hp <= 0:
                self.is_destroyed = True
                self.is_invincible = True
                self.vel_y = 0
                self.vel_x = 0
                self.rect.x = self.rect.x - 100
                self.rect.y = self.rect.y - 100
                self.image = self.anim_explosion[self.anim_index]
            else:
                pass