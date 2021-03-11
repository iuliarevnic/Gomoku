'''
Created on 23 dec. 2018

@author: Revnic
'''
def checkRows(matrix):
    '''
    Function that checks whether there are 5 consecutive elements of 1 or 2 on any row of a given matrix
    input: matrix
    preconditions:-
    output: 0 or 1 or 2
    postconditions: If there are such 5 elements of 1, the function returns 1,if there are such 5 elements of 2 else it returns 0
    '''
    for line in range(0,15):
        column=0
        while column<=10:
            if(matrix[line][column]==1 and matrix[line][column+1]==1 and matrix[line][column+2]==1 and matrix[line][column+3]==1 and matrix[line][column+4]==1):
                return 1
            elif matrix[line][column]==2 and matrix[line][column+1]==2 and matrix[line][column+2]==2 and matrix[line][column+3]==2 and matrix[line][column+4]==2:
                return 2
            column+=1
    return 0        
def checkColumns(matrix):
    '''
    Function that checks whether there are 5 consecutive elements of 1 or 2 on any column of a given matrix
    input: matrix
    preconditions:-
    output: 0 or 1 or 2
    postconditions: If there are such 5 elements of 1, the function returns 1,if there are such 5 elements of 2 else it returns 0
    '''
    for column in range(0,15):
        line=0
        while line<=10:
            if(matrix[line][column]==1 and matrix[line+1][column]==1 and matrix[line+2][column]==1 and matrix[line+3][column]==1 and matrix[line+4][column]==1):
                return 1
            elif matrix[line][column]==2 and matrix[line+1][column]==2 and matrix[line+2][column]==2 and matrix[line+3][column]==2 and matrix[line+4][column]==2:
                return 2
            line+=1
    return 0
def checkDiagonals(matrix):
    '''
    Function that checks whether there are 5 consecutive elements of 1 or 2 diagonally in a given matrix
    input: matrix
    preconditions:-
    output: 0 or 1 or 2
    postconditions: If there are such 5 elements, the function will return the value of the elements, else it will return 0
    '''
    for line in range(0,11):
        for column in range(0,11):
            if matrix[line][column]==1 and matrix[line+1][column+1]==1 and matrix[line+2][column+2]==1 and matrix[line+3][column+3]==1 and matrix[line+4][column+4]==1:
                return 1
            elif matrix[line][column]==2 and matrix[line+1][column+1]==2 and matrix[line+2][column+2]==2 and matrix[line+3][column+3]==2 and matrix[line+4][column+4]==2:
                return 2
    for line in range(0,11):
        for column in range(14,3,-1):
            if matrix[line][column]==1 and matrix[line+1][column-1]==1 and matrix[line+2][column-2]==1 and matrix[line+3][column-3]==1 and matrix[line+4][column-4]==1:
                return 1
            elif matrix[line][column]==2 and matrix[line+1][column-1]==2 and matrix[line+2][column-2]==2 and matrix[line+3][column-3]==2 and matrix[line+4][column-4]==2:
                return 2  
    return 0             
def MaximumRows(matrix,position):
    '''
    Function that finds the maximum number of consecutive elements of 2 in a row, having at least an element of 0 at one end of the sequence
    input: matrix, position 
    preconditions:-
    output: maximum 
    postconditions:-
    '''
    maximum=0
    for line in range(0,15):
        column=0
        while column<=14:
            ok=0
            length=0
            while matrix[line][column]==2 and column<14:
                length+=1
                column+=1
            if column==14 and matrix[line][13]==2 and matrix[line][14]==2:
                length+=1         
            if length!=0:
                if (column-1-length>=0 and matrix[line][column-1-length]==0):
                    ok=1
                    columnIndex=column-1-length
                elif (column<=14 and matrix[line][column]==0): 
                    ok=1
                    columnIndex=column       
            if length>maximum and ok==1:
                maximum=length
                position[0]=line
                position[1]=columnIndex        
                
            column+=1    
    return maximum
        
