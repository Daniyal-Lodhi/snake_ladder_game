running=True
from random import *
import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((1000,700))
button= pygame.Rect(5,30,64,64)
bg=pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\snakeladder new.png')
pawn_1=pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\pawn.png')
pawn_2=pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\pawn 2.png')
pawn2_resize=pygame.transform.scale(pawn_2,(55,60))
play=pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\button..png')
bg_resize=pygame.transform.scale(bg,(600,650))
font2=pygame.font.SysFont('comicsansms',32)
font12=pygame.font.SysFont('comicsansms',25)
bgx=400
bgy=1
pnx=50
pny=140
pn2x=50
pn2y=240
def bng():
    screen.blit(bg_resize, (bgx, bgy))
    screen.blit(play,(5,30))
def pawns():
    screen.blit(pawn_1,(pnx,pny))
    screen.blit(pawn2_resize,(pn2x,pn2y))
def font1(x,y):
    font=pygame.font.Font('freesansbold.ttf',32)
    appear=font.render('click to roll dice',True,(0,0,0))
    screen.blit(appear,(x,y))
def dices():
    roll=random.randint(1 , 6)
    if roll == 1:
        dice=pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\d1.png')
    elif roll == 2:
        dice = pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\d2.png')
    elif roll == 3:
        dice = pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\d3.png')
    elif roll == 4:
        dice = pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\d4.png')
    elif roll == 5:
        dice = pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\d5.png')
    elif roll == 6:
        dice = pygame.image.load('C:\\Users\\daniyal\\Pictures\\Saved Pictures\\d6.png')
    return (dice,roll)
def playersname():
    msg1=font2.render('PLAYER 1',True,(255,0,0 ))
    screen.blit(msg1,(30,100))
    msg2 =font2.render('PLAYER 2', True, (137, 207, 240))
    screen.blit(msg2, (30, 200))
def roll1():
    msg3=font12.render('Your Turn',True,(0,0,0))
    screen.blit(msg3,(200,120))
def roll2():
    msg4=font12.render('Your Turn',True,(0,0,0))
    screen.blit(msg4,(200,220))
def pl1won():
    font3=pygame.font.SysFont('algerian',30)
    appear1=font3.render('CONGRATZ PLAYER 1',True,(255,0,0))
    appear1 = font3.render('CONGRATZ PLAYER 1', True, (255, 0, 0))
    appear2 = font3.render('YOU WON', True, (255, 0, 0))
    screen.blit(appear1, (50,500))
    screen.blit(appear2, (95,550))
def pl2won():
    font3=pygame.font.SysFont('algerian',30)
    appear1=font3.render('CONGRATZ PLAYER 2',True,(0,0,255))
    appear2 = font3.render('YOU WON', True, (0, 0, 255))
    screen.blit(appear1,(50,500))
    screen.blit(appear2, (95,550))
