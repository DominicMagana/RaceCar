import pygame
import sys
import time
import random
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *

pg.init()

WIDTH = 400
HEIGHT = 400
WHITE = (225,255,225)
# For the music
music = pg.mixer.music.load('Fluffing-a-Duck.mp3')
pg.mixer.music.play(-1)
collect_sound = pg.mixer.Sound('Collect.mp3')
x, y = 200, 200
delta_x, delta_y = 10, 0
food_x, food_y = random.randrange(0, WIDTH)//10*10, random.randrange(0,HEIGHT)//10*10 
body_list = [(x,y)]
clock = pg.time.Clock()
game_over = False
font = pg.font.SysFont("Ariel", 25)
