import sys
import pygame

Width=950
Height=950

Red=0
Green=0
Blue=0

program_onn=True

print ("                               ")
print ("    ########             #     ")
print ("  ##        #            #     ")
print (" #                       #     ")
print (" #      ######           #     ")
print ("  ###     ####           #     ")
print ("    #######   OOD        # MAGE")
print ("                               ")
print ("Good program for good image    ")
print ("                               ")

pygame.init()

sc = pygame.display.set_mode((950, 950))
pygame.display.set_caption("GoodImage")
previus_pos = None

sc.fill((255, 255, 255))

def line_dragged(pos):
    global previus_pos
    if previus_pos is not None:
        pygame.draw.line(sc, (Red, Green, Blue), previus_pos, pos, 5)

    previus_pos=pos

while program_onn:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            program_onn = False
            pygame.quit()
        elif e.type==pygame.KEYDOWN:
            if e.key==pygame.K_0:
                Red=255
                Green=255
                Blue=255
            elif e.key==pygame.K_1:
                Red=0
                Green=0
                Blue=0
            elif e.key==pygame.K_2:
                Red=255
                Green=0
                Blue=0
            elif e.key==pygame.K_3:
                Red=255
                Green=255
                Blue=0
            elif e.key==pygame.K_4:
                Red=0
                Green=255
                Blue=0
            elif e.key==pygame.K_5:
                Red=0
                Green=255
                Blue=255
            elif e.key==pygame.K_6:
                Red=0
                Green=190
                Blue=255
            elif e.key==pygame.K_7:
                Red=0
                Green=0
                Blue=255
            elif e.key==pygame.K_8:
                Red=128
                Green=0
                Blue=128
            elif e.key==pygame.K_9:
                Red=255
                Green=0
                Blue=128
        elif e.type == pygame.MOUSEMOTION:
            if e.buttons == (1,0,0):
                line_dragged(e.pos)
            else:
                previus_pos = None
                pygame.display.update()
    pygame.time.delay(1)

pygame.quit()
sys.exit()
