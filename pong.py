
import pygame, sys
from pygame.locals import*
FPS=200
windowidth=400
windowhight=300
def main():
    pygame.init()
    global DISPLAYSURF
    
    FPSclock=pygame.time.clock()
    DISPLAYSURF=pygame.display.set_mode((windowwith,windowhight))
    pyhame.display.set_caption('Pong')
    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSclock.tick(FPS)

if __name__=='__main__':
    main()

