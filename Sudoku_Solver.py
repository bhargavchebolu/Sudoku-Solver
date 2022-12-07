M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end="")
        print()
def solve(grid, row, col, num):
    for k in range(9):
        if grid[row][k] == num:
            return False
    for k in range(9):
        if grid[k][col] == num:
            return False

    Row = row - row % 3
    Col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + Row][j + Col] == num:
                return False
    return True

def Sudoku(grid, row, col):

    if (row == M - 1 and col == M):
        return True
    if col == M:
        row +=1
        col = 0
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

grid = [[0, 0, 0, 0, 8, 0, 0, 0, 3],
        [0, 7, 3, 0, 0, 0, 1, 0, 5],
        [4, 6, 0, 1, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 7, 6],
        [0, 3, 2, 8, 6, 1, 0, 4, 9],
        [6, 9, 5, 7, 0, 3, 0, 2, 1],
        [0, 0, 4, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 3, 0, 4, 0, 0, 2],
        [3, 5, 0, 0, 2, 8, 0, 0, 0]]

if (Sudoku(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist")



