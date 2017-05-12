import pygame
from pygame.locals import *
import sys
from sys import exit
from random import *

global SIZE
SIZE = input("Please input the size of maze:")

#colors
global line,blank,filled
line,blank,filled = (0,0,0),(255,255,255),(0,0,0)

pygame.init()
screen = pygame.display.set_mode((SIZE*20,SIZE*20),0,32)

#statu = 0 :blank ,statu = 1 : wall, statu = 2:visited
class Block(object):
    def __init__(self,idx,idy,statu):
        self.idx = idx
        self.idy = idy
        self.statu = statu
        self.a = ((idx-1)*20,(idy-1)*20)
        self.b = (idx*20,(idy-1)*20)
        self.c = ((idx-1)*20,idy*20)
        self.d = (idx*20,idy*20)

    def convert(self):
        if self.statu == 0: #blank
            pygame.draw.rect(screen,filled,self.a,(20,20)))
        else if self.statu == 1:
            pygame.draw.rect(screen,blank,self.a,(20,20)))


def DrawRect():
    for i in range(1,SIZE):
        pygame.draw.line(screen,line,(),()

def GenerateBlockInstance():
    pass


