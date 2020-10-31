# import modules
import pygame,sys
import os
import pygame.freetype
import time

pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
PlayerFront = pygame.image.load('Sprites/Player/Bill.png')
PlayerBack = pygame.image.load('Sprites/Player/Bill back.png')
PlayerRight = pygame.image.load('Sprites/Player/Bill right.png')
PlayerLeft = pygame.image.load('Sprites/Player/Bill left.png')

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Collison test')

class player():
    self.Facing_Right = False
    self.Facing_Left = False
    self.Facing_Up = False
    self.Facing_Left = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
