import pygame
import constants as c
from functions import get_file_path, colorize
import random

class Zombie(pygame.sprite.Sprite):
    def __init__(self, side):
        super().__init__()
        self.base_img = pygame.image.load(get_file_path("zombie.png")).convert_alpha()
        self.hp = 2
        self.points_value = 10

        self.setup_movement(side, self.base_img, speed=2)

    def setup_movement(self, side, image, speed):
        if side == "right":
            self.image = pygame.transform.flip(image, True, False)
            self.speed = -speed
            start_x = c.WIDTH + random.randint(50, 600)
        else:
            self.image = image
            self.speed = speed
            start_x = -random.randint(50, 600)

        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.bottom = 680

    def update(self):
        self.rect.x  += self.speed

        # Border's limits
        if (self.speed > 0 and self.rect.left > c.WIDTH) or (self.speed < 0 and self.rect.right < 0):
            self.kill()

class ZombieSpeed(Zombie):
    def __init__(self, side):
        super().__init__(side)

        self.hp = 1
        self.points_value = 25

        zombie_speed_img = colorize(self.base_img, c.BLUE)

        self.setup_movement(side, zombie_speed_img, speed= 6)


class ZombieGiant(Zombie):
    def __init__(self, side):
        super().__init__(side)

        self.hp = 5
        self.points_value = 50

        new_size = (self.base_img.get_width() * 2, self.base_img.get_height() * 2)
        big_img = pygame.transform.scale(self.base_img, new_size)

        giant_zombie_img = colorize(big_img, c.RED)

        self.setup_movement(side, giant_zombie_img, speed=1)