turn='red'
while running:
    screen.fill((255, 229, 180))
    if turn == 'red':
        roll1()
    if turn == 'blue':
        roll2()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
        if event.type == pygame.MOUSEBUTTONDOWN:
           mp=pygame.mouse.get_pos()
           if button.collidepoint(mp):
              dices()
              dice,roll=dices()
              screen.blit(dice,(100,40))
              print(roll)
           if dices() and turn == 'red':
               turn = 'blue'
               if roll == 6 and pnx == 50 and pny == 140 :
                   pnx = 410
                   pny = 570
                   turn='red'
               elif  pnx in range(410,1000) and pny == 570:
                   pnx += roll * 60
                   if pnx>1000:
                       pny = 510
                       abovet = pnx
                       t = pnx - 1000
                       pnx = 400 + t
                   elif pnx == 530:
                      pnx=410
                      pny=270
                   elif pnx == 710:
                       pnx=770
                       pny=450
               elif pnx in range(410, 1000) and pny == 510:
                    pnx+=roll*60
                    if pnx>1000:
                       abovet=pnx
                       pny = 450
                       t = pnx-1000
                       pnx=400+t
                    elif pnx == 950 :
                        pnx=950
                        pny=200
               elif pnx in range(410, 1000) and pny in range (440,471):
                    pnx += roll * 60
                    if pnx > 1000:
                        pny = 390
                        abovet = pnx
                        t = pnx - 1000
                        pnx = 400 + t
                    elif pnx == 650 :
                        pnx =650
                        pny =570
               elif pnx in range(410, 1000) and pny in range(380,400):
                    pnx += roll * 60
                    if pnx > 1000:
                        pny = 330
                        abovet = pnx
                        t = pnx - 1000
                        pnx = 400+t
                    elif pnx == 710:
                        pnx = 650
                        pny = 270
                    elif pnx ==590:
                        pnx = 410
                        pny = 570
               elif pnx in range(410, 1000) and pny == 330:
                    pnx += roll * 60
                    if pnx > 1000:
                        pny = 260
                        abovet = pnx
                        t = pnx - 1000
                        pnx = 400 + t
                    elif pnx == 770:
                        pnx = 890
                        pny = 510
               elif pnx in range(410, 1000) and pny in range(260,271):
                            pnx += roll * 60
                            if pnx > 1000:
                                pny = 200
                                abovet = pnx
                                t = pnx - 1000
                                pnx = 400 + t
               elif pnx in range(410, 1000) and pny in range(190,211):
                    pnx += roll * 60
                    if pnx > 1000:
                        pny = 135
                        abovet = pnx
                        t = pnx - 1000
                        pnx = 400+t
                    elif pnx == 530:
                        pnx = 650
                        pny = 7
                    elif pnx == 830 :
                        pnx = 830
                        pny = 7
                    elif pnx == 650:
                        pnx = 470
                        pny = 270
               elif pnx in range(410,1000) and pny in range(135,150):
                   pnx += roll * 60
                   if pnx > 1000:
                       pny = 70
                       abovet = pnx
                       t = pnx - 1000
                       pnx = 400 + t
               elif pnx in range(410,1000) and pny in range(60,91):
                   pnx += roll * 60
                   if pnx > 1000:
                       pny = 0
                       abovet = pnx
                       t = pnx - 1000
                       pnx = 400 + t
                   elif pnx == 770:
                       pnx = 770
                       pny = 270
               elif pnx in range(410, 1000) and pny in range(0, 30):
                    x= pnx
                    pnx+=roll*60
                    if pnx>1000:
                        pnx=x
                    elif pnx == 1000:
                        pnx=1000
                    elif pnx == 890:
                        pnx = 890
                        pny = 190
                    elif pnx == 410:
                        pnx = 410
                        pny = 190




           elif dices() and turn == 'blue':
               turn = 'red'
               if roll == 6 and pn2x == 50 and pn2y == 240 :
                   pn2x = 410
                   pn2y = 570
                   turn='blue'
               elif pn2x in range(410, 1000) and pn2y == 570:
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 510
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 530:
                       pn2x = 410
                       pn2y = 270
                   elif pn2x == 710:
                       pn2x = 770
                       pn2y = 450
               elif pn2x in range(410, 1000) and pn2y == 510:
                   pn2x += roll * 60
                   if pn2x > 1000:
                       abovet = pn2x
                       pn2y = 450
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 950:
                       pn2x = 950
                       pn2y = 200
               elif pn2x in range(410, 1000) and pn2y in range(440,471):
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 390
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 650:
                       pn2x = 650
                       pn2y = 570
               elif pn2x in range(410, 1000) and pn2y in range(380,400):
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 330
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 710:
                       pn2x = 650
                       pn2y = 270
                   elif pn2x == 590:
                       pn2x = 410
                       pn2y = 570
               elif pn2x in range(410, 1000) and pn2y == 330:
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 260
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 770:
                       pn2x = 890
                       pn2y = 510
               elif pn2x in range(410, 1000) and pn2y in range(260, 271):
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 200
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
               elif pn2x in range(410, 1000) and pn2y in range(190, 211):
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 135
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 530:
                       pn2x = 650
                       pn2y = 7
                   elif pn2x == 830:
                       pn2x = 830
                       pn2y = 7
                   elif pn2x == 650:
                       pn2x = 470
                       pn2y = 270
               elif pn2x in range(410, 1000) and pn2y in range(135, 150):
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 70
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
               elif pn2x in range(410, 1000) and pn2y in range(60, 91):
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2y = 0
                       abovet = pn2x
                       t = pn2x - 1000
                       pn2x = 400 + t
                   elif pn2x == 770:
                       pn2x = 770
                       pn2y = 270
               elif pn2x in range(410, 1000) and pn2y in range(0, 30):
                   x = pn2x
                   pn2x += roll * 60
                   if pn2x > 1000:
                       pn2x = x
                   elif pn2x == 1000:
                       pn2x = 1000
                   elif pn2x == 890:
                       pn2x = 890
                       pn2y = 190
                   elif pn2x == 410:
                       pn2x = 410
                       pn2y = 190

    if pnx in range(950,1000) and pny in range(0, 30):
        pl1won()
    elif pn2x in range(950,1000) and pn2y in range(0, 30):
        pl2won()
    playersname()
    bng()
    pawns()
    font1(1,1)
    pygame.display.update()
    time.sleep(1)
