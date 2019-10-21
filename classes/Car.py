import pygame, random

class Car(pygame.sprite.Sprite):
    def __init__(self, colour, Xposition, Yposition, direction, screenWidth):
        super().__init__()
        self.image = pygame.Surface([screenWidth/10,screenWidth/20])
        self.image = pygame.image.load("images/"+colour+"car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(screenWidth/8),int(screenWidth/20)))
        #self.image.fill(colour)
        self.rect = self.image.get_rect()
        if direction > 0:
            self.rect.x = 0 - self.rect.width
            self.image = pygame.transform.flip(self.image, True, False)

        else:
            self.rect.x = screenWidth
        #self.rect.x = Xposition
        self.rect.y = Yposition

        self.speed = random.randint(int(screenWidth/60),int(screenWidth/40))*direction

        self.limit = screenWidth
        self.alive=True

    def move(self):
        if self.alive:
            self.rect.x+=self.speed
            if self.speed>0:
                if self.rect.x > self.limit:
                    self.alive=False
            else:
                if self.rect.x < (0 - self.rect.width):
                    self.alive=False
    
    def paint(self, surface):
        if self.alive:
            surface.blit(self.image,(self.rect.x,self.rect.y)) 



    