def MaximumColumns(matrix,position):
    '''
    Function that finds the maximum number of consecutive elements of 2 in a column, having at least an element of 0 at one end of the sequence
    input: matrix, position 
    preconditions:-
    output: maximum 
    postconditions:-
    '''
    maximum=0
    for column in range(0,15):
        line=0
        while line<=14:
            ok=0
            length=0
            while matrix[line][column]==2 and line<14:
                length+=1
                line+=1
            if line==14 and matrix[line][13]==2 and matrix[line][14]==2:
                length+=1 
            if length!=0:
                if (line-1-length>=0 and matrix[line-1-length][column]==0):
                    ok=1
                    lineIndex=line-1-length
                elif (line<=14 and matrix[line][column]==0):
                    ok=1
                    lineIndex=line
                     
            if length>maximum and ok==1:
                maximum=length
                position[0]=lineIndex
                position[1]=column         
                
            line+=1
    return maximum        
def MaximumDiagonals(matrix,position):
    '''
    Function that finds the maximum number of consecutive elements of 2 diagonally, having at least an element of 0 at one end of the sequence
    input: matrix, position 
    preconditions:-
    output: maximum 
    postconditions:-
    '''
    maximum=0
    for line in range(0,11):
        column=0
        while column<=10:
            length=0
            ok=0
            auxiliaryLine=line
            while matrix[auxiliaryLine][column]==2 and auxiliaryLine<14 and column<14:
                length+=1
                auxiliaryLine+=1
                column+=1
            if auxiliaryLine==14 and matrix[auxiliaryLine][column]==2 and matrix[auxiliaryLine-1][column-1]==2:
                length+=1
            elif column==14 and matrix[auxiliaryLine][column]==2 and matrix[auxiliaryLine-1][column-1]==2:
                length+=1
            if length!=0:
                if (auxiliaryLine-1-length>=0 and column-1-length>=0 and matrix[auxiliaryLine-1-length][column-1-length]==0): 
                    ok=1
                    lineIndex=auxiliaryLine-1-length
                    columnIndex=column-1-length
                elif (auxiliaryLine<=14 and column<=14 and matrix[auxiliaryLine][column]==0):
                    ok=1
                    lineIndex=auxiliaryLine
                    columnIndex=column    
                    
            if length>maximum and ok==1:
                maximum=length
                position[0]=lineIndex
                position[1]=columnIndex
            column+=1                           
    
    
    for line in range(0,11):
        column=14
        while column>=4:
            length=0
            ok=0
            auxiliaryLine=line
            while matrix[auxiliaryLine][column]==2 and auxiliaryLine<14 and column>0:
                length+=1
                auxiliaryLine=auxiliaryLine+1
                column=column-1
            if auxiliaryLine==14 and matrix[auxiliaryLine][column]==2 and matrix[auxiliaryLine+1][column+1]==2:
                length+=1
            elif column==0 and matrix[auxiliaryLine][column]==2 and matrix[auxiliaryLine-1][column+1]==2:
                length+=1          
            if length!=0:
                if (auxiliaryLine-1-length>=0 and column+1+length<=14 and matrix[auxiliaryLine-1-length][column+1+length]==0): 
                    ok=1
                    lineIndex=auxiliaryLine-1-length
                    columnIndex=column+1+length
                elif (auxiliaryLine<=14 and column>=0 and matrix[auxiliaryLine][column]==0):
                    ok=1
                    lineIndex=auxiliaryLine
                    columnIndex=column    
                    
            if length>maximum and ok==1:
                maximum=length
                position[0]=lineIndex
                position[1]=columnIndex
            column=column-1 
    
    return maximum         

