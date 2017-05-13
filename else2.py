#coding:utf-8
import pygame
from pygame.locals import *
import sys
from sys import exit
from random import *

global SIZE
SIZE = input("Please input the size of maze:")

global linecolor
linecolor = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((SIZE*10,SIZE*10),0,32)

sys.setrecursionlimit(10000)

class Cell(object):
    def __init__(self,x,y,statu):
        #x,y为左上角坐标
        #statu = 0 未访问　statu = 1　已访问过       
        self.x,self.y,self.statu = x,y,statu
        #0 没墙，1有墙
        self.up,self.right,self.down,self.left = 1,1,1,1
        self.walls = [self.up,self.right,self.down,self.left]
        self.id = (x/10,y/10)

    def draw(self):
        if self.walls[0] == 1:
            pygame.draw.line(screen,linecolor,(self.x,self.y),(self.x+10,self.y))
        if self.walls[1] == 1:
            pygame.draw.line(screen,linecolor,(self.x+10,self.y),(self.x+10,self.y+10))
        if self.walls[2] == 1:
            pygame.draw.line(screen,linecolor,(self.x+10,self.y+10),(self.x,self.y+10))
        if self.walls[3] == 1:
            pygame.draw.line(screen,linecolor,(self.x,self.y+10),(self.x,self.y))

def GenerateCells():
    global AllCells
    AllCells = {}
    for i in range(0,SIZE*10,10):
        for j in range(0,SIZE*10,10):
            idx,idy = i/10,j/10
            AllCells[(idx,idy)] = Cell(i,j,0)
            '''
            if idy == 0:
               AllCells[(idx,idy)].walls[0] = 2
            if idx == 0:
                AllCells[(idx,idy)].walls[3] = 2
            if idy == SIZE-1:
                AllCells[(idx,idy)].walls[2] = 2
            if idx == SIZE-1:
                AllCells[(idx,idy)].walls[1] = 2
            '''

def DrawAll():
    #for i in range(len(AllCells.keys())):
        #print len(AllCells.values())
        #print AllCells.values()[i].id,AllCells.values()[i].statu,AllCells.values()[i].walls
        #print AllCells.values()[i].statu,
    for i in range(0,SIZE*10,10):
        for j in range(0,SIZE*10,10):
            idx,idy = i/10,j/10
            AllCells[(idx,idy)].draw()       



def next(nowCell):
    temp = [0,0,0,0]
    


def backtrack(nextCell):
    pass

'''
def Next(cell):
    cell.statu = 1
    #up,right,down,left
    all_choice = [[0,1],[1,0],[0,-1],[-1,0]]
    print cell.id,cell.walls
    while len(all_choice)>0:
        random_choice = randint(0,len(all_choice)-1)
        choice = all_choice[random_choice]
        all_choice.remove(choice)
        if cell.id[0] + choice[0] >= 0 and cell.id[0] + choice[0] <SIZE and cell.id[1] + choice[1] >= 0 and cell.id[1] + choice[1] <SIZE:
            nextcell = AllCells[(cell.id[0]+choice[0],cell.id[1]+choice[1])]
            if nextcell.statu == 0:
                if random_choice == 0 :
                    cell.walls[0] = 0 
                    nextcell.walls[2] = 0
                elif random_choice == 1:
                    cell.walls[1] == 0
                    nextcell.walls[3] = 0
                elif random_choice == 2:
                    cell.walls[2] = 0
                    nextcell.walls[0] = 0
                elif random_choice == 3:
                    cell.walls[3] = 0
                    nextcell.walls[1] = 0
                Next(nextcell)
    else:
       return
'''


#Pygame
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_g:
                screen.fill((255,255,255))
                GenerateCells()
                Next(AllCells[(SIZE/2,SIZE/2)])
                DrawAll()

        pygame.display.update()
