import pygame
from pygame.locals import *
import sys
from sys import exit
from random import *

global SIZE
SIZE = input("Please input the size of maze:")
print "Press g to generate the maze."

global maze_color
maze_color = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((SIZE*10+20,SIZE*10+20),0,32)

sys.setrecursionlimit(10000)

class Block(object):
    #statu: 0:blank 1:wall 2:has visited
    def __init__(self,x,y,statu):
        self.x = x
        self.y = y
        self.statu = statu;
        self.id = ((x)/10,(y)/10)

def DrawRect():
    pygame.draw.line(screen,maze_color,(15,15),(SIZE*10+5,15))
    pygame.draw.line(screen,maze_color,(15,15),(15,SIZE*10+5))
    pygame.draw.line(screen,maze_color,(15,SIZE*10+5),(SIZE*10+5,SIZE*10+5))
    pygame.draw.line(screen,maze_color,(SIZE*10+5,15),(SIZE*10+5,SIZE*10+5))

def GenerateBlocks():
    global d
    d = {}
    for i in range(15,SIZE*10+6,10):
        for j in range (15,SIZE*10+6,10):
            idx,idy= i/10,j/10
            if ((idx == 1 or idx == SIZE) or (idy == 1 or idy == SIZE )):
                d[((i)/10,(j)/10)] = Block(i,j,1)
                #if (idx == 1 and idy==1) or (idx == 1 and idy == 2):
                #    d[(i/10,j/10)].statu=0
            else:
                d[((i)/10,(j)/10)] = Block(i,j,0)

def GenerateMaze(point):
    point.statu = 1
    all_choice = [(1,0),(0,1),(-1,0),(0,-1)]
    while True:
        if len(all_choice) != 0:
            choice = all_choice[randint(0,len(all_choice)-1)]
            all_choice.remove(choice)
            #in the maze
            if point.id[0] + choice[0] > 0 and point.id[0] + choice[0] <=SIZE and point.id[1] + choice[1] > 0 and point.id[1] + choice[1] <=SIZE:
                nextpoint = d[(point.id[0] + choice[0],point.id[1]+choice[1])]
                if nextpoint.statu == 0:
                    pygame.draw.line(screen,maze_color,(point.x,point.y),(nextpoint.x,nextpoint.y),2)
                    GenerateMaze(nextpoint)
        
        else:
            return

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            #Generate Maze Part
            if event.key == K_g:
                screen.fill((255,255,255))
                DrawRect()
                GenerateBlocks()
                GenerateMaze(d[((randint(2,SIZE-1)),(randint(2,SIZE-1)))])
                
        pygame.display.update()
