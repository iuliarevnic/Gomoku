'''
Created on 23 dec. 2018

@author: Revnic
'''
class Validator():
    def validateElementPosition(self,line,column,matrix):
        '''
        Function that checks whether an element can be added at the given position in a matrix
        input: self, line, column, matrix
        preconditions:-
        output: errors
        postconditions: If the position is incorrect, errors will contain a proper message
        '''
        errors=""
        try: 
            line=int(line)
            if (line<0 or line>14):
                errors+="Line number should be between 0 and 14.\n"    
            try:
                column=int(column)
                if(column <0 or column > 14):
                    errors+="Column number should be between 0 and 14.\n"
                    if matrix[line][column]!=0:
                        errors+="Element already exists at the given position."    
            except ValueError:
                errors+="Column number should be an integer.\n"    
        except ValueError:
            errors+="Line number should be an integer.\n"
        
        return errors                    