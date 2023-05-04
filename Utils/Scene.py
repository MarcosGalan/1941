import pygame

from SceneManager import SceneManager
from Utils.InputStream import InputStream


class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm:SceneManager, inputStream: InputStream):
        pass
    def update(self, sm:SceneManager, inputStream: InputStream):
        pass
    def draw(self, sm:SceneManager, screen:pygame.surface.Surface):
        pass









