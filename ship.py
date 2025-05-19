import pygame
import constants as c
from bullet import Bullet
from hud import Hud

#setting up the ship
#importing the ship
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        #loads the picture into the 'image' object and put the image to the screen with convert_alpha
        self.image = pygame.image.load('Ship.png').convert_alpha()
        #scaling image by 1.5
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.hp = 3
        self.max_hp = 3
        self.lives = 3
        self.hp = self.max_hp
        self.hud = Hud(self.hp, self.lives)
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2.5
        self.is_alive = True
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.is_invincible = False
        self.max_invincible_timer = 60
        self.invincible_timer = 0
        self.bullets = pygame.sprite.Group()
        #setting speeds
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5

        # Optional: Keep the ship within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > c.DISPLAY_WIDTH:
            self.rect.right = c.DISPLAY_WIDTH

    #grab position and adds velocity
    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.x + self.vel_x:
            self.rect.x = 250
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
       
        # Check for Invincibility
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
        else:
            self.is_invincible = False
        print(self.is_invincible)    
            
    def shoot(self):
        if self.is_alive:
            new_bullet = Bullet()
            new_bullet.rect = Bullet()
            new_bullet.vel_x = 0
            new_bullet.vel_y = -8
            #this sets the same location of the bullet to the location of the ship
            new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 4
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet)
        
    def get_hit(self):
        if self.is_alive:
            self.hp -= 1
            self.hud.health_bar.decrease_hp_value()
            if self.hp <= 0:
                self.hp = 0
                self.death()
            print(f'HP: {self.hp}')
    
    def death(self):
        self.lives -= 1
        print(f'HP: {self.hp}')
        if self.lives <= 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()
        self.hud.lives.decrement_life()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.is_invincible = True
        self.is_invincible_timer = self.max_invincible_timer