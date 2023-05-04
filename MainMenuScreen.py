import os

import pygame.image

from GameScreen import GameScreen
from SceneManager import SceneManager
from Utils.Button import ClickButton
from Utils.InputStream import InputStream
from Utils.Scene import Scene
from Utils.constants import screen_width, screen_height


class MainMenuScreen(Scene):

    def __init__(self):
        self.background = pygame.image.load("assets/sprites/background_0.png")
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

        self.font = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 136)

        self.main_text = self.font.render("1941", True, (200, 50, 50))

        self.play_button = ClickButton(screen_width // 2,
                                       screen_height * 0.4,
                                      "PLAY",
                                       ["assets/sprites/buttons/blue_button.png",
                                       "assets/sprites/buttons/blue_button_pressed.png"])

        super().__init__()

    def input(self, sm: SceneManager, inputStream: InputStream):
        if self.play_button.is_clicked():
            sm.push(GameScreen())
            self.play_button.clicked = False

    def update(self, sm, inputStream):
        self.play_button.update(inputStream)

    def draw(self, sm: SceneManager, screen: pygame.surface.Surface):
        # Background drawing
        screen.blit(self.background, (0, 0))

        # Main text drawing
        o = self.main_text.get_rect(center=(screen_width / 2, screen_height * 0.25))
        screen.blit(self.main_text, o)

        # Buttons drawing
        self.play_button.draw(screen)
