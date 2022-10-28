from pickle import TRUE
from turtle import Screen
import pygame
import time
import math

pygame.init()
GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
total_secs = 0
total=0
start=False

sound = pygame.mixer.Sound('oniichan.wav')

font = pygame.font.SysFont('sans',50)
text1= font.render('+',True,BLACK)
text2= font.render('-',True,BLACK)
text3= font.render('+',True,BLACK)
text4= font.render('-',True,BLACK)
text5= font.render('Start',True,BLACK)
text6= font.render('Reset',True,BLACK)


screen = pygame.display.set_mode((500,600))

running =True
clock=pygame.time.Clock()
#Bắt đầu chương trình
while running: 
    clock.tick(60)
    #Tọa độ ấn chuột
    mouseX,mouseY = pygame.mouse.get_pos()
    #print(mouseX)

    screen.fill(GREY) #thay đổi màu màn hình
    
    #draw text

    # draw.rect : Vẽ hình vuông 
    pygame.draw.rect(screen,WHITE,(100,50,50,50)) # (100,50,50,50) là tọa độ trên màn hình , rộng
    pygame.draw.rect(screen,WHITE,(100,200,50,50))
    pygame.draw.rect(screen,WHITE,(200,50,50,50))
    pygame.draw.rect(screen,WHITE,(200,200,50,50))
    pygame.draw.rect(screen,WHITE,(300,50,150,50))
    pygame.draw.rect(screen,WHITE,(300,150,150,50))
    
    screen.blit(text1,(100,50))
    screen.blit(text2,(100,200))
    screen.blit(text3,(200,50))
    screen.blit(text4,(200,200))
    screen.blit(text5,(300,50))
    screen.blit(text6,(300,150))

    
    pygame.draw.rect(screen,BLACK,(50,520,400,50))
    pygame.draw.rect(screen,WHITE,(60,530,380,30))
    
    
    # Vẽ hình tròn : tọa độ tâm + bán kính
    pygame.draw.circle(screen,BLACK,(250,400),100)
    pygame.draw.circle(screen,WHITE,(250,400),95)
    pygame.draw.circle(screen,BLACK,(250,400),5)
    #Vẽ đường thẳng ((X1,Y1),(X2,Y2))
   # pygame.draw.line(screen,BLACK,(250,400),(250,310))
    
    for event in pygame.event.get():
        
        #Tương tác chuột

        if event.type== pygame.QUIT:    #Khởi tạo nút close
            running = False
            # Nếu bấm chuột trái 
        if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button==1: 
                pygame.mixer.pause()
                if(100<mouseX<150) and (50<mouseY<100):
                    total_secs+=60
                    total = total_secs
                    print("press + min")   
                if(300<mouseX<450) and (50<mouseY<100):
                    start = True
                    total = total_secs
                    print("press Start")
                if(200<mouseX<250) and (50<mouseY<100):
                    total_secs+=1
                    total = total_secs
                    print("press + sec")
                if(100<mouseX<150) and (200<mouseY<250):
                    total_secs-=60
                    total = total_secs
                    print("press - min")
                if(200<mouseX<250) and (200<mouseY<250):
                    total_secs-=1
                    total = total_secs
                    print("press - sec")
                if(300<mouseX<450) and (150<mouseY<200):
                    total_secs = 0
                    print("press Reset")  
                print("total_secs: " + str(total_secs))
        
       
    mins = int(total_secs/60 ) 
    secs =  total_secs - 60*mins
        #print(mins)

    if start:
        total_secs-=1
        if total_secs==0:
            start=False
            pygame.mixer.Sound.play(sound)
        time.sleep(0.03)
    if total_secs < 0:
        start=False
        total_secs =0
    time_now=str(mins) +":"+ str(secs)
    text_time=font.render(time_now,True,BLACK)
    screen.blit(text_time,(120,120))
   
    # Vẽ kim giay
    x_sec = 250+90*math.sin(6*secs*math.pi/180)
    y_sec = 400-90*math.cos(6*secs*math.pi/180)
    pygame.draw.line(screen,RED,(250,400),(int(x_sec),int(y_sec)))
    #Vẽ kim phut
    x_min = 250+40*math.sin(6*mins*math.pi/180)
    y_min = 400-40*math.cos(6*mins*math.pi/180)
    pygame.draw.line(screen,RED,(250,400),(int(x_min),int(y_min)))

    if total!= 0:
        pygame.draw.rect(screen,RED,(60,530,380*(total_secs/total),30))      

    
    pygame.display.flip()


pygame.quit()# xóa bộ nhớ khi chương trình chạy xong
