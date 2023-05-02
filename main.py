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
pg.display.set_caption("Sanke Type Game")

def drawsnake():
    pg.draw.rect(game_screen, (255, 255, 255), [10, 10])

def update():
    drawsnake()

while True:
    events = pg.event.get()
    for event in events:
        if(event.type == pg.QUIT):
            pg.quit()
            quit()



