# Flappy bird by Kevin Tran, (add your name here)
# 5/1/2019

import pygame
from pygame.locals import *  
import sys
import random
import os

class Bird:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        # Stores rectangular coordinates
        self.bird = pygame.Rect(65, 50, 50, 50)
        # Loads background Image and changes the pixel format of an image
        self.background = pygame.image.load("images/background.png").convert()
         # Loads bird sprites and changes the pixel format of an img including ppa (per pixel alphas)
        self.birdSprites = [pygame.image.load("images/1.png").convert_alpha(),
                            pygame.image.load("images/2.png").convert_alpha(),
                            pygame.image.load("images/dead.png")]
        self.wallUp = pygame.image.load("images/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("images/top.png").convert_alpha()
        self.death = False
        self.spriteNum = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(1)
            keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                self.spriteNum = 1
    def run(self):
        while True:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            pygame.display.update()

Bird().run()

