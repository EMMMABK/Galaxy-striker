import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 650))
    pygame.display.set_caption("Space defenders")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)

if __name__ == "__main__":
    run()