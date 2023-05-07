# File created by: DOminic Magana
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed it so that now I have a game over feature when you go off to the sides

# This file was created by: Dominic Magana
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/, 
# Sources: http:https://www.youtube.com/watch?v=iIb_xOs2a_E&t=1s
# Sources: https://www.youtube.com/watch?v=D40PKRyI1bQ
# Sources:  
# goals:I want to create a game over feature
# rules:

# import libs
import pygame
import sys
import time
import random
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

pg.init ()


game_screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Type Game")


# def drawtext(text, size, color, x, y):
#     font_name = pg.font.match_font('arial')
#     font = pg.font.Font(font_name, size)
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x,y)
#     game_screen.blit(text_surface, text_rect)


def snake():
    global x, y, food_x, food_y, game_over
    x = (x + delta_x) % WIDTH
    y = (y + delta_y) % HEIGHT

    if((x,y) in body_list):
        game_over = True
        return

    body_list.append((x,y))

    if(food_x == x and food_y == y):
        collect_sound.play()
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, WIDTH)//10*10, random.randrange(0,HEIGHT)//10*10 
    else:
        del body_list[0]
        
    game_screen.fill((0,0,0))
    score = font.render("Score: " + str(len(body_list)), True, (255,255,0))
    game_screen.blit(score,[0,0])
    pg.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])
    for (i,j) in body_list:
        pg.draw.rect(game_screen, (255,255,255), [i, j, 10, 10])
    pg.display.update()

while True:
    if game_over == True:
        game_screen.fill (WHITE) 
        msg = font.render("GAME OVER!", True, (255, 0, 0))
        game_screen.blit(msg, [WIDTH//3, HEIGHT//3])
        display_restart = font.render("Press Space to Restart", True, WHITE, (0,0,0))
        game_screen.blit(display_restart, (170,450))
        pg.display.update()
        time.sleep(10)
        pg.quit()
        quit()

        # game_screen.fill(WHITE)
        # drawtext("Game Over", 35, WHITE, WIDTH/2, HEIGHT/2)
        
    events = pg.event.get()
    for event in events:
        if(event.type == pg.QUIT):
            pg.quit()
            quit()
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_LEFT):
                if(delta_x != 10):
                    delta_x = -10
                delta_x = -10
                delta_y = 0
            elif(event.key == pg.K_RIGHT):
                if(delta_x != 10):
                    delta_x = 10
                delta_x = 10
                delta_y = 0
            elif(event.key == pg.K_UP):
                delta_x = 0
                if(delta_y != 10):
                    delta_y = -10
                delta_y = -10
            elif(event.key == pg.K_DOWN):
                delta_x = 0
                if(delta_y != -10):
                     delta_y = 10
            elif(event.key == pg.K_SPACE and game_over):
                score = 0
                game_over = False

            else:
                continue
            snake()
    if(not events):
        snake()
    clock.tick(10)
