import pygame
from player import Player
from enemy import Enemy
from functions import *
import constants as c
import random


# Initialize videogame
def main():
    pygame.init()
    window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    pygame.display.set_caption("Space Ship")
    # Establish FPS
    clock = pygame.time.Clock()

    # Sounds
    bg_music = pygame.mixer.music.load(get_file_path("bg_music.mp3"))
    pygame.mixer.music.play(loops=-1)
    point_sound = pygame.mixer.Sound(get_file_path("point.wav"))

    enemy_laser_sound = pygame.mixer.Sound(get_file_path("shoot.wav"))
    enemy_laser_sound.set_volume(0.3)
    Enemy.shoot_sound = enemy_laser_sound

    # Background
    bg = pygame.image.load(get_file_path("space.jpg")).convert()
    bg = pygame.transform.scale(bg, (c.WIDTH, c.HEIGHT))

    # Groups and Sprites
    all_sprites = pygame.sprite.Group()
    players = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    enemy_lasers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player(lasers, all_sprites)
    players.add(player)
    all_sprites.add(player)

    execute = True

    def spawn_enemies(count: int, current_score: int):
        for _ in range(count):
            if current_score > 1000:
                enemy_type = random.choice(["normal", "yellow", "red"])
            elif current_score > 500:
                enemy_type = random.choice(["normal", "yellow"])
            else:
                enemy_type = "normal"

            e = Enemy(enemy_type)
            enemies.add(e)
            all_sprites.add(e)
    
    # Main Loop
    while execute:
        clock.tick(c.FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execute = False
        
        # Update's Logic
        all_sprites.update()

        # Enemies' Waves
        if not enemies:
            spawn_enemies(random.randint(5, 8), c.SCORE)

        for e in enemies:
            e.shoot(enemy_lasers, all_sprites)
        
    
        # LASER colission's to: ENEMY
        hits = pygame.sprite.groupcollide(enemies, lasers, True, True)
        if hits:
            c.SCORE += 30 * len(hits)
            point_sound.play()
            if c.HIGHSCORE < c.SCORE:
                c.HIGHSCORE = c.SCORE
        
        # Colissions
        colission_to_ship = pygame.sprite.spritecollide(player, enemies, False)
        colission_to_shoot = pygame.sprite.spritecollide(player, enemy_lasers, True)

        if colission_to_ship:
            c.SCORE -= 10
        
        if colission_to_shoot:
            c.SCORE -= 100

        # Game Over
        if c.SCORE <= 0:
            c.SCORE = 0
            if colission_to_ship or colission_to_shoot:
                if show_game_over(window, clock):
                    enemies.empty()
                    lasers.empty()
                    enemy_lasers.empty()
                    all_sprites.empty()

                    player.rect.center = (c.WIDTH//2, c.HEIGHT - 50)
                    all_sprites.add(player)
                else:
                    execute = False

        # Render 
        window.blit(bg, (0, 0))

        # Draw sprites
        all_sprites.draw(window)

        # UI
        color_score = c.GREEN if c.SCORE >= c.HIGHSCORE and c.SCORE > 0 else c.WHITE

        score(window, c.times_font, str(c.SCORE).zfill(7), color_score, 700, 50)

        score(window, c.times_font, str(c.HIGHSCORE).zfill(7), c.GREEN, 100, 50)


        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()

