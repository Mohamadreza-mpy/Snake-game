import pygame,sys,random
from pygame.locals import *
from tkinter import *
pygame.init()
#variables
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)
whit= (255,255,255)
black= (0,0,0)
yellow= (255,255,0)
gray= (30,30,30)
fps= 8
win_width= 400
#andaza safe
win_hieight= 400 
worm_x=180

worm_y=80
speed_worm_X=0
speed_worm_y=0
food_x=random.randrange(0,400,20)
food_y=random.randrange(0,400,20)
worm_list=[]
worm_sd=0
game_over=False
a=['r','l','u','d']
amtiaz=0
#--------------------------------------------------------
win = pygame.display.set_mode((win_width,win_hieight))
pygame.display.set_caption("snake")
clock= pygame.time.Clock()

def worm_fat(worm_list,worm_x,worm_y):
    g_over=False
    worm_head =[worm_x,worm_y]
    worm_list.append(worm_head)
#baray mar
    for lst in worm_list:
        
        pygame.draw.rect(win,yellow,(lst[0],lst[1],20,20))
    for each_section in worm_list[:-1]:
        if each_section==worm_head:
            g_over=True
    return g_over
#----------------------------------------------------
#bara harekat
while not game_over:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_RIGHT and "r" in a:
                speed_worm_X = 20
                speed_worm_y=0
                a.clear()
                a.append('l')
                a.append('u')
                a.append('d')
            elif event.key==K_LEFT and "l" in a:
                speed_worm_X= -20
                speed_worm_y=0
                a.clear()
                a.append('r')
                a.append('u')
                a.append('d')
            elif event.key==K_DOWN and "d" in a:
                speed_worm_y=20
                speed_worm_X=0
                a.clear()
                a.append('r')
                a.append('u')
                a.append('l')
            elif event.key==K_UP and "u" in a:
                speed_worm_y= -20
                speed_worm_X=0
                a.clear()
                a.append('r')
                a.append('l')
                a.append('d') 
                    
#------------------------------------------------
    worm_x += speed_worm_X
    worm_y += speed_worm_y
    if worm_x < 0:
      worm_x =400
    if worm_x > 400:
        worm_x=0
    if worm_y < 0:
        worm_y=400
    if worm_y > 400:
        worm_y= 0
    if worm_x==food_x and worm_y==food_y:
        food_x= random.randrange(0,400,20)
        food_y= random.randrange(0,400,20)
        worm_sd += 1
        amtiaz += 10
        print(amtiaz)
    
        
    if len(worm_list) > worm_sd :
        worm_list.pop(0) 
#-----------------------------------------------------
#safe namaesh
    win.fill(blue)
    
    if worm_fat(worm_list,worm_x,worm_y):
         game_over=True 
         print('game over')
    pygame.draw.rect(win,red,(food_x,food_y,20,20))
    pygame.display.update()
    clock.tick(fps)
        

       