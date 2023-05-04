import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, damage, screen_height, flip=False):
        super().__init__()
        self.sprites = []
        for i in range(4):
            temp_image = pygame.image.load(f"assets/sprites/bullet/bullet_{i}.png")
            temp_image = pygame.transform.rotate(temp_image, 90).convert_alpha()
            temp_image = pygame.transform.flip(temp_image, False, flip)
            self.sprites.append(temp_image)

        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

        self.damage = damage

        self.rect = self.image.get_rect(midbottom=pos)
        self.rect.center = pos
        self.speed = speed
        self.height_y_constraint = screen_height

    def animation(self):
        self.current_sprite += 0.4
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.animation()
        self.destroy()