def computerWin(matrix,winPosition):
    '''
    Function that checks if the computer has a chance to win with the next move, and if so, it also gives the position of the computer element 
    input: matrix,winPosition
    preconditions:-
    output:0 or 1
    postconditions:-
    '''
    for line in range(0,15):
        column=0
        while column<=11:
            if matrix[line][column]==2 and matrix[line][column+1]==2 and matrix[line][column+2]==2 and matrix[line][column+3]==2:
                if column-1>=0 and matrix[line][column-1]==0:
                    winPosition[0]=line
                    winPosition[1]=column-1
                    return 1
                else:
                    if column+4<=14 and matrix[line][column+4]==0:
                        winPosition[0]=line
                        winPosition[1]=column+4
                        return 1   
                
            column+=1
        

    for column in range(0,15):
        line=0
        while line<=11:
            if matrix[line][column]==2 and matrix[line+1][column]==2 and matrix[line+2][column]==2 and matrix[line+3][column]==2 :
                if line-1>=0 and matrix[line-1][column]==0:
                    winPosition[0]=line-1
                    winPosition[1]=column
                    return 1
                else:
                    if line+4<=14 and matrix[line+4][column]==0:
                        winPosition[0]=line+4
                        winPosition[1]=column
                        return 1
            line+=1
     

    for line in range(0,12):
        for column in range(0,12):
            if matrix[line][column]==2 and matrix[line+1][column+1]==2 and matrix[line+2][column+2]==2 and matrix[line+3][column+3]==2:
                if line-1>=0 and column-1>=0 and matrix[line-1][column-1]==0:
                    winPosition[0]=line-1
                    winPosition[1]=column-1
                    return 1
                else:
                    if line+4<=14 and column+4<=14 and matrix[line+4][column+4]==0:
                        winPosition[0]=line+4
                        winPosition[1]=column+4
                        return 1
            
    for line in range(0,12):
        for column in range(14,2,-1):
            if matrix[line][column]==2 and matrix[line+1][column-1]==2 and matrix[line+2][column-2]==2 and matrix[line+3][column-3]==2:
                if line-1>=0 and column+1<=14 and matrix[line-1][column+1]==0:
                    winPosition[0]=line-1
                    winPosition[1]=column+1
                    return 1
                else:
                    if line+4<=14 and column-4>=0 and matrix[line+4][column-4]==0:
                        winPosition[0]=line+4
                        winPosition[1]=column-4
                        return 1  
    return 0     
    
    
    
