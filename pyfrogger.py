import pygame, sys, random, os
from Classes.Car import *
from Cotxe import *
from pygame.locals import *

pygame.init()

#Demanem la mida del monitor
mw = pygame.display.Info().current_w
mh = pygame.display.Info().current_h

if mw > mh:
    windowSize = mh - int(mh/10)
else:
    windowSize = mw - int(mw/10)

#posicio de la finestra
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (int((mw/2)-(windowSize/2)),int((mh/2)-(windowSize/2)))

# Definim la mida de la finestra
SCREENWIDTH = windowSize
SCREENHEIGHT= windowSize
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
cotxes = pygame.sprite.Group()
cotxes.add(Cotxe(400))
cotxes.add(Cotxe(300))
#car = Car(Color(50,50,50),1,(int(SCREENHEIGHT/20*16)),1,SCREENWIDTH)
#redcar = Car("redcar.png",1,0,1,SCREENWIDTH)

#bluecar = Car("bluecar.png",1,(int(SCREENHEIGHT/20*14)),-1,SCREENWIDTH)

'''#velocitat de la primera línia 
speed = random.randint(int(SCREENWIDTH/60),int(SCREENWIDTH/40)) 

#creem la primera línia
cars.add(Car("redcar.png",0,(int(SCREENHEIGHT/20*16)),speed,SCREENWIDTH))
cars.add(Car("redcar.png",1,(int(SCREENHEIGHT/20*16)),speed,SCREENWIDTH))
cars.add(Car("redcar.png",2,(int(SCREENHEIGHT/20*16)),speed,SCREENWIDTH))




speed = random.randint(int(SCREENWIDTH/60),int(SCREENWIDTH/40)) *(-1)
cars.add(Car("bluecar.png",0,(int(SCREENHEIGHT/20*14)),speed,SCREENWIDTH))
cars.add(Car("bluecar.png",1,(int(SCREENHEIGHT/20*14)),speed,SCREENWIDTH))
cars.add(Car("bluecar.png",2,(int(SCREENHEIGHT/20*14)),speed,SCREENWIDTH))
#Car("redcar.png",1,1,1,SCREENWIDTH)
#cars.add(bluecar)'''

speed = random.randint(int(SCREENWIDTH/60),int(SCREENWIDTH/40)) 
for i in range(3):
    cars.add(Car("redcar.png",i,(int(SCREENHEIGHT/20*16)),speed,SCREENWIDTH))

speed = random.randint(int(SCREENWIDTH/60),int(SCREENWIDTH/40))*(-1)
for i in range(3):
    cars.add(Car("bluecar.png",i,(int(SCREENHEIGHT/20*14)),speed,SCREENWIDTH))

speed = random.randint(int(SCREENWIDTH/55),int(SCREENWIDTH/35)) 
for i in range(3):
    cars.add(Car("redcar.png",i,(int(SCREENHEIGHT/20*12)),speed,SCREENWIDTH))

speed = random.randint(int(SCREENWIDTH/50),int(SCREENWIDTH/30))*(-1)
for i in range(3):
    cars.add(Car("bluecar.png",i,(int(SCREENHEIGHT/20*10)),speed,SCREENWIDTH))
# Rellotge de control
clock=pygame.time.Clock()


#bucle infinit de joc
while True:
    for car in pygame.sprite.spritecollide(FROG, cars,0):
        print("Collision")
        FROG.rect.x = SCREENWIDTH/2 - FROG.image.get_width()/2
        FROG.rect.y = SCREENHEIGHT-FROG.image.get_height()-(JUMP/2)
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

    for c in cars:
        c.paint(DISPLAYSURF)

    #redibuixem la pantalla
    pygame.display.update()
    clock.tick(10)