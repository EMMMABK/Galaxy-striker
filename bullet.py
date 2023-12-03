import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,250,12)
        self.color = 34, 177, 76
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)