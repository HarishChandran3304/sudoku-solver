#HELPER FUNCTIONS

def getgrid(filename: str) -> list[list[int]]:
    '''
    Retrieves the unsolved sudoku grid from a text file converts it into a matrix and returns it
    '''
    with open(filename) as f:
        return [list(map(int, row.split())) for row in f.readlines()]

def printgrid(grid: list[list[int]]) -> None:
    '''
    Pretty prints the grid to the terminal in a readable manner
    '''
    for i in range(9):
        if i%3 == 0:
            print("- "*13)
        
        for j in range(9):
            if j%3 == 0:
                print("| ", end="")
            print(grid[i][j], end=" ")
        
        print("|")
    print("- "*13)

def findempty(grid: list[list[int]]) -> tuple[int, int]:
    '''
    Finds the next empty square on the grid and returns its position as a tuple
    '''
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def checkrow(grid: list[list[int]], n: int, r: int) -> bool:
    '''
    Returns True if the number does not exist in a given row
    '''
    if n in grid[r]:
        return False
    return True

def checkcol(grid: list[list[int]], n: int, c: int) -> bool:
    '''
    Returns True if the number does not exist in a given col
    '''
    if n in [grid[i][c] for i in range(9)]:
        return False
    return True

def check3x3(grid: list[list[int]], n: int, r:int, c: int) -> bool:
    '''
    Returns True if the number does not exist in its corresponding 3x3 square
    '''
    x, y = c//3, r//3
    for i in range(y*3, y*3 +3):
        for j in range(x*3, x*3 +3):
            if grid[i][j] == n and (i, j) != (r, c):
                return False
    return True

def isvalid(grid: list[list[int]], n: int, pos: tuple[int, int]) -> bool:
    '''
    Returns True if the inserted number n is a valid move
    '''
    r, c = pos
    if checkrow(grid, n, r) and checkcol(grid, n, c) and check3x3(grid, n, r, c):
        return True
    return False

def solve(grid: list[list[int]]) -> bool:
    '''
    Solves the entire sudoku grid using the backactracking algorithm recursively
    '''
    find = findempty(grid)

    if not find:
        return True
    else:
        row, col = find
    
    for n in range(1, 10):
        if isvalid(grid, n, (row, col)):
            grid[row][col] = n

            if solve(grid):
                return True
            
            grid[row][col] = 0
    
    return False