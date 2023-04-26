import pygame
import random
import math
import time
from pygame import mixer


# initialize oygame
pygame.init()
# creating a game window
# width, height
screen = pygame.display.set_mode((1000, 800))

# title and icon
pygame.display.set_caption("Snake")
background=pygame.image.load("images (1).jpeg")

# mixer.music.load("bg_music.mp3")
# mixer.music.play(-1)
# importing snake head img

# snake_headimg = pygame.image.load("snake_head_img.png")
# snake_headX = random.randint(80, 920)
# snake_headY = random.randint(80, 720)

snake_head_state = "play"

snake_body_img=[]
snake_bodyX=[]
snake_bodyY=[]
snake_bodyX.append(80)
snake_bodyY.append(80)
snake_headX_change = 0
snake_headY_change = 0

if snake_head_state!='rest':
    mixer.music.load("bg_music.mp3")
    mixer.music.play(-1)

snake_body_img.append(pygame.image.load("snake_head(1).jpeg"))
snake_body_img.append(pygame.image.load("snake.jpg"))



def snake_head(x, y, state):
    if state == "play":
        screen.blit(snake_body_img[0], (x, y))

def snake_body(x, y, state):
    if state == "play":
        screen.blit(snake_body_img[1], (x, y))

# importing fruit
fruitimg = pygame.image.load("fruit(1).png")
fruitX = int(random.uniform(0,1)*((920/40)))*40 +40
fruitY = int(random.uniform(0,1)*((720/40)))*40 +40


def fruit(x, y):
    screen.blit(fruitimg, (x, y))


def is_collision(x, y, z, w):
    distance = math.sqrt((math.pow(x-z, 2))+(math.pow(y-w, 2)))
    if distance < 30:
        return True
    else:
        return False


# importing tail
# snake_body_img=[]
# snake_bodyX=[]
# snake_bodyY=[]
# snake_bodyX.append(snake_headX)
# snake_bodyY.append(snake_headY)

# for i in range(100):
#     snake_body_img.append(pygame.image.load("snake copy.png"))

color=(0,0,0)

running = True
# game loop
# infinitely running
while running:

    screen.fill((255, 255, 255))
    screen.blit(background,(40,40))
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, 1000, 800),  40)
    # checking for events in game windiw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                snake_headY_change = 0
                snake_headX_change = -20
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                snake_headX_change = 0
                snake_headY_change = -20
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                snake_headX_change = 0
                snake_headY_change = 20
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                snake_headY_change = 0
                snake_headX_change = 20

    

    # boundary detection
    if  snake_bodyX[0]<= 20:
        snake_bodyX[0] = 20
        snake_head_state = "rest"
        # end_sound=mixer.Sound("collision.mp3")
        # end_sound.play()
    if  snake_bodyX[0] >= 950:
        snake_bodyX[0] = 950
        snake_head_state = "rest"
        # end_sound=mixer.Sound("collision.mp3")
        # end_sound.play()
    if  snake_bodyY[0] <= 20:
        snake_bodyY[0] = 20
        snake_head_state = "rest"
        # end_sound=mixer.Sound("collision.mp3")
        # end_sound.play()
    if  snake_bodyY[0] >= 740:
        snake_bodyY[0] = 740
        snake_head_state = "rest"
        # end_sound=mixer.Sound("collision.mp3")
        # end_sound.play()

    # snake_bodyX[0]=snake_headX
    # snake_bodyY[0]=snake_headY
    

    fruit(fruitX, fruitY)
    # appearing of snake head on the screen
    

    collision = is_collision( snake_bodyX[0],  snake_bodyY[0], fruitX, fruitY)
    
   
        
        

    if collision:
        eat_sound=mixer.Sound('eat.mp3')
        eat_sound.play()
        snake_bodyX.append(-80)
        snake_bodyY.append(-80)
        fruit(fruitX,fruitY)
        fruitX = int(random.uniform(0,1)*((920/40)))*40 +40
        fruitY = int(random.uniform(0,1)*((720/40)))*40 +40

    for i in range(len(snake_bodyX)-1,-1,-1):
        if i==0:
            snake_head( snake_bodyX[i],  snake_bodyY[i], snake_head_state)
        
        if i!=0:
            snake_body( snake_bodyX[i],  snake_bodyY[i], snake_head_state)
            snake_bodyX[i]=snake_bodyX[i-1]
            snake_bodyY[i]=snake_bodyY[i-1]
            
    snake_bodyX[0] = snake_bodyX[0]+snake_headX_change
    snake_bodyY[0] = snake_bodyY[0]+snake_headY_change
    for i in range(len(snake_bodyX)-1,0,-1):
        if snake_bodyX[0]==snake_bodyX[i] and snake_bodyY[0]==snake_bodyY[i]:
            snake_head_state="rest"
            # end_sound=mixer.Sound("collision.mp3")
            # end_sound.play()
    
    # print(snake_bodyX[0])
    # print(snake_bodyY[0])  
    
    time.sleep(0.1)
    # updating screen in continuous time
    pygame.display.update()