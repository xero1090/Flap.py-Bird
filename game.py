# Flappy bird by Kevin Tran 991566232
# 5/1/2019

import pygame
from pygame.locals import *  
import sys
import random

class bird:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        # Stores rectangular coordinates
        self.bird = pygame.Rect(65, 50, 50, 50)
        # Loads background Image and changes the pixel format of an image
        self.background = pygame.image.load("images/background.png").convert()
        # Loads bird sprites and changes the pixel format of an img including ppa (per pixel alphas)
        self.birdsprites = [pygame.image.load("images/1.png").convert_alpha(),
                            pygame.image.load("images/2.png").convert_alpha(),
                            pygame.image.load("images/dead.png")]
        self.topPipe = pygame.image.load("images/bottom.png").convert_alpha()
        self.botPipe = pygame.image.load("images/top.png").convert_alpha()
        self.space = 130
        self.pipex = 400
        self.birdY = 350
        self.fly = 0
        self.flySpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)

        