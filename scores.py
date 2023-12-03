import pygame.font

class Score():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.screen_rect.top = 20
    
    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)

