import random

import pygame.sprite

from Bullet import Bullet
from Utils.constants import screen_width, screen_height


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos: tuple,health=2, shoot_interval = 1500,bullet_speed = 5):
        super().__init__()

        self.sprites = []
        rand_size = random.uniform(1.5, 2)
        for i in range(4):
            temp_image = pygame.image.load(f"assets/sprites/enemy/enemy_{i}.png")
            temp_image = pygame.transform.scale(temp_image, (
                temp_image.get_width() * rand_size, temp_image.get_height() * rand_size)).convert_alpha()
            temp_image = pygame.transform.flip(temp_image, False, True).convert_alpha()
            self.sprites.append(temp_image)
        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        self.health = health

        self.objetive_pos = pos
        self.rect = self.image.get_rect(midbottom=pos)
        self.rect.center = (pos[0]-80, -10)

        self.shoot_interval = shoot_interval
        self.bullet_speed = bullet_speed
        self.last_shoot = 0
        self.bullets = pygame.sprite.Group()

    def movement(self):
        if self.rect.centerx < self.objetive_pos[0]:
            self.rect.center = (self.rect.centerx + 3, self.rect.centery)

        if self.rect.centery < self.objetive_pos[1]:
            self.rect.center = (self.rect.centerx, self.rect.centery + 3)

    def update(self) -> None:
        self.animation()
        self.shoot_control()
        self.movement()
        self.bullets.update()

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            return True
        return False


    def animation(self):

        self.current_sprite += 0.4
        if self.current_sprite >= 2:
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def shoot_control(self):
        if pygame.time.get_ticks() - self.last_shoot > self.shoot_interval:
            self.last_shoot = pygame.time.get_ticks()
            self.bullets.add(Bullet(self.rect.center,self.bullet_speed,1,screen_height,True))

