import os

import pygame.sprite

from Bullet import Bullet
from Utils.constants import screen_height


class Player(pygame.sprite.Sprite):

    def __init__(self, pos: tuple, speed, health, damage, constraint_x):
        super().__init__()

        self.sprites = []
        for i in range(7):
            temp_image = pygame.image.load(f"assets/sprites/player/player_{i}.png")
            temp_image = pygame.transform.scale(temp_image, (temp_image.get_width() * 2, temp_image.get_height() * 2)).convert_alpha()
            self.sprites.append(temp_image)
        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect(midbottom=pos)
        self.rect.center = pos

        self.constraint_x = constraint_x

        # ------ DATA ---------
        self.speed = speed

        # Bullets
        self.shoot_delay = 0
        self.bullets = pygame.sprite.Group()
        self.health = health
        self.damage = damage

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.shoot_delay > 200:
            self.shoot_delay = current_time
            self.bullets.add(Bullet((self.rect.centerx - 14, self.rect.centery), -10, 1,screen_height))
            self.bullets.add(Bullet((self.rect.centerx + 14, self.rect.centery), -10, 1,screen_height))

    def get_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.animation()
            self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.animation()
            self.rect.x += self.speed

        else:
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]

        if keys[pygame.K_SPACE]:
            self.shoot()

    def animation(self):
        self.current_sprite += 0.4
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = len(self.sprites) - 1

        self.image = self.sprites[int(self.current_sprite)]

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.constraint_x:
            self.rect.right = self.constraint_x

    def update(self) -> None:
        self.get_inputs()
        self.constraint()
        self.bullets.update()

    def helth_damage(self,dmg:int):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            return True
        return False