import pygame
import constants as c
import random


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self,).__init__()
        self.planet_01 = pygame.image.load('planet_01.png').convert()
        self.planet_02 = pygame.image.load('planet_02.png').convert()
        self.planet_03 = pygame.image.load('planet_03.png').convert()
        self.img_planets = [self.planet_01, self.planet_01, self.planet_01]
        self.num_planets = len(self.img_planets)
        self.img_index = random.randrange(0, self.num_planets - 1)
        self.image = self.img_planets[self.img_index]
        self.scale_value = random.uniform(.25, 1.0)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_value), int(self.image.get_height() * self.scale_value)))
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.pos_x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.pos_y = 0 - self.rect.height
        self.vel_x = 0.0
        self.vel_y = random.uniform(0.1, 1.5)
        
    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x = int(self.pos_x)
        self.rect.y= int(self.pos_y)