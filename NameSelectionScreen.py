import pygame

from GameScreen import GameScreen
from SceneManager import SceneManager
from Utils.Button import ClickButton
from Utils.InputStream import InputStream
from Utils.Scene import Scene
from Utils.TextInput import TextInputBox
from Utils.constants import screen_height, screen_width


class NameSelectionScreen(Scene):

    def __init__(self):
        super().__init__()


        self.big_font = pygame.font.Font("assets/fonts/forwa.ttf", 136)
        self.font = pygame.font.Font("assets/fonts/forwa.ttf", 32)

        self.music = pygame.mixer.music.load("assets/sounds/stage1.mp3","ambient")
        pygame.mixer.music.play(-1,0,0)

        self.main_text = self.big_font.render("1941", True, (200, 50, 50))
        self.name_text = self.font.render("PICK A NICKNAME:",True,(255,255,255))

        self.textBox = TextInputBox(screen_width * 0.5, screen_height * 0.6,(200,50))

        self.start_button = ClickButton(screen_width // 2,
                                        screen_height * 0.8,
                                       "START",
                                        ["assets/sprites/buttons/green_button.png",
                                        "assets/sprites/buttons/green_button_pressed.png"])

        self.back_button = ClickButton(screen_width // 2,
                                        screen_height * 0.9,
                                       "BACK",
                                        ["assets/sprites/buttons/red_button.png",
                                        "assets/sprites/buttons/red_button_pressed.png"])

    def input(self, sm: SceneManager, inputStream: InputStream):
        if self.start_button.is_clicked():

            sm.push(GameScreen(self.textBox.get_text()))
            self.start_button.clicked = False
        if self.back_button.is_clicked():
            sm.pop()
            sm.scenes[0].__init__()

    def update(self, sm: SceneManager, inputStream: InputStream):
        self.textBox.update(inputStream)
        self.start_button.update(inputStream)
        self.back_button.update(inputStream)

    def draw(self, sm: SceneManager, screen: pygame.surface.Surface):
        screen.fill((20, 20, 50))

        o = self.main_text.get_rect(center=(screen_width / 2, screen_height * 0.3))
        screen.blit(self.main_text, o)

        o = self.name_text.get_rect(center=(screen_width / 2, screen_height * 0.5))
        screen.blit(self.name_text, o)

        self.textBox.draw(screen)

        self.start_button.draw(screen)
        self.back_button.draw(screen)
