import pygame


class Explosion(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.sprites = []

        for i in range(14):
            temp_image = pygame.image.load(f"assets/sprites/explosions/explosion_{i}.png")
            temp_image = pygame.transform.scale(temp_image, (temp_image.get_width()*2,temp_image.get_height()*2))
            self.sprites.append(temp_image)

        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(midbottom=pos)
        self.rect.center = pos

    def animation(self):
        self.current_sprite += 0.4
        if self.current_sprite >= len(self.sprites)-1:
            self.kill()

        self.image = self.sprites[int(self.current_sprite)]

    def update(self) -> None:

        self.animation()


