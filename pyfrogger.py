import pygame, sys, random
from Classes.Car import *

from pygame.locals import *

pygame.init()

# Definim la mida de la finestra
SCREENWIDTH = 800
SCREENHEIGHT=800
# Creem una finestra de les mides indicades
DISPLAYSURF=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
# Poseu el nom que més us convingui a la finestra!
pygame.display.set_caption("PyFrogger")

# Una font per escriure coses per pantalla. 
FONT = pygame.font.SysFont('arial',18)

#El "salt" que es mou la granota
JUMP = int(SCREENHEIGHT/10)

background=pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (SCREENWIDTH,SCREENHEIGHT))

#La nostra granota. Recordeu buscar la imatge i posar-la a la carpeta!
FROG = pygame.sprite.Sprite()
FROG.image = pygame.image.load("images/standingFrog.png").convert_alpha()
FROG.image = pygame.transform.scale(FROG.image, (int(SCREENWIDTH/20),int(SCREENHEIGHT/20)))
FROG.rect = FROG.image.get_rect()

# Aquestes posicions inicials potser caldria arreglar-les una mica...
FROG.rect.x = SCREENWIDTH/2 - FROG.image.get_width()/2
FROG.rect.y = SCREENHEIGHT-FROG.image.get_height()-(JUMP/2)


cars=pygame.sprite.Group()

#car = Car(Color(50,50,50),1,(int(SCREENHEIGHT/20*16)),1,SCREENWIDTH)
redcar = Car("red",1,(int(SCREENHEIGHT/20*16)),1,SCREENWIDTH)
bluecar = Car("blue",1,(int(SCREENHEIGHT/20*14)),-1,SCREENWIDTH)
 
cars.add(redcar)
cars.add(bluecar)

# Rellotge de control
clock=pygame.time.Clock()


#bucle infinit de joc
while True:
    for car in pygame.sprite.spritecollide(FROG, cars,0):
        print("Collision")
    #controlem els esdeveniments
    for event in pygame.event.get():
        #si és de tipus sortida, tanquem el joc
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # Si han premut una tecla...
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT and FROG.rect.x + JUMP < SCREENWIDTH-FROG.image.get_width(): # Aquest -1 no és correcte...
                FROG.rect.x+=JUMP 
            elif event.key==K_LEFT and FROG.rect.x - JUMP > 0:
                FROG.rect.x-=JUMP 
            elif (event.key==K_UP  and FROG.rect.y > 0):
                FROG.rect.y-=JUMP
            elif (event.key==K_DOWN  and FROG.rect.y + JUMP < SCREENHEIGHT-FROG.image.get_height()):# Aquest -1 no és correcte...
                FROG.rect.y+=JUMP
    
    #movem el cotxe
    for c in cars:
        c.move()
    # Fons negre
    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(background,(0,0)) 
    # La granota
    DISPLAYSURF.blit(FROG.image,(FROG.rect.x,FROG.rect.y)) 
    #DISPLAYSURF.blit(redcar.image,(redcar.rect.x,redcar.rect.y)) 
    #DISPLAYSURF.blit(car.image,(car.rect.x,car.rect.y)) 
    for c in cars:
        c.paint(DISPLAYSURF)
    #car.paint(DISPLAYSURF)
    #redibuixem la pantalla
    pygame.display.update()
    clock.tick(10)