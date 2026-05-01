import pygame
import os
import constants as c

def get_file_path(filename: str) ->str:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
        subfolder = os.path.join("assets", "images")
    
    elif filename.endswith(('.mp3', '.wav', '.ogg')):
        subfolder = os.path.join("assets", "sounds")

    else:
        subfolder = "" #Root Folder

    return os.path.join(base_dir, subfolder, filename)


# Score Text
def score(screen: pygame.Surface, font_obj: pygame.font.Font, text: str, color: tuple, x: int, y: int):
    surface = font_obj.render(text, True, color)
    rectangle = surface.get_rect()
    rectangle.center = (x, y)
    screen.blit(surface, rectangle)



# Game Over Screen
def show_game_over(screen: pygame.Surface, clock: pygame.time.Clock):
    
    screenshot = screen.copy()

    # Blur trick
    small_img = pygame.transform.smoothscale(screenshot, (c.WIDTH//10, c.HEIGHT//10))
    blurred_img = pygame.transform.smoothscale(small_img, (c.WIDTH, c.HEIGHT))

    center_x = c.WIDTH //2
    center_y = c.HEIGHT//2

    pygame.mixer.music.fadeout(1000)
    
    waiting = True
    while waiting:
        clock.tick(c.FPS)

        screen.blit(blurred_img, (0,0))
        
        # Semi-transparent dark screen
        overlay = pygame.Surface((c.WIDTH, c.HEIGHT)) 
        overlay.set_alpha(128)
        overlay.fill(c.BLACK)
        screen.blit(overlay, (0, 0))


        score(screen, c.times_font, "GAME OVER", c.RED, center_x, center_y - 100)
        score(screen, c.console_font, f"Current Highscore: {c.HIGHSCORE}", c.GREEN, center_x, center_y -20)
        score(screen, c.console_font, "Press 'R' to Retry", c.WHITE, center_x, center_y + 60)
        score(screen, c.console_font, "Press 'Q' to Quit", c.WHITE, center_x, center_y + 100)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.mixer.music.play(loops=-1) # Reset music
                    return True
                if event.key == pygame.K_q:
                    return False                


def colorize(image: pygame.Surface, new_color: tuple) -> pygame.Surface:
    colorized_image = image.copy()
    color_surface = pygame.Surface(colorized_image.get_size()).convert_alpha()
    color_surface.fill(new_color)

    colorized_image.blit(color_surface, (0,0), special_flags=pygame.BLEND_RGBA_MIN)
    return colorized_image