def oneMoveVictory(matrix,blockPosition):
    '''
    Function that checks whether the human player is at one-move victory or not, and if it is, it finds the position for the computer player to put his piece on, blocking the human player
    input: matrix, blockPosition
    preconditions:-
    output:0 or 1
    postconditions:-
    '''
    #cautarea pe randuri
    for line in range(0,15):
        column=0
        while column<=11:
            if matrix[line][column]==1 and matrix[line][column+1]==1 and matrix[line][column+2]==1 and matrix[line][column+3]==1:
                if column-1>=0 and matrix[line][column-1]==0:
                    blockPosition[0]=line
                    blockPosition[1]=column-1
                    return 1
                else:
                    if column+4<=14 and matrix[line][column+4]==0:
                        blockPosition[0]=line
                        blockPosition[1]=column+4
                        return 1   
            
            column+=1
    
        
    for line in range(0,15):
        column=0
        while column<=12:
            if matrix[line][column]==1 and matrix[line][column+1]==1 and matrix[line][column+2]==1 and column-1>=0 and matrix[line][column-1]==0 and column+3<=14 and matrix[line][column+3]==0:
                blockPosition[0]=line
                blockPosition[1]=column-1
                return 1    
            column+=1
            
    for line in range(0,15):
        column=0
        while column<=12:
            if matrix[line][column]==1 and matrix[line][column+1]==1 and matrix[line][column+2]==1:
                if column-1>=0 and matrix[line][column-1]==0:
                    blockPosition[0]=line
                    blockPosition[1]=column-1
                    return 1
                else:
                    if column+3<=14 and matrix[line][column+3]==0:
                        blockPosition[0]=line
                        blockPosition[1]=column+3
                        return 1   
            
            column+=1        
    #cautarea pe coloane        
    for column in range(0,15):
        line=0
        while line<=11:
            if matrix[line][column]==1 and matrix[line+1][column]==1 and matrix[line+2][column]==1 and matrix[line+3][column]==1 :
                if line-1>=0 and matrix[line-1][column]==0:
                    blockPosition[0]=line-1
                    blockPosition[1]=column
                    return 1
                else:
                    if line+4<=14 and matrix[line+4][column]==0:
                        blockPosition[0]=line+4
                        blockPosition[1]=column
                        return 1
            line+=1 
            
    for column in range(0,15):
        line=0
        while line<=12:
            if matrix[line][column]==1 and matrix[line+1][column]==1 and matrix[line+2][column]==1 and line-1>=0 and matrix[line-1][column]==0 and line+3<=14 and matrix[line+3][column]==0:
                blockPosition[0]=line-1
                blockPosition[1]=column
                return 1
            line+=1
            
    for column in range(0,15):
        line=0
        while line<=12:
            if matrix[line][column]==1 and matrix[line+1][column]==1 and matrix[line+2][column]==1:
                if line-1>=0 and matrix[line-1][column]==0:
                    blockPosition[0]=line-1
                    blockPosition[1]=column
                    return 1
                else:
                    if line+3<=14 and matrix[line+3][column]==0:
                        blockPosition[0]=line+3
                        blockPosition[1]=column
                        return 1
            line+=1         
            
    #cautarea pe diagonale
                                        
    for line in range(0,12):
        for column in range(0,12):
            if matrix[line][column]==1 and matrix[line+1][column+1]==1 and matrix[line+2][column+2]==1 and matrix[line+3][column+3]==1:
                if line-1>=0 and column-1>=0 and matrix[line-1][column-1]==0:
                    blockPosition[0]=line-1
                    blockPosition[1]=column-1
                    return 1
                else:
                    if line+4<=14 and column+4<=14 and matrix[line+4][column+4]==0:
                        blockPosition[0]=line+4
                        blockPosition[1]=column+4
                        return 1   
                    
    for line in range(0,13):
        for column in range(0,13):
            if matrix[line][column]==1 and matrix[line+1][column+1]==1 and matrix[line+2][column+2]==1 and line-1>=0 and column-1>=0 and matrix[line-1][column-1]==0 and line+3<=14 and column+3<=14 and matrix[line+3][column+3]==0:
                blockPosition[0]=line-1
                blockPosition[1]=column-1
                return 1     
            
    for line in range(0,13):
        for column in range(0,13):
            if matrix[line][column]==1 and matrix[line+1][column+1]==1 and matrix[line+2][column+2]==1:
                if line-1>=0 and column-1>=0 and matrix[line-1][column-1]==0:
                    blockPosition[0]=line-1
                    blockPosition[1]=column-1
                    return 1
                else:
                    if line+3<=14 and column+3<=14 and matrix[line+3][column+3]==0:
                        blockPosition[0]=line+3
                        blockPosition[1]=column+3
                        return 1                       
            
    for line in range(0,12):
        for column in range(14,2,-1):
            if matrix[line][column]==1 and matrix[line+1][column-1]==1 and matrix[line+2][column-2]==1 and matrix[line+3][column-3]==1:
                if line-1>=0 and column+1<=14 and matrix[line-1][column+1]==0:
                    blockPosition[0]=line-1
                    blockPosition[1]=column+1
                    return 1
                else:
                    if line+4<=14 and column-4>=0 and matrix[line+4][column-4]==0:
                        blockPosition[0]=line+4
                        blockPosition[1]=column-4
                        return 1 
                    
    for line in range(0,13):
        for column in range(14,1,-1):
            if matrix[line][column]==1 and matrix[line+1][column-1]==1 and matrix[line+2][column-2]==1 and line-1>=0 and column+1<=14 and matrix[line-1][column+1]==0 and line+3<=14 and column-3>=0 and matrix[line+3][column-3]==0:
                blockPosition[0]=line-1
                blockPosition[1]=column+1
                return 1
            
    for line in range(0,13):
        for column in range(14,1,-1):
            if matrix[line][column]==1 and matrix[line+1][column-1]==1 and matrix[line+2][column-2]==1:
                if line-1>=0 and column+1<=14 and matrix[line-1][column+1]==0:
                    blockPosition[0]=line-1
                    blockPosition[1]=column+1
                    return 1
                else:
                    if line+3<=14 and column-3>=0 and matrix[line+3][column-3]==0:
                        blockPosition[0]=line+3
                        blockPosition[1]=column-3
                        return 1         
            
    return 0

def firstComputerElement(matrix,playerElementPosition):
    '''
    Function that checks whether its the computer's first turn or not
    input: matrix,playerElementPosition
    preconditions:-
    output: 0 or 1
    postconditions:-
    '''
    for line in range(0,15):
        for column in range(0,15):
            if(matrix[line][column]==2):
                return 0
    for line in range(0,15):
        for column in range(0,15):
            if (matrix[line][column]==1):
                playerElementPosition[0]=line
                playerElementPosition[1]=column
                return 1                

def isFull(matrix):
    '''
    Function that checks whether the matrix is full or not
    input: matrix
    preconditions:-
    output: 0 or 1
    postconditions:-
    '''
    for line in range(0,15):
        for column in range(0,15):
            if matrix[line][column]==0:
                return 0
    return 1                    