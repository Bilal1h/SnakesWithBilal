import pygame
from pygame import (
    K_ESCAPE, K_LCTRL, K_RETURN, K_SPACE, K_UP,K_DOWN,K_LEFT,K_RIGHT, K_a, K_q, K_r, K_s, K_w
)
from pygame import mixer
import pyautogui as pg
import random
import os
pygame.init()
mixer.init()
screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((900,600))
bgimg = pygame.image.load('images.png')
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("Snakes with Bilal")
pygame.display.update()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
font = pygame.font.SysFont(None,55)
clock = pygame.time.Clock()
gameover = False
exit_game = False
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    screen.blit(screen_text,[x,y])

def plot_snake(screen,color,snk_list,snake_size_width,snake_size_height):
    for x,y in snk_list:
        pygame.draw.rect(screen,black,[x,y,snake_size_width,snake_size_height])
def welcome():
    global exit_game
    global name
    exit_game = False
    while not exit_game:
        screen.fill((134,243,205))
        text_screen("Welcome To Snakes with Bilal!",black,170,260)
        text_screen("Press Space Bar to Play!",black,230,300)
        text_screen("Press ESC to Quit!",black,260,340)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                exit_game = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    gameloop()
                if event.key == K_ESCAPE:
                    exit_game = True
        pygame.display.flip()
        clock.tick(30)
        
def gameloop():
    global snake_size_width
    global snake_size_height
    snakes_x = 450
    snakes_y = 300
    snake_size_width = 40
    snake_size_height = 30
    
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    food_size = 25
    score = 0
    init_velocity = 8
    fps = 30
    
    snk_list = []
    snk_length = 1
    exit_game= False
    gameover = False
    if(not os.path.exists("hiscore.txt")):
        with open('hiscore.txt','w') as f:
            f.write("0")
    with open("hiscore.txt",'r') as f:
        hiscore = f.read()
    while not exit_game:
        if gameover:
            with open('hiscore.txt' , 'w') as f:
                f.write(str(hiscore))
            screen.fill((134,243,205))
            mixer.music.load("out.mp3")
            mixer.music.play()
            text_screen("Game Over! Press Enter To Continue",black,100,300)
            text_screen("Press ESC to Quit",black,260,350)
            text_screen("Score :"+str(score),black,330,400)
            for event in pygame.event.get():

                    # hiscore= int(hiscore)+int(score)
                
                    
                
                if event.type == pygame.QUIT:
                    exit_game = True
                    exit()
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # data = [score,hiscore]
                        # stri = str(data)
                        # res = [score if item == hiscore else item for item in data]
                        # strires = str(res)

                        gameloop()
                    if event.key == K_ESCAPE:
                        exit_game = True
                   
            init_velocity = 8
            

            
                
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        velocity_x = 0  
                        velocity_y = -init_velocity  
                        # snakes_y = snakes_y-10

                    if event.key == K_LEFT:
                        # snakes_x = snakes_x-10
                        velocity_x = -init_velocity  
                        velocity_y = 0  
                    if event.key == K_DOWN:
                        # snakes_y = snakes_y+10
                        velocity_x = 0  
                        velocity_y = init_velocity  
                    if event.key == K_RIGHT:
                        # snakes_x = snakes_x+10
                        velocity_x = init_velocity  
                        velocity_y = 0  
                    if event.key == K_q:
                        score +=50
                    if event.key == K_a:
                        # food_x1 = random.randint(40,screen_width/2)
                        # food_y1 = random.randint(40,screen_height/2)
                        # food_x2 = random.randint(40,screen_width/2)
                        # food_y2 = random.randint(40,screen_height/2)
                        # food_x3 = random.randint(40,screen_width/2)
                        # food_y3 = random.randint(40,screen_height/2)
                        # pygame.draw.rect(screen,red,[food_x1,food_y1,food_size,food_size])
                        # pygame.draw.rect(screen,red,[food_x2,food_y2,food_size,food_size])
                        # pygame.draw.rect(screen,red,[food_x3,food_y3,food_size,food_size])
                        snk_length += 10
                    if event.key == K_s:
                        init_velocity = init_velocity-1
                    if event.key == K_w:
                        init_velocity +=5
            snakes_x = snakes_x + velocity_x
            snakes_y = snakes_y + velocity_y

            if abs(snakes_x - food_x)<15 and abs(snakes_y - food_y)<15:
                score +=10
                food_x = random.randint(40,screen_width/2)
                food_y = random.randint(40,screen_height/2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score
                    # pg.alert(text=f"Congrats {name}! You created a New High Score", title='Status', button='OK')
               
                    
                if score!=100 or score!=200 or score!=300 or score!=400 or score!=500:
                    mixer.music.load("success.mp3")
                    mixer.music.play()
                if score==100 or score == 200 or score == 300 or score == 400 or score == 500:
                    mixer.music.load("eaten.mp3")
                    mixer.music.play()
                
                    # hisco = hiscore
                    # datasco = str(score)
                    # datahisco = str(hiscore)
                    # datahisco.replace(hisco,datasco)
                    # res = [score if item == hiscore else item for item in data]
                    
                    


            screen.fill(white)
            screen.blit(bgimg,(0,0))
            text_screen("Score :"+str(score),white,5,5)
            text_screen("Hiscore : "+ str(hiscore),white,650,5)
            
            apple = pygame.draw.rect(screen,red,[food_x,food_y,snake_size_width,snake_size_height])
            # sna = pygame.draw.rect(screen,black,[snakes_x,snakes_y,snake_size_width,snake_size_width_width])
            
            
            
            head = []
            head.append(snakes_x)
            head.append(snakes_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if snakes_x<0 or snakes_x>screen_width or snakes_y<0 or snakes_y > screen_height:
                gameover = True
            if head in snk_list[:-1]:
                gameover = True
           
            plot_snake(screen,black,snk_list,snake_size_width,snake_size_height)
        clock.tick(fps)
        pygame.display.flip()











    pygame.quit()
   
welcome()
gameloop()
