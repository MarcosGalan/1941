import pygame


class Keyboard:
    def __init__(self):
        self.currentKeyStates = None
        self.previousKeyStates = None

    def processInput(self):
        self.previousKeyStates = self.currentKeyStates
        self.currentKeyStates = pygame.key.get_pressed()

    def isKeyDown(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == True

    def isKeyPressed(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == True and self.previousKeyStates[keyCode] == False

    def isKeyReleased(self, keyCode):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[keyCode] == False and self.previousKeyStates[keyCode] == True


class Mouse:
    def __init__(self):
        self.currentKeyStates = None
        self.previousKeyStates = None

    def processInput(self):
        self.previousKeyStates = self.currentKeyStates
        self.currentKeyStates = pygame.mouse.get_pressed()

    def isKeyDown(self, key_index):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[key_index] == True

    def isKeyPressed(self, key_index):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[key_index] == True and self.previousKeyStates[key_index] == False

    def isKeyReleased(self, key_index):
        if self.currentKeyStates is None or self.previousKeyStates is None:
            return False
        return self.currentKeyStates[key_index] == False and self.previousKeyStates[key_index] == True

    def getMousePos(self):
        return pygame.mouse.get_pos()


class InputStream:
    def __init__(self):
        self.keyboard = Keyboard()
        self.mouse = Mouse()

    def processInput(self):
        self.keyboard.processInput()
        self.mouse.processInput()
