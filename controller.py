'''
Created on 23 dec. 2018

@author: Revnic
'''
from validator import Validator
from helpers import *
class Controller():
    def __init__(self,matrix):
        self.__matrix=matrix
    def addElement(self,lineNumber,columnNumber):
        '''
        Function that adds an element to a matrix, if the lineNumber and the columnNumber are valid
        input: self, lineNumber, columnNumber
        preconditions: -
        output: -
        postconditions: If the element indexes are valid, the element will be added to the matrix
        '''
        validator=Validator()
        errors=validator.validateElementPosition(lineNumber,columnNumber,self.__matrix._Matrix__elements)
        if(len(errors)==0):
            lineNumber=int(lineNumber)
            columnNumber=int(columnNumber)
            self.__matrix._Matrix__elements[lineNumber][columnNumber]=1
        else:
            raise ValueError(errors)    
    def EndGame(self):
        '''
        Function that checks whether the game is over or not  
        input: self
        preconditions:-
        output: 0 or 1 or 2
        postconditions: If the game is over, the function will return 1, else it will return 0.
        '''
        row=checkRows(self.__matrix._Matrix__elements)
        column=checkColumns(self.__matrix._Matrix__elements)
        diagonal=checkDiagonals(self.__matrix._Matrix__elements)       
        if row!=0 or column!=0 or diagonal!=0:
            return max(row,column,diagonal)
        else:
            return 0
    def addComputerElement(self,lineNumber,columnNumber):
        '''
        Function that adds a 2 element in a matrix at the given position
        input: self, lineNumber, columnNumber
        preconditions:-
        output:-
        postconditions:-
        '''    
        self.__matrix._Matrix__elements[lineNumber][columnNumber]=2
        
    def makeCloseMove(self):
        '''
        Function that decides where the next close move of the computer should be
        input: self
        preconditions:-
        output:-
        postconditions:-
        '''
        elementPosition=[0,0]
        playerElementPosition=[0,0]
        if firstComputerElement(self.__matrix._Matrix__elements,playerElementPosition)==0:
            rowPosition=[0,0]
            columnPosition=[0,0]
            diagonalPosition=[0,0]
        
            row=MaximumRows(self.__matrix._Matrix__elements,rowPosition)
            column=MaximumColumns(self.__matrix._Matrix__elements,columnPosition)
            diagonal=MaximumDiagonals(self.__matrix._Matrix__elements,diagonalPosition)
            
        
            maximum=row
            elementPosition[0]=rowPosition[0]
            elementPosition[1]=rowPosition[1]
        
            if maximum<column:
                maximum=column
                elementPosition[0]=columnPosition[0]
                elementPosition[1]=columnPosition[1]
            if maximum<diagonal:
                elementPosition[0]=diagonalPosition[0]
                elementPosition[1]=diagonalPosition[1]    
                
        else:
            elementPosition[0]=playerElementPosition[0]
            if playerElementPosition[1]<7:
                elementPosition[1]=playerElementPosition[1]+1
            else:
                elementPosition[1]=playerElementPosition[1]-1
        self.addComputerElement(elementPosition[0], elementPosition[1])        
                    
                
                

    def computerMove(self):
        '''
        Function that finds one of the best moves for the computer
        input: self
        preconditions:-
        output:-
        postconditions:-
        '''    
        winPosition=[0,0] 
        blockPosition=[0,0]   
        if computerWin(self.__matrix._Matrix__elements,winPosition):
            self.addComputerElement(winPosition[0],winPosition[1])
        elif oneMoveVictory(self.__matrix._Matrix__elements,blockPosition):#ambele capete libere si 3 piese sau un capat liber(celalalt ori 2 ori nu exista) si 4 piese
            self.addComputerElement(blockPosition[0],blockPosition[1])
        else:
            self.makeCloseMove()    
        
    def Draw(self):
        '''
        Function that checks whether the board is filled or not
        input: self
        preconditions:-
        output: 0 or 1
        postconditions:-
        '''
        if isFull(self.__matrix._Matrix__elements)==1:
            return 1
        return 0    