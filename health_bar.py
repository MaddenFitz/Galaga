import pygame
import constants as c


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(HealthBar, self).__init__()
        self.max_hp = hp
        self.hp = self.max_hp
        self.original_image = pygame.image.load('health_bar.png').convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * 5), int(self.original_image.get_height() * 1.5)))
        self.max_width = self.image.get_width()
        self.rect = self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        
    def update(self):
        self.rect.x += self.vel_x 
        self.rect.y += self.vel_y
    
    def decrease_hp_value(self):
        self.hp -= 1
        self.image = pygame.transform.scale(self.original_image, (self.max_width * self.hp // self.max_hp, self.rect.height))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset_health_to_max(self):
        self.hp = self.max_hp
        self.image = pygame.transform.scale(self.original_image, (self.max_width * self.hp // self.max_hp, self.rect.height))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y