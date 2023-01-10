# SYNCAD001
# Cade Sayner 
# 24/04/2022

import util

# Shifts all blocks to the far left and erases zeroes
def shiftLeft(grid):
    new = create_grid()
    for i in range(4):
        fill_pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new[i][fill_pos] = grid[i][j]
                fill_pos += 1
    for row in range(4):
        for col in range(4):
            grid[row][col] = new[row][col]

# Combines all adjacent equal numbers and shifts them to the far left 
def CombineLeft(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0

# Reverses the matrix
def reverse(grid):
    new_ = []
    for i in range(4):
        new_.append([])
        for j in range(4):
            new_[i].append(grid[i][3-j])
    for row in range(4):
        for col in range(4):
            grid[row][col] = new_[row][col]
    

# Transposes the matrix 
def transpose(grid):
    new_matrix = create_grid()
    for i in range(4):
        for j in range(4):
            new_matrix[i][j] = grid[j][i]
    for row in range(4):
        for col in range(4):
            grid[row][col] = new_matrix[row][col]

# Create an empty grid 
def create_grid():
    arr = [[], [], [], []]
    for row in range(4):
        for col in range(4):
            arr[row].append(0)
    return arr

def push_left(grid):
    shiftLeft(grid)
    CombineLeft(grid)
    shiftLeft(grid)


def push_right(grid):
    reverse(grid)
    shiftLeft(grid)
    CombineLeft(grid) 
    shiftLeft(grid)
    reverse(grid)

def push_up(grid_):
    transpose(grid_)
    shiftLeft(grid_)
    CombineLeft(grid_) 
    shiftLeft(grid_)
    transpose(grid_)
    

def push_down(grid):
    transpose(grid)
    reverse(grid)
    shiftLeft(grid)
    CombineLeft(grid) 
    shiftLeft(grid)
    reverse(grid)
    transpose(grid)




