'''
Created on 24 dec. 2018

@author: Revnic
'''
import unittest
from matrix import Matrix
from validator import Validator
from helpers import *
from controller import *
class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def testValidateElementPosition(self):
        '''
        Function that checks whether a position for a player element is correctly validated or not
        input:-
        preconditions:-
        output:-
        postconditions: If the position isn't correctly validated, an error will appear.
        '''
        matrix=Matrix()
        line=12
        column=3
        validator=Validator()
        errors=validator.validateElementPosition(line, column, matrix._Matrix__elements)
        self.assertEqual(errors,"")
        newLine=15
        errors=validator.validateElementPosition(newLine,column,matrix._Matrix__elements)
        self.assertEqual(errors,"Line number should be between 0 and 14.\n")
    def testCheckRows(self):
        '''
        Function that checks whether 5 consecutive elements of 1 or 2 on a row are properly found
        input:-
        preconditions:-
        output:-
        postconditions: If they aren't found correctly, an error will appear.
        '''
        matrix=Matrix()
        value=checkRows(matrix._Matrix__elements)
        self.assertEqual(value,0)
        matrix._Matrix__elements[2][5]=2
        matrix._Matrix__elements[2][6]=2
        matrix._Matrix__elements[2][7]=2
        matrix._Matrix__elements[2][8]=2
        matrix._Matrix__elements[2][9]=2
        value=checkRows(matrix._Matrix__elements)
        self.assertEqual(value,2)
    def testCheckColumns(self):
        '''
        Function that checks whether 5 consecutive elements of 1 or 2 on a column are properly found
        input:-
        preconditions:-
        output:-
        postconditions: If they aren't found correctly, an error will appear.
        '''
        matrix=Matrix()
        value=checkColumns(matrix._Matrix__elements)
        self.assertEqual(value,0)
        matrix._Matrix__elements[8][5]=1
        matrix._Matrix__elements[9][5]=1
        matrix._Matrix__elements[10][5]=1
        matrix._Matrix__elements[11][5]=1
        matrix._Matrix__elements[12][5]=1
        value=checkColumns(matrix._Matrix__elements)
        self.assertEqual(value,1)
    def testCheckDiagonals(self):
        '''
        Function that checks whether 5 consecutive elements of 1 or 2 diagonally are properly found
        input:-
        preconditions:-
        output:-
        postconditions: If they aren't found correctly, an error will appear.
        '''
        matrix=Matrix()
        value=checkDiagonals(matrix._Matrix__elements)
        self.assertEqual(value,0)
        matrix._Matrix__elements[8][5]=1
        matrix._Matrix__elements[9][6]=1
        matrix._Matrix__elements[10][7]=1
        matrix._Matrix__elements[11][8]=1
        matrix._Matrix__elements[12][9]=1
        value=checkDiagonals(matrix._Matrix__elements)
        self.assertEqual(value,1)
    def testMaximumRows(self):
        '''
        Function that checks whether the maximum number of consecutive elements of 2 on a row is correctly found 
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly found, an error will appear
        '''
        matrix=Matrix()
        matrix._Matrix__elements[8][5]=2
        matrix._Matrix__elements[8][6]=2
        matrix._Matrix__elements[8][7]=2
        matrix._Matrix__elements[11][8]=2
        matrix._Matrix__elements[11][9]=2
        position=[0,0]
        maximum=MaximumRows(matrix._Matrix__elements, position)
        self.assertEqual(maximum, 3)
        self.assertEqual(position,[8,4])
    def testMaximumColumns(self):
        '''
        Function that checks whether the maximum number of consecutive elements of 2 on a column is correctly found 
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly found, an error will appear
        '''
        matrix=Matrix()
        matrix._Matrix__elements[8][5]=2
        matrix._Matrix__elements[9][5]=2
        matrix._Matrix__elements[10][5]=2
        matrix._Matrix__elements[11][5]=2
        matrix._Matrix__elements[12][9]=2
        position=[0,0]
        maximum=MaximumColumns(matrix._Matrix__elements, position)
        self.assertEqual(maximum, 4)
        self.assertEqual(position,[7,5])
    def testMaximumDiagonals(self):
        '''
        Function that checks whether the maximum number of consecutive elements of 2 diagonally is correctly found 
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly found, an error will appear
        '''
        matrix=Matrix()
        matrix._Matrix__elements[8][5]=2
        matrix._Matrix__elements[9][6]=2
        matrix._Matrix__elements[10][7]=2
        matrix._Matrix__elements[11][8]=2
        position=[0,0]
        maximum=MaximumDiagonals(matrix._Matrix__elements, position)
        self.assertEqual(maximum, 4)
        self.assertEqual(position,[7,4])
        matrix=Matrix()
        matrix._Matrix__elements[8][5]=2
        matrix._Matrix__elements[9][4]=2
        matrix._Matrix__elements[10][3]=2
        matrix._Matrix__elements[11][2]=2
        maximum=MaximumDiagonals(matrix._Matrix__elements, position)
        self.assertEqual(maximum, 4)
        self.assertEqual(position,[7,6])
    def testComputerWin(self):
        '''
        Function that checks whether the opportunity of the computer to win with the next move is correctly found
        input:-
        preconditions:-
        output:-
        postconditions: If it not correctly found, an error will appear
        '''
        matrix=Matrix()
        winPosition=[0,0]
        matrix._Matrix__elements[8][5]=2
        matrix._Matrix__elements[9][4]=2
        matrix._Matrix__elements[10][3]=2
        matrix._Matrix__elements[11][2]=2
        value=computerWin(matrix._Matrix__elements,winPosition)
        self.assertEqual(value,1)
        self.assertEqual(winPosition,[7,6])
    def testOneMoveVictory(self):
        '''
        Function that checks whether the player's opportunity to win is correctly found 
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly found, an error will appear
        '''
        matrix=Matrix()
        blockPosition=[0,0]
        matrix._Matrix__elements[8][5]=1
        matrix._Matrix__elements[9][4]=1
        matrix._Matrix__elements[10][3]=1
        matrix._Matrix__elements[11][2]=1
        value=oneMoveVictory(matrix._Matrix__elements, blockPosition)
        self.assertEqual(value,1)
        self.assertEqual(blockPosition,[7,6]) 
    def testFirstComputerElement(self):
        '''
        Function that checks whether the computer's first turn is correctly found or not
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly found, an error will appear
        '''
        matrix=Matrix()
        matrix._Matrix__elements[12][3]=1
        playerElementPosition=[0,0]
        value=firstComputerElement(matrix._Matrix__elements,playerElementPosition)
        self.assertEqual(value,1)
        self.assertEqual(playerElementPosition,[12,3])
        matrix._Matrix__elements[12][4]=2
        value=firstComputerElement(matrix._Matrix__elements,playerElementPosition)
        self.assertEqual(value,0)
    def testIsFull(self):
        '''
        Function that checks whether a full matrix is correctly identified or not
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly identified, an error will appear
        '''
        matrix=Matrix()
        value=isFull(matrix._Matrix__elements)
        self.assertEqual(value,0)
        for line in range(0,15):
            for column in range(0,15):
                if(line+column==20):
                    matrix._Matrix__elements[line][column]=2
                else:
                    matrix._Matrix__elements[line][column]=1
        value=isFull(matrix._Matrix__elements)
        self.assertEqual(value,1)                
    def testAddElement(self):
        '''
        Function that checks whether a player element is correctly added to the board or not
        input:-
        preconditions:-
        output:-
        postconditions: If it not correctly added, an error will appear.
        '''
        matrix=Matrix()
        controller=Controller(matrix)
        controller.addElement(2,10)
        self.assertEqual(controller._Controller__matrix._Matrix__elements[2][10],1)
    def testEndGame(self):
        '''
        Function that checks whether the end of the game is correctly found or not
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly found, an error will appear.
        '''
        matrix=Matrix()
        controller=Controller(matrix)
        matrix._Matrix__elements[5][5]=2
        matrix._Matrix__elements[6][6]=2
        matrix._Matrix__elements[7][7]=2
        matrix._Matrix__elements[8][8]=2
        matrix._Matrix__elements[9][9]=2
        matrix._Matrix__elements[9][10]=1
        matrix._Matrix__elements[6][5]=1
        matrix._Matrix__elements[4][5]=1
        value=controller.EndGame()
        self.assertEqual(value,2)
    def testAddComputerElement(self):
        '''
        Function that checks whether a computer element is correctly added at the given position or not
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly added, an error will appear.
        '''
        matrix=Matrix()
        controller=Controller(matrix)
        controller.addComputerElement(2, 5)
        self.assertEqual(controller._Controller__matrix._Matrix__elements[2][5],2)
    def testMakeCloseMove(self):
        '''
        Function that checks whether the computer's close move is correctly made or not
        input:-
        preconditions:-
        output:-
        postconditions: If it not correctly made, an error will appear.
        '''
        matrix=Matrix()
        controller=Controller(matrix)
        matrix._Matrix__elements[5][5]=1
        controller.makeCloseMove()
        self.assertEqual(controller._Controller__matrix._Matrix__elements[5][6],2)
        matrix._Matrix__elements[6][6]=1
        controller.makeCloseMove()
        self.assertEqual(controller._Controller__matrix._Matrix__elements[5][7],2)
    def testComputerMove(self):
        '''
        Function that checks whether the best move for the computer is correctly found or not
        input:-
        preconditions:-
        output:-
        postconditions: If it not correctly found, an error will appear.
        '''
        matrix=Matrix()
        controller=Controller(matrix)
        matrix._Matrix__elements[4][4]=2
        matrix._Matrix__elements[5][5]=1
        matrix._Matrix__elements[6][6]=1
        matrix._Matrix__elements[7][7]=1
        controller.computerMove()
        self.assertEqual(controller._Controller__matrix._Matrix__elements[8][8],2)
    def testDraw(self):
        '''
        Function that checks whether the draw situation is correctly identified or not
        input:-
        preconditions:-
        output:-
        postconditions: If it is not correctly identified, an error will appear.
        '''
        matrix=Matrix()
        controller=Controller(matrix)
        value=controller.Draw()
        self.assertEqual(value,0)
        for line in range(0,15):
            for column in range(0,15):
                if(line+column==line-column+20):
                    matrix._Matrix__elements[line][column]=2
                else:
                    matrix._Matrix__elements[line][column]=1
        value=controller.Draw()
        self.assertEqual(value,1)     
if __name__=="__main__":
    unittest.main()        