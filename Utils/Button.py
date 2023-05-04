import os

import pygame.image

from Utils.InputStream import InputStream


class ClickButton:
    def __init__(self, x: int, y: int, text: str, button_images, keyCode=None, mouseKey=0):
        self.x = x
        self.y = y

        # Interacions
        self.keyCode = keyCode
        self.mouseKey = mouseKey

        # UI
        self.images = [pygame.image.load(os.path.abspath(i)) for i in button_images]
        self.images = [pygame.transform.scale(i,(i.get_width()*5,i.get_height()*4)) for i in self.images]
        self.image = self.images[0]
        self.image_rect = self.image.get_rect(center=(x, y))

        self.text = text
        self.font = pygame.font.Font(os.path.abspath("assets/fonts/forwa.ttf"), 14)
        self.rendered_text = self.font.render(self.text, True, (0, 0, 0))

        self.clicked = False
        self.hover = False

    def update(self, inputStream: InputStream):

        if self.image_rect.collidepoint(inputStream.mouse.getMousePos()):
            self.hover = True

            if inputStream.mouse.isKeyDown(self.mouseKey):
                self.clicked = True
            else:
                self.clicked = False

        else:
            self.hover = False

    def draw(self, screen: pygame.surface.Surface, alpha=255):

        if self.hover:
            self.rendered_text = self.font.render(self.text, True, (255, 20, 20))

            if self.clicked:
                self.image = self.images[-1]
            else:
                self.image = self.images[0]

        else:
            self.rendered_text = self.font.render(self.text, True, (0, 0, 0))

        screen.blit(self.image, self.image_rect)
        text_center = self.rendered_text.get_rect(center=(self.x, self.y))
        screen.blit(self.rendered_text, text_center)

    def is_clicked(self):
        return self.clicked

