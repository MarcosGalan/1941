import os

import pygame

from SceneManager import SceneManager
from Utils.Button import ClickButton
from Utils.InputStream import InputStream
from Utils.Scene import Scene
from Utils.constants import screen_width, screen_height


class PauseScreen(Scene):

    def __init__(self, prev_screen: Scene):
        super().__init__()

        self.prev_screen = prev_screen
        self.foreground = pygame.image.load("assets/sprites/foreground.png")
        self.foreground = pygame.transform.scale(self.foreground, (screen_width, screen_height))

        self.font_big = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 136)
        self.font_mid = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 32)

        self.main_text = self.font_big.render("1941", True, (200, 50, 50))
        self.pause_text = self.font_mid.render("PAUSE", True, (255, 255, 255))

        self.play_button = ClickButton(screen_width * 0.5, screen_height*0.6,'',["assets/sprites/buttons/play_button.png","assets/sprites/buttons/play_button_pressed.png"])
        self.home_button = ClickButton(screen_width * 0.5, screen_height*0.7,'',["assets/sprites/buttons/home_button.png","assets/sprites/buttons/home_button_pressed.png"])


    def input(self, sm: SceneManager, inputStream: InputStream):

        if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE) or self.play_button.is_clicked():
            pygame.mixer.music.play(-1, 0, 0)
            sm.pop()
        if self.home_button.is_clicked():
            sm.scenes[0].__init__()
            sm.set([sm.scenes[0]])

    def update(self, sm: SceneManager, inputStream: InputStream):
        self.play_button.update(inputStream)
        self.home_button.update(inputStream)
        pass

    def draw(self, sm: SceneManager, screen: pygame.surface.Surface):
        self.prev_screen.draw(sm, screen)
        screen.blit(self.foreground,(0,0))

        o = self.main_text.get_rect(center=(screen_width / 2, screen_height * 0.3))
        screen.blit(self.main_text, o)

        o = self.pause_text.get_rect(center=(screen_width / 2, screen_height * 0.45))
        screen.blit(self.pause_text, o)

        self.play_button.draw(screen)
        self.home_button.draw(screen)



