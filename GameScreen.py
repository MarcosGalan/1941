import math
import os
import random

import pygame

from Enemy import Enemy
from Explosion import Explosion
from LoseScreen import LoseScreen
from PauseScreen import PauseScreen
from Player import Player
from Utils.Button import ClickButton
from Utils.Scene import Scene
from Utils.constants import screen_width, screen_height


class GameScreen(Scene):

    def __init__(self, name):
        super().__init__()

        self.background = pygame.image.load(f"assets/sprites/background_{random.randint(0, 3)}.png")
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

        self.points = 0

        self.pause_button = ClickButton(screen_width * 0.9, screen_height*0.05,'',["assets/sprites/buttons/pause_button.png","assets/sprites/buttons/pause_button_pressed.png"])

        # Info surface

        self.font_mid = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 12)

        # Sounds

        self.explosion_sound = pygame.mixer.Sound("assets/sounds/shipexplosion.wav")
        self.life_sound = pygame.mixer.Sound("assets/sounds/life_lose.wav")

        # Player
        self.name = name
        self.max_health = 5
        player_sprite = Player(pos=(screen_width / 2, screen_height * 0.95), speed=5, health=self.max_health, damage=5,
                               constraint_x=screen_width)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Enemies
        self.last_enemy = 0
        self.enemies = pygame.sprite.Group()
        self.frequency = 2500
        self.quantity = 8
        self.bullet_speed = 5

        # Explosions
        self.explosions = pygame.sprite.Group()
        
        # Heart
        self.heart_sprites = [pygame.image.load(f"assets/sprites/health/heart_{i}.png") for i in range(2)]
        self.heart_sprites = [pygame.transform.scale(i, (i.get_width() * 3, i.get_height() * 3)) for i in self.heart_sprites]

        self.heart_proportion = 5 / self.max_health



    def input(self, sm, inputStream):
        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE) or self.pause_button.is_clicked():
            self.pause_button.clicked = False
            self.enemy_creator()
            pygame.mixer.music.pause()
            sm.push(PauseScreen(self))

    def update(self, sm, inputStream):

        self.pause_button.update(inputStream)
        self.player.update()
        self.enemy_creator()
        self.enemies.update()
        self.explosions.update()
        self.collisions(sm)



    def draw(self, sm, screen):
        try:

            screen.blit(self.background, (0, 0))
            self.player.sprite.bullets.draw(screen)
            [o.bullets.draw(screen) for o in self.enemies.sprites()]
            self.player.draw(screen)
            self.enemies.draw(screen)
            self.explosions.draw(screen)
            self.pause_button.draw(screen)
            self.heart_draw(screen)
            points = self.font_mid.render(f"Points: {self.points}",True,(255,255,255))
            points_rect = points.get_rect(center=(screen_width*0.1,screen_height*0.1))
            screen.blit(points,points_rect)
        except :
            pass



    def enemy_creator(self):
        if pygame.time.get_ticks() - self.last_enemy > self.frequency and len(self.enemies.sprites()) <= int(self.quantity):
            self.quantity += 0.5
            self.frequency *= 0.99
            self.bullet_speed *= 1.007
            self.last_enemy = pygame.time.get_ticks()
            self.enemies.add(Enemy((random.randint(40, screen_width - 40), random.randint(40, screen_height * 0.5)),2,self.frequency,self.bullet_speed))

    def collisions(self,sm):
        try:
            for bullet in self.player.sprite.bullets.sprites():
                enemy = pygame.sprite.spritecollide(bullet, self.enemies, False)
                if enemy:
                    bullet.kill()
                for agro in enemy:
                    if agro.damage(bullet.damage):
                        self.points += 10
                        self.explosion_sound.play()
                        self.explosions.add(Explosion(agro.rect.center))




            for enemy in self.enemies.sprites():
                for bullet in enemy.bullets.sprites():

                    bullet_player = pygame.sprite.spritecollide(bullet,self.player.sprite.bullets.sprites(),False)
                    for collision in bullet_player:
                        self.explosions.add(Explosion(collision.rect.center))
                        bullet.kill()
                        collision.kill()

                    if self.player.sprite.rect.colliderect(bullet.rect):
                        self.life_sound.play()
                        if self.player.sprite.helth_damage(bullet.damage):
                            sm.pop()
                            sm.push(LoseScreen(self,self.points, self.name))
                            return

                        bullet.kill()

        except AttributeError:
            pass


    def heart_draw(self, screen):

        hearts = math.ceil(self.player.sprite.health * self.heart_proportion)
        for i in range(5):

            if i < hearts:
                screen.blit(self.heart_sprites[1],(screen_width*0.02+self.heart_sprites[1].get_width()*i+10*i,screen_height*0.05))
            else:
                screen.blit(self.heart_sprites[0],(screen_width*0.02+self.heart_sprites[0].get_width()*i+10*i,screen_height*0.05))