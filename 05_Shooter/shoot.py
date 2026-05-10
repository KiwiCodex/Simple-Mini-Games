import pygame
import constants as c
from functions import get_file_path

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, to_right):
        super().__init__()
        bullet_img = pygame.image.load(get_file_path("bullet.png")).convert_alpha()

        if to_right:
            self.image = pygame.transform.flip(bullet_img, True, False)
            self.speed = 10
        else:
            self.image = bullet_img
            self. speed = -10

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.rect.x += self.speed

        if self.rect.right < 0 or self.rect.left > c.WIDTH:
            self.kill()
