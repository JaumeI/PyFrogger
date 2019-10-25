import pygame

class Cotxe(pygame.sprite.Sprite):
    def __init__(self,Yposition):
        super().__init__()
        self.image = pygame.Surface((50,30))
        self.image.fill((90,90,90))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = Yposition

    def move(self):
        self.rect.x+=10
        
    def paint(self,surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
