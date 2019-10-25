import pygame, random

class Car(pygame.sprite.Sprite):
    def __init__(self, image, orderNum, Yposition, speed, screenWidth):
        super().__init__()
        #self.image = pygame.Surface([screenWidth/10,screenWidth/20])
        self.image = pygame.image.load("images/"+image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(screenWidth/8),int(screenWidth/20)))
        #self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.orderNum = orderNum
        self.screenWidth = screenWidth

        self.startPosition = (screenWidth/4*self.orderNum) + int(self.rect.width*self.orderNum)
        if self.speed > 0:
            
            self.rect.x = 0 - self.startPosition
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.rect.x = screenWidth + self.startPosition

        self.rect.y = Yposition

        self.limit = screenWidth


    def move(self):
        self.rect.x+=self.speed
        if self.speed>0:
            if self.rect.x > self.limit:
                self.rect.x = 0-self.rect.width
        else:
            if self.rect.x < (0 - self.rect.width):
                self.rect.x = self.screenWidth
    
    def paint(self, surface):
        surface.blit(self.image,(self.rect.x,self.rect.y)) 



    
