# File created by: DOminic Magana
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed it so that now I have a game over feature when you go off to the sides

# This file was created by: Dominic Magana
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
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

x, y = 200, 200
delta_x, delta_y = 0, 0

def snake():
    global x, y
    x = (x + delta_x) % WIDTH
    y = (y + delta_y) % HEIGHT
    game_screen.fill((0,0,0))
    pg.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
    pg.display.update()
while True:
    events = pg.event.get()
    for event in events:
        if(event.type == pg.QUIT):
            pg.quit()
            quit()
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_LEFT):
                delta_x = -10
                delta_y = 0
            elif(event.key == pg.K_RIGHT):
                delta_x = 10
                delta_y = 0
            elif(event.key == pg.K_UP):
                delta_x = 0
                delta_y = -10
            elif(event.key == pg.K_DOWN):
                delta_x = 0
                delta_y = 10
            else:
                continue
            snake()
    if(not events):
        snake()

