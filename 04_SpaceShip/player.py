import pygame
from laser import Laser
from functions import get_file_path
import constants as c


# Player's class
class Player(pygame.sprite.Sprite):
    def __init__(self, laser_group, all_sprites_groups):
        super().__init__()
        self.image = pygame.image.load(get_file_path("ship.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

        self.laser_group = laser_group # Save Laser Group here
        self.all_sprites = all_sprites_groups

        self.speed_x = 0
        self.speed_y = 0

        self.cadence = 100
        self.cooldown = pygame.time.get_ticks()

        self.laser_shoot_sound = pygame.mixer.Sound(get_file_path("shoot.wav"))

    def shoot(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        self.laser_group.add(laser)
        self.all_sprites.add(laser)


    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.speed_x = -10
        if keys[pygame.K_RIGHT]:
            self.speed_x = 10
        if keys[pygame.K_UP]:
            self.speed_y = -10
        if keys[pygame.K_DOWN]:
            self.speed_y = 10
        
        if keys[pygame.K_SPACE]:
            time = pygame.time.get_ticks()
            if time - self.cooldown > self.cadence:
                self.shoot()
                self.laser_shoot_sound.play()
                self.cooldown = time


        self.rect.x += self.speed_x         
        self.rect.y += self.speed_y         

        # Border Limit
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > c.WIDTH:
            self.rect.right = c.WIDTH
        if self.rect.bottom > c.HEIGHT:
            self.rect.bottom = c.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


