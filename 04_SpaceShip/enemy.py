import pygame
from functions import get_file_path, colorize
from laser import EnemyLaser
import random
import constants as c


class Enemy(pygame.sprite.Sprite):
    shoot_sound = None

    def __init__(self, enemy_type = "normal"):
        super().__init__()
        base_image = pygame.image.load(get_file_path("ufo.png")).convert_alpha()
        self.type = enemy_type

        if self.type == "yellow":
            self.image = colorize(base_image, c.YELLOW)
        elif self.type == "red":
            self.image = colorize(base_image, c.RED)
        else:
            self.image = base_image

        self.rect = self.image.get_rect()
        
        self.rect.x = random.randrange(c.WIDTH - self.rect.width)
        self.rect.y = random.randrange(100, 300)

        # Enemy's movement
        self.speed_x = random.randrange(1, 6)
        self.speed_y = random.randrange(1, 6)

        # Trigger laser cooldown
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = random.randint(1500, 3000)

    def shoot(self, laser_group, all_sprites):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now

            if Enemy.shoot_sound:
                Enemy.shoot_sound.play()

            if self.type == "yellow":
                # X axis shoot
                l1 = EnemyLaser(self.rect.center, "left", c.YELLOW)
                l2 = EnemyLaser(self.rect.center, "right", c.YELLOW)
                laser_group.add(l1, l2)
                all_sprites.add(l1, l2)
            
            elif self.type == "red":
                l3 = EnemyLaser(self.rect.center, "down", c.RED)
                l4 = EnemyLaser(self.rect.center, "up", c.RED)
                laser_group.add(l3, l4)
                all_sprites.add(l3, l4)


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Border's collision
        if self.rect.left < 0 or self.rect.right > c.WIDTH:
            self.speed_x *= -1
       
        if self.rect.bottom > c.HEIGHT or self.rect.top < 0:
            self.speed_y *= -1


