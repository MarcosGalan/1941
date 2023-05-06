import json
import os

import pygame.image

from GameScreen import GameScreen
from NameSelectionScreen import NameSelectionScreen
from SceneManager import SceneManager
from Utils.Button import ClickButton
from Utils.InputStream import InputStream
from Utils.Scene import Scene
from Utils.constants import screen_width, screen_height


class MainMenuScreen(Scene):

    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("assets/sprites/background_0.png")
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

        self.font = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 136)
        self.font_low = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 11)

        self.main_text = self.font.render("1941", True, (200, 50, 50))

        self.play_button = ClickButton(screen_width // 2,
                                       screen_height * 0.45,
                                       "PLAY",
                                       ["assets/sprites/buttons/blue_button.png",
                                        "assets/sprites/buttons/blue_button_pressed.png"])

        self.credits_button = ClickButton(screen_width // 2,
                                       screen_height * 0.55,
                                       "CREDITS",
                                       ["assets/sprites/buttons/orange_button.png",
                                        "assets/sprites/buttons/orange_button_pressed.png"],
                                       )

        self.quit_button = ClickButton(screen_width // 2,
                                       screen_height * 0.65,
                                       "QUIT",
                                       ["assets/sprites/buttons/red_button.png",
                                        "assets/sprites/buttons/red_button_pressed.png"],
                                       )

        # Puntuactions
        # Read JSON file
        with open('data.json') as data_file:
            data_loaded = json.load(data_file)

        self.first_player = data_loaded["top_players"]["first_player"]
        self.first_player_text = self.font_low.render(f"{self.first_player[0]}: {self.first_player[1]}", True,
                                                      (255, 255, 255))

        self.second_player = data_loaded["top_players"]["second_player"]
        self.second_player_text = self.font_low.render(f"{self.second_player[0]}: {self.second_player[1]}", True,
                                                       (255, 255, 255))

        self.third_player = data_loaded["top_players"]["third_player"]
        self.third_player_text = self.font_low.render(f"{self.third_player[0]}: {self.third_player[1]}", True,
                                                      (255, 255, 255))


    def input(self, sm: SceneManager, inputStream: InputStream):
        if self.play_button.is_clicked():
            sm.push(NameSelectionScreen())
            self.play_button.clicked = False

        if self.quit_button.is_clicked():
            sm.pop()

    def update(self, sm, inputStream):
        self.play_button.update(inputStream)
        self.credits_button.update(inputStream)
        self.quit_button.update(inputStream)

    def draw(self, sm: SceneManager, screen: pygame.surface.Surface):
        # Background drawing
        screen.blit(self.background, (0, 0))

        # Main text drawing
        o = self.main_text.get_rect(center=(screen_width / 2, screen_height * 0.25))
        screen.blit(self.main_text, o)

        # Buttons drawing
        self.play_button.draw(screen)
        self.credits_button.draw(screen)
        self.quit_button.draw(screen)

        o = self.first_player_text.get_rect(center=(screen_width / 2, screen_height * 0.9))
        screen.blit(self.first_player_text, o)

        o = self.second_player_text.get_rect(center=(screen_width * 0.2, screen_height * 0.9))
        screen.blit(self.second_player_text, o)

        o = self.third_player_text.get_rect(center=(screen_width * 0.8, screen_height * 0.9))
        screen.blit(self.third_player_text, o)
