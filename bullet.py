import pygame 

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('bullet.png').convert_alpha()
        #scaling image by 1.5
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*1.5, self.image.get_height()*1.5))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = -8

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    