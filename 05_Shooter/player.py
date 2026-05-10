import pygame
import constants as c
from functions import get_file_path
from shoot import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group, all_sprites):
        super().__init__()
        self.image_left = pygame.image.load(get_file_path("player.png")).convert_alpha()
        self.image_right = pygame.transform.flip(self.image_left, True, False) # Horizontal Flip
        self.image = self.image_left

        self.rect = self.image.get_rect()
        self.rect.center = (c.WIDTH // 2, c.PLAYER_START_Y)

        self.facing_right = False
        self.speed_x = 0

        self.all_sprites = all_sprites
        self.bullet_group = bullet_group

        self.cadence = 300
        self.cooldown = pygame.time.get_ticks()

        self.hp = 3
        self.invulnerable = False
        self.last_hit = 0
        self.iframe_duration = 1500 # 1.5 seconds

        self.shotgun_sound = pygame.mixer.Sound(get_file_path("shotgun.mp3"))
        self.shotgun_sound.set_volume(0.1)

    def take_damage(self):
        now = pygame.time.get_ticks()
        if not self.invulnerable:
            self.hp -= 1
            self.invulnerable = True
            self.last_hit = now
            return True
        return False


    def fire(self):
        spawn_x = self.rect.right if self.facing_right else self.rect.left

        bullets = Bullet(spawn_x, self.rect.centery - 32, self.facing_right)
        self.bullet_group.add(bullets)
        self.all_sprites.add(bullets)

    def update(self):
        now = pygame.time.get_ticks()

        if self.invulnerable:
            if self.invulnerable and now - self.last_hit > self.iframe_duration:
                self.invulnerable = False
                self.image.set_alpha(255) # Normal Opacity
            
            # Flickering effect
            else:
                if (now // 100) % 2 == 0:
                    self.image.set_alpha(255) # Normal Opacity
                else:
                    self.image.set_alpha(100) # Kinda Transparent


        self.speed_x = 0
        keys = pygame.key.get_pressed()

        # Controls
        if keys[pygame.K_LEFT]:
            self.speed_x = -3
            self.image = self.image_left
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.speed_x = 3
            self.image = self.image_right
            self.facing_right = True
        if keys[pygame.K_SPACE]:
            time = pygame.time.get_ticks()
            if time - self.cooldown > self.cadence:
                self.fire()
                self.shotgun_sound.play()
                self.cooldown = time

        self.rect.x += self.speed_x 

        # Border's limits
        if self.rect.left < 0:  self.rect.left = 0
        if self.rect.right > c.WIDTH: self.rect.right = c.WIDTH