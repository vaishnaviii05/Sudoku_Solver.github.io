# creating a soduku game in python 

import numpy as np

grid = [[0,0,0,0,0,0,9,8,4],
        [4,0,0,8,0,0,2,5,0],
        [0,8,0,0,4,9,0,0,3],
        [9,0,6,1,5,7,8,0,2],
        [0,0,0,0,0,0,0,4,0],
        [0,0,0,0,8,0,1,9,6],
        [0,3,4,9,2,8,5,6,0],
        [6,0,2,0,1,5,3,7,0],
        [0,0,5,0,6,0,0,0,0]]


def possible(row, column, number):
    global grid
    
    #check if the number already exists in a row 
    
    for x in range(0,9):
        if grid [row][x]== number:
            return False
        
    #check if the number already exists in a column
    
    for x in range (0,9):
        if grid[x][column]== number:
            return False
        
    #check if the number is already exixts in a box
    
    x0 = (column // 3) *3
    y0 = (row // 3) * 3
    
    for i in range (0,3):
        for j in range (0,3):
            if grid [y0+1][x0+j]== number:
                return False
            
    return True
 
    
def solve() :
    global grid
    for row in range (0,9) :
        for column in range (0,9) :
            if grid [row][column]==0:
                for number in range (1,10):
                    if possible (row,column,number):
                        grid[row][column]= number
                        solve()
                        grid[row][column]=0
                return
    print (np.matrix(grid))
    input ('More possible solutions')
solve()
    



