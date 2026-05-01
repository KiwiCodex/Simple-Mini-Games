import pygame
from functions import get_file_path, colorize
import constants as c

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(get_file_path("laser.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 10

        if self.rect.y < 0:
            self.kill()


class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, position, direction, color):
        super().__init__()
        base_image = pygame.image.load(get_file_path("laser.png")).convert_alpha()
        w, h = base_image.get_size()
        big_laser = pygame.transform.scale(base_image, (w*2, h*2))
        self.image = colorize(big_laser, color)

        if direction in ["left", "right"]:
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect(center=position)
        self.direction = direction
        self.speed = 7

    def update(self):
        if self.direction == "left": self.rect.x -= self.speed
        elif self.direction == "right": self.rect.x += self.speed
        elif self.direction == "down": self.rect.y += self.speed
        elif self.direction == "up": self.rect.y -= self.speed

        if not (0 <= self.rect.x <= c.WIDTH and 0 <= self.rect.y <= c.HEIGHT):
            self.kill()
        