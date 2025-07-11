import pygame
import random

pygame.init()
width, height =600,600

game_screen =pygame.display.set_mode((width, height))
pygame.display.set_caption("Lokesh games 1")

snake_x, snake_y = width/2, height/2
change_x, change_y =0, 0

def display_snake():
    global snake_x, snake_y
    snake_x =snake_x + change_x
    snake_y =snake_y + change_y


    pygame.draw.rect(game_screen,(255,255,255),[snake_x, snake_y,10,10])
    pygame.display.update()


while True:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.QUIT
            quit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                   change_x = -10
                   change_y = 0
                 (event.key == pygame.K_UP):
                    change_x = 0
                    change_y = -10
                elif(event.key == pygame.K_RIGHT):
                    change_x = 10
                    change_y = 0
                elif(event.key == pygame.K_DOWN):
                    change_x = 0
                    change_y = 10
        display_snake()
             
                 



