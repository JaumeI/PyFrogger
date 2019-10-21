import pygame

class Cars(pygame.sprite.Sprite):
    def __init__(self, colour, Yposition, Xposition, direction):
        self.image = pygame.Surface([200,100])
        self.image.fill(colour)
        self.rect = self.image.get_rect()