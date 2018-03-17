#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:41:19 2018

@author: serge
"""
import random


class Minesweeper:
    
    #point = [position1, position2, ...]; position1 = 20, position2 =  37...
    field = []  #the whole field
    mines = []  #list of all mines
    flags = []  #            flags
    zeros = []  #            zeros
    
    openL = []  #            opened cells
    restL = []  #            unopened cells 
    
    fieldSize = (0,0)
    total = 0
    
    flagsLeft = len(mines)
    cellsLeft = len(restL)
    
    #Order of field numeration:
    '''
        0     1     2     3  ...
    0 (0,0) (1,0) (2,0) (3,0)
    1 (0,1) (1,1) (2,1) (3,1)
    2 (0,2) (1,2) (2,2) (3,2)
    3 (0,3) (1,3) (2,3) (3,3)
    .
    .
    .
    
        0   1   2   3
    0   0   1   2   3
    1   4   5   6   7
    2   8   9   10  11
    3   12  13  14  15
    
    '''
    
    #structure of field elements:
    #field = [ value ]
    
    def __init__(self, size = (0,0), minesNumber = 0):
        #the purpose of method startGame() to define object BEFORE start of the game
        #thats because I don't want to delete the game object but start again just using startGame()
        #also I don't wanna check existing of that object every time i ???
        
        self.startGame(size, minesNumber)
        
    def cleanParameters(self):
        self.field = []  #the whole field
        self.mines = []  #list of all mines
        self.flags = []  #            flags
        self.zeros = []  #            zeros
        
        self.openL = []  #            opened cells
        self.restL = []  #            unopened cells 
        
        self.fieldSize = (0,0)
                
        self.updateParameters()
    
    def updateParameters(self):
        
        self.height = self.fieldSize[0]
        self.width = self.fieldSize[1]
        
        self.flagsLeft = len(self.mines)
        self.cellsLeft = len(self.restL)
        
        self.total = self.height * self.width
        
      
    
    def startGame(self, size, minesNumber):
        
        self.cleanParameters()
        
        self.fieldSize = size
        self.updateParameters()
                
        self.flagsLeft = minesNumber
        
        self.generateField()
        self.generateMines()
        self.generateHints()
        self.updateParameters()

        
    def generateField(self):
        
        for i in range(self.total):
            self.field.append(0)
            self.restL.append(i)


    def generateMines(self):
        
        for i in range(self.flagsLeft):
            
            while True:
                rand = random.randint(1, self.total-1)
                if rand not in self.mines:
                    break
                
            self.mines.append(rand)
        
        self.mines.sort()
        
    def generateHints(self):
        
        for i in self.mines:
            
            self.field[i] = -1
            
        for i in self.mines:
            for j in self.neighbors(i):
                if j not in self.mines:
                    self.field[j] += 1
        
        for i in range(self.total):
            if self.field[i] == 0:
                self.zeros.append(i)
                    
    def flagCell(self, N):
        
        if N not in self.flags:
            self.flags.append(N)
            #self.restL.remove(N)
            self.cellsLeft -= 1
            self.flagsLeft -= 1
            return 1
            
        else:
            self.flags.remove(N)
            #self.restL.append(N)
            self.cellsLeft += 1
            self.flagsLeft += 1
            return 0
        
    def openCell(self, N):
        
        if N in self.restL:
                
            self.cellsLeft -= 1
            self.openL.append(N)
            self.restL.remove(N)
            
        return self.field[N]
    
    
    def openMeadow(self, N):
        
        return self.findZeros([N])


    def findZeros(self, zlist):
        #zlist - already discovered zeros
        #neighbors of last element is zlist
        nlist = self.neighbors(zlist[-1])
        for i in nlist:
            
            if i in self.openL or i in self.flags or i in zlist:
                continue
            
            else:
                zlist.append(i)
                
                if i in self.zeros:
                    self.findZeros(zlist)
                    
        return zlist
    
        
    def neighbors(self, N):
        (y, x) = self.rCoord(N)
        anl =   [(y-1, x-1), (y-1, x  ), (y-1, x+1),
                 (y  , x-1)            , (y  , x+1), 
                 (y+1, x-1), (y+1, x  ), (y+1, x+1)]
        
        
        #corners
            #tl
        if               x == 0     and                 y == 0:
            nlist = [  anl[4], *anl[6:8] ]

            #tr
        elif x == self.width - 1 and                 y == 0:
            nlist = [  anl[3], *anl[5:7] ]
            
            #bl
        elif             x == 0     and y == self.height - 1:
            nlist = [ *anl[1:3],  anl[4] ]
            
            #br
        elif x == self.width - 1 and y == self.height - 1:
            nlist = [ *anl[0:2],  anl[3] ]
         
            
        #sides 
            #t
        elif                y == 0:
            nlist = [ *anl[3:8] ]
            
            #l
        elif                x == 0:
            nlist = [ *anl[1:3], anl[4], *anl[6: 8] ]
            
            #r
        elif x == self.width - 1:
            nlist = [ *anl[0:2], anl[3], *anl[5:7] ]
            
            #b
        elif y == self.height - 1:
            nlist = [ *anl[0:5] ]
        
        
        #inside
        else:
            nlist = anl
           
        #I wanna return numbers, not coordinates
        
        nnlist = []
        
        for i in nlist:
            nnlist.append(self.width * i[0] + i[1])
            
        return  nnlist
    
    
            
    def rCoord(self, N):
        
        if N >= self.total:
            print('Error rCoord: N is too big')
            return 
        
        return ( int( N / self.fieldSize[1] ), N % self.fieldSize[1])
    
    def rHint(self, N):
        return self.field[N]