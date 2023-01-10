# 2D Array Manipulation
# Cade Sayner
# 24 April 2022

# Create a 4x4 grid of zeroes
def create_grid(grid):
    for row in range(4):
        grid.append([])
        for col in range(4):
            grid[row].append(0)

# Prints a 4x4 grid in a grid of size 5
def print_grid(grid):
    print("+--------------------+")
    for row in range(4):
        print("|", end="")
        row_string = ""
        for col in range(4):
            if (grid[row][col] == 0):
                row_string += "     "
            else:
                row_string += "{0:<5}".format(grid[row][col])
        print(row_string, end="")   
        print("|")
    print("+--------------------+")

# Checking if any are zeroes or there are any adjacent values
def check_lost(grid):
    # cHorizontally adjacent 
    for row in range(4):
        for col in range(1, 3):
            if (grid[row][col] == grid[row][col-1]) or (grid[row][col] == grid[row][col+1]):
                return False

    # Verticla adjacent check
    for col in range(4):
        for row in range(1, 3):
            if (grid[row][col] == grid[row-1][col]) or (grid[row][col] == grid[row+1][col]):
                return False

    # Checking for any zeroes
    for row in range(4):
        for col in range(4):
            if (grid[row][col] == 0):
                return False

    # No options returned therefore the game is lost
    return True

# Check if any value>=32 
def check_won(grid):
    for row in range(4):
        for col in range(4):
            if (grid[row][col] >= 32):
                return True
    
    # no value >= 32 was found, therefore the game has not yet been won
    return False


def copy_grid(grid):
    arr = []
    for row in range(4):
        arr.append([])
        for col in range(4):
            arr[row].append(grid[row][col])

    return arr

# checking if 2 grids are equal
def grid_equal(grid1, grid2):
    # checking for unreal grid values
    for row in range(4):
        for col in range(4):
            if (grid1[row][col] != grid2[row][col]):
                return False

    # grid values are equal
    return True