# -*- coding: utf-8 -*-

import json
import os
import io


from pyparsing import unicode

import pygame

from SceneManager import SceneManager
from Utils.Button import ClickButton
from Utils.InputStream import InputStream
from Utils.Scene import Scene
from Utils.constants import screen_height, screen_width


class LoseScreen(Scene):

    def __init__(self, prev_screen, points, name):
        super().__init__()

        self.points = points
        self.name = name

        self.prev_screen = prev_screen
        self.foreground = pygame.image.load("assets/sprites/foreground.png")
        self.foreground = pygame.transform.scale(self.foreground, (screen_width, screen_height))


        self.music = pygame.mixer.Sound("assets/sounds/game_over.mp3")
        self.music.play()

        self.font_big = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 64)
        self.font_mid = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 32)

        self.main_text = self.font_big.render(f"CONGRATS!", True, (220, 220, 50))
        self.name_text = self.font_mid.render(f"{name}", True, (255, 255, 255))
        self.points_text = self.font_mid.render(f"POINTS:{points}", True, (255, 255, 255))

        self.home_button = ClickButton(screen_width * 0.5, screen_height * 0.7, '',
                                       ["assets/sprites/buttons/home_button.png",
                                        "assets/sprites/buttons/home_button_pressed.png"])

    def input(self, sm: SceneManager, inputStream: InputStream):
        if self.home_button.is_clicked():

            with open('data.json') as data_file:
                data_loaded = json.load(data_file)

            modified = False

            if data_loaded["top_players"]["first_player"][1] < self.points:
                data_loaded["top_players"]["third_player"] = data_loaded["top_players"]["second_player"]
                data_loaded["top_players"]["second_player"] = data_loaded["top_players"]["first_player"]
                data_loaded["top_players"]["first_player"] = [self.name, self.points]
                modified = True

            elif data_loaded["top_players"]["second_player"][1] < self.points:
                data_loaded["top_players"]["third_player"] = data_loaded["top_players"]["second_player"]
                data_loaded["top_players"]["second_player"] = [self.name, self.points]
                modified = True

            elif data_loaded["top_players"]["third_player"][1] < self.points:
                data_loaded["top_players"]["third_player"] = [self.name, self.points]
                modified = True

            else:
                pass

            data_file.close()

            if modified:
                with io.open('data.json', 'w', encoding='utf8') as outfile:
                    str_ = json.dumps(data_loaded,
                                      indent=4, sort_keys=True,
                                      separators=(',', ': '), ensure_ascii=True)

                    outfile.write(str_)

                outfile.close()

            sm.scenes[0].__init__()
            sm.set([sm.scenes[0]])

    def update(self, sm: SceneManager, inputStream: InputStream):
        self.home_button.update(inputStream)

    def draw(self, sm: SceneManager, screen: pygame.surface.Surface):
        self.prev_screen.draw(sm, screen)
        screen.blit(self.foreground, (0, 0))

        o = self.main_text.get_rect(center=(screen_width / 2, screen_height * 0.3))
        screen.blit(self.main_text, o)

        o = self.name_text.get_rect(center=(screen_width / 2, screen_height * 0.4))
        screen.blit(self.name_text, o)

        o = self.points_text.get_rect(center=(screen_width / 2, screen_height * 0.6))
        screen.blit(self.points_text, o)

        self.home_button.draw(screen)

        pass
