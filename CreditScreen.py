import pygame

from SceneManager import SceneManager
from Utils.Button import ClickButton
from Utils.InputStream import InputStream
from Utils.Scene import Scene
from Utils.constants import screen_height, screen_width


class CreditScreen(Scene):

    def __init__(self):
        super().__init__()

        self.big_font = pygame.font.Font("assets/fonts/forwa.ttf", 72)
        self.font = pygame.font.Font("assets/fonts/forwa.ttf", 32)

        self.main_text = self.big_font.render("CREDITS", True, (200, 50, 50))
        self.main_text_rect = self.main_text.get_rect(center = (screen_width * 0.5, screen_height * 0.3))
        self.name_text = self.font.render("MARCOS GALAN ©",True,(255,255,255))
        self.name_text_rect = self.name_text.get_rect(center = (screen_width * 0.5, screen_height * 0.5))

        self.back_button = ClickButton(screen_width // 2,
                                       screen_height * 0.9,
                                       "BACK",
                                       ["assets/sprites/buttons/red_button.png",
                                        "assets/sprites/buttons/red_button_pressed.png"])


    def input(self, sm:SceneManager, inputStream: InputStream):
        if self.back_button.is_clicked():
            sm.pop()
            sm.scenes[0].__init__()
    def update(self, sm:SceneManager, inputStream: InputStream):
        self.back_button.update(inputStream)
    def draw(self, sm:SceneManager, screen:pygame.surface.Surface):
        screen.fill((20, 20, 50))

        screen.blit(self.main_text,self.main_text_rect)
        screen.blit(self.name_text,self.name_text_rect)

        self.back_button.draw(screen)