import pygame
import constants as c
from functions import get_file_path, load_highscore, save_highscore, show_game_over, score, draw_lives
from player import Player
from enemy import Zombie, ZombieGiant, ZombieSpeed
import random

# Inicialize game
def main():
    pygame.init()

    window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    bg = pygame.transform.scale(pygame.image.load(get_file_path("bg.jpg")).convert(), (c.WIDTH, c.HEIGHT))
    heart = heart_image = pygame.image.load(get_file_path("heart.png")).convert_alpha()

    bg_music = pygame.mixer.music.load(get_file_path("bg_music.mp3"))
    pygame.mixer.music.play(loops=-1)

    time = pygame.time.Clock()

    pygame.display.set_caption("Shooter Fire!")

    highscore = load_highscore()
    points = 0


    # Sprites creation
    all_sprites = pygame.sprite.Group()
    player = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    GameOver = False


    hero = Player(bullets, all_sprites)
    player.add(hero)
    all_sprites.add(hero)
    

    while GameOver is False:
        window.blit(bg, (0, 0))
        time.tick(c.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameOver = True
    
        # Bullets kills zombies
        hits = pygame.sprite.groupcollide(enemies, bullets, False, True)
        for zombie in hits:
            zombie.hp -= 1
            if zombie.hp == 0:
                points += zombie.points_value
                zombie.kill()
                if points > highscore:
                    highscore = points

        # Zombies touch Hero
        if pygame.sprite.spritecollide(hero, enemies, True):
            got_hit = hero.take_damage()

            if got_hit and hero.hp <= 0:
                save_highscore(highscore)
                if show_game_over(window, time, highscore):
                    all_sprites.empty()
                    enemies.empty()
                    player.empty()
                    bullets.empty()

                    points = 0
                    hero.hp = 3
                    hero.invulnerable = False

                    hero.rect.center = (c.WIDTH // 2, c.PLAYER_START_Y)
                    player.add(hero)
                    all_sprites.add(hero)
                else:
                    GameOver = True
    
        # Zombie Spawn
        if not enemies:
            num_zombies = random.randrange(9, 15)
            for x in range(num_zombies):
                side = random.choice(["left", "right"])

                zombie_type = random.choices([Zombie, ZombieSpeed, ZombieGiant], weights=[65, 25, 10])[0]

                new_zombie = zombie_type(side)
                enemies.add(new_zombie)
                all_sprites.add(new_zombie)

        color_score = c.GREEN if points >= highscore and points > 0 else c.WHITE

        score(window, c.arial_font, str(points), color_score, 1100, 67)
        score(window, c.arial_font, str(highscore), c.GREEN, 100, 67)

        draw_lives(window, hero.hp, 1100, 120, heart)


        all_sprites.update()

        all_sprites.draw(window)

        pygame.display.flip()
        
    
if __name__ == "__main__":
    main()