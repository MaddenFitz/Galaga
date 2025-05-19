import pygame
import constants as c 


class HeartIcon(pygame.sprite.Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()
        self.img_heart_01 = pygame.image.load('Heart_01.png').convert_alpha()
        self.img_heart_01 = pygame.transform.scale(self.img_heart_01, (self.img_heart_01.get_width()*0.65, self.img_heart_01.get_height()*0.65))

        self.img_heart_02 = pygame.image.load('Heart_02.png').convert_alpha()
        self.img_heart_02 = pygame.transform.scale(self.img_heart_02, (self.img_heart_02.get_width()*0.65, self.img_heart_02.get_height()*0.65))

        self.img_heart_03 = pygame.image.load('Heart_03.png').convert_alpha()
        self.img_heart_03 = pygame.transform.scale(self.img_heart_03, (self.img_heart_03.get_width()*0.65, self.img_heart_03.get_height()*0.65))

        self.img_heart_04 = pygame.image.load('Heart_04.png').convert_alpha()
        self.img_heart_04 = pygame.transform.scale(self.img_heart_04, (self.img_heart_04.get_width()*0.65, self.img_heart_04.get_height()*0.65))

        self.img_heart_05 = pygame.image.load('Heart_05.png').convert_alpha()
        self.img_heart_05 = pygame.transform.scale(self.img_heart_05, (self.img_heart_05.get_width()*0.65, self.img_heart_05.get_height()*0.65))

        self.anim_list = [self.img_heart_01, self.img_heart_02, self.img_heart_03, self.img_heart_04, self.img_heart_05]

        self.anim_index = 0
        self.max_index = len(self.anim_list) - 1
        self.max_frame_duration = 5
        self.frame_duration = self.max_frame_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.65), int(self.image.get_height() * 0.65)))
        self.rect.x = 14
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 10
    
    def update(self):
        if self.frame_duration == 0:
            self.anim_index += 1
            if self.anim_index > self.max_index:
                self.anim_index = 0
            self.image = self.anim_list[self.anim_index]
            self.frame_duration = self.max_frame_duration
        self.frame_duration -= 1