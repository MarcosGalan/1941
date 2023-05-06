import os

import pygame

from Utils.InputStream import InputStream
from Utils.constants import screen_width, screen_height


class TextInputBox:
    def __init__(self, x, y, size):

        self.background = pygame.image.load(os.path.abspath("assets/sprites/black_frame.png"))
        self.background = pygame.transform.scale(self.background, size)
        self.bg_rect = self.background.get_rect(center=(x, y))

        self.text = ""
        self.active = False

        self.font = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 14)


    def update(self, inputStream):
        event_list = inputStream.events
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                if self.bg_rect.collidepoint((event.pos[0], event.pos[1])):
                    self.active = True
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 17:
                        self.text += event.unicode

    def draw(self, screen: pygame.surface.Surface):

        screen.blit(self.background, self.bg_rect)

        text = self.font.render(f"{self.text}", True,(255, 255, 255))
        text_rect = text.get_rect(midleft=self.bg_rect.midleft)
        screen.blit(text, (text_rect.x + 10,text_rect.y))

    def get_text(self):
        return self.text
