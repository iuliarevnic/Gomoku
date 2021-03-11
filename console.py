'''
Created on 23 dec. 2018

@author: Revnic
'''
class Console():
    def __init__(self,controller):
        self.__controller=controller
    def __uiAddElement(self):
        lineNumber=input("Give line number")
        columnNumber=input("Give column number")
        try:
            self.__controller.addElement(lineNumber,columnNumber)
            if self.__controller.EndGame()==0 and self.__controller.Draw()==0:
                self.__uiComputerMove()  
            else:
                return    
        except ValueError as valueError:
            print(valueError)
                    
    def __uiComputerMove(self):
        self.__controller.computerMove()   
                     
    def __uiPrintMatrix(self,Matrix):
        print("    ",0,"",1,"",2,"",3,"",4,"",5,"",6,"",7,"",8,"",9,10,11,12,13,14)
        print("    ____________________________________________")
        for lineIndex in range(0,15):
            if lineIndex<10:
                print(lineIndex," |",Matrix[lineIndex][0],
                      "",
                      Matrix[lineIndex][1],
                      "",
                      Matrix[lineIndex][2],
                      "",
                      Matrix[lineIndex][3],
                      "",
                      Matrix[lineIndex][4],
                      "",
                      Matrix[lineIndex][5],
                      "",
                      Matrix[lineIndex][6],
                      "",
                      Matrix[lineIndex][7],
                      "",
                      Matrix[lineIndex][8],
                      "",
                      Matrix[lineIndex][9],
                      "",
                      Matrix[lineIndex][10],
                      "",
                      Matrix[lineIndex][11],
                      "",
                      Matrix[lineIndex][12],
                      "",
                      Matrix[lineIndex][13],
                      "",
                      Matrix[lineIndex][14])
            else:
                print(lineIndex,"|",Matrix[lineIndex][0],
                      "",
                      Matrix[lineIndex][1],
                      "",
                      Matrix[lineIndex][2],
                      "",
                      Matrix[lineIndex][3],
                      "",
                      Matrix[lineIndex][4],
                      "",
                      Matrix[lineIndex][5],
                      "",
                      Matrix[lineIndex][6],
                      "",
                      Matrix[lineIndex][7],
                      "",
                      Matrix[lineIndex][8],
                      "",
                      Matrix[lineIndex][9],
                      "",
                      Matrix[lineIndex][10],
                      "",
                      Matrix[lineIndex][11],
                      "",
                      Matrix[lineIndex][12],
                      "",
                      Matrix[lineIndex][13],
                      "",
                      Matrix[lineIndex][14])    
        print("\n")          
    def run(self):
        print("Welcome to Gomoku!\n")
        self.__uiPrintMatrix(self.__controller._Controller__matrix._Matrix__elements)
        while self.__controller.EndGame()==0 and self.__controller.Draw()==0:
            self.__uiAddElement()
            self.__uiPrintMatrix(self.__controller._Controller__matrix._Matrix__elements)
        if self.__controller.EndGame()==1:
            print("Player wins!")
        if self.__controller.EndGame()==2:
            print("Computer wins!")        
        elif self.__controller.Draw()==1:
            print("It's a draw.")    
            