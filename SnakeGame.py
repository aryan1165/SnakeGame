import pygame
import random
import math
import time


pygame.init()
# creating a game window
# width, height
screen = pygame.display.set_mode((1000, 800))

# title and icon
pygame.display.set_caption("Snake")

# importing snake head img

# snake_headimg = pygame.image.load("snake_head_img.png")
# snake_headX = random.randint(80, 920)
# snake_headY = random.randint(80, 720)
snake_headX_change = 0
snake_headY_change = 0
snake_head_state = "play"

snake_body_img=[]
snake_bodyX=[]
snake_bodyY=[]
snake_bodyX.append(80)
snake_bodyY.append(80)
snake_headX_change = 0
snake_headY_change = 0


for i in range(1):
    snake_body_img.append(pygame.image.load("snake_head_img.png"))


def snake_head(x, y, state):
    if state == "play":
        screen.blit(snake_body_img[0], (x, y))

# importing fruit
fruitimg = pygame.image.load("fruit.png")
fruitX = int(random.uniform(0,1)*((920/40)))*40 +40
fruitY = int(random.uniform(0,1)*((720/40)))*40 +40


def fruit(x, y):
    screen.blit(fruitimg, (x, y))


def is_collision(x, y, z, w):
    distance = math.sqrt((math.pow(x-z, 2))+(math.pow(y-w, 2)))
    if distance < 20:
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



running = True
# game loop
# infinitely running
while running:

    screen.fill((255, 255, 255))
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
    if  snake_bodyX[0]<= 40:
        snake_bodyX[0] = 40
        snake_head_state = "rest"
    if  snake_bodyX[0] >= 960:
        snake_bodyX[0] = 960
        snake_head_state = "rest"
    if  snake_bodyY[0] <= 40:
        snake_bodyY[0] = 40
        snake_head_state = "rest"
    if  snake_bodyY[0] >= 760:
        snake_bodyY[0] = 760
        snake_head_state = "rest"

    # snake_bodyX[0]=snake_headX
    # snake_bodyY[0]=snake_headY
    

    fruit(fruitX, fruitY)
    # appearing of snake head on the screen
    

    collision = is_collision( snake_bodyX[0],  snake_bodyY[0], fruitX, fruitY)

    

    if collision:
        snake_bodyX.append(-80)
        snake_bodyY.append(-80)
        fruit(fruitX,fruitY)
        fruitX = random.randint(80, 920)
        fruitY = random.randint(80, 720)

    for i in range(len(snake_bodyX)-1,-1,-1):
        
        snake_head( snake_bodyX[i],  snake_bodyY[i], snake_head_state)
        if i!=0:
            snake_bodyX[i]=snake_bodyX[i-1]
            snake_bodyY[i]=snake_bodyY[i-1]
            
    snake_bodyX[0] = snake_bodyX[0]+snake_headX_change
    snake_bodyY[0] = snake_bodyY[0]+snake_headY_change
    for i in range(len(snake_bodyX)-1,0,-1):
        if snake_bodyX[0]==snake_bodyX[i] and snake_bodyY[0]==snake_bodyY[i]:
            snake_head_state="rest"
    
    # print(snake_bodyX[0])
    # print(snake_bodyY[0])  
    
    time.sleep(0.1)
    # updating screen in continuous time
    pygame.display.update()