import numpy as np

# Define the Sudoku grid
matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Convert the matrix to a NumPy array
grid = np.array(matrix)


# Print the Sudoku grid
def print_sudoku(grid):
    for row in grid:
        print(row)


print("Initial Sudoku Grid:")
print_sudoku(grid)

# Each cell contains a number from 1 to 9.
# Each number appears exactly once in each row.
# Each number appears exactly once in each column.
# Each number appears exactly once in each 3x3 sub-grid.


# 1. Ensure each number appears exactly once in each row, ignoring zeros.
def row_constraint(grid, row):
    row_values = grid[row, :]

    # Check if the unique non-zero values in the row are equal to the count of non-zero values
    # This ensures that each number from 1 to 9 appears exactly once, ignoring zeros.
    # If there are no duplicates, the length of the set of non-zero values should equal the count of non-zero values.
    # If there are duplicates, the length of the set will be less than the count of non-zero values.
    return len(set(row_values) - {0}) == len(row_values) - list(row_values).count(0)


# 2. Ensure each number appears exactly once in each column, ignoring zeros.
def column_constraint(grid, col):
    col_values = grid[:, col]
    return len(set(col_values) - {0}) == len(col_values) - list(col_values).count(0)


# 3. Ensure each number appears exactly once in each 3x3 sub-grid, ignoring zeros.
def subgrid_constraint(grid, row, col):
    subgrid = grid[row//3*3:row//3*3+3, col//3*3:col//3*3+3]
    subgrid_values = subgrid.flatten()
    return len(set(subgrid_values) - {0}) == len(subgrid_values) - list(subgrid_values).count(0)


# Combine all constraints
def is_valid_sudoku(grid):
    for i in range(9):
        if not row_constraint(grid, i):
            return 'Sudoku structure is not valid'
        if not column_constraint(grid, i):
            return 'Sudoku structure is not valid'
        for j in range(0, 9, 3):
            if not subgrid_constraint(grid, i, j):
                return 'Sudoku structure is not valid'
    return '\nSudoku structure is valid'


# Check the validity of the Sudoku grid
print(is_valid_sudoku(grid))


# Check if a move is valid
def is_valid_move(grid, row, col, num):
    grid[row, col] = num
    valid = (row_constraint(grid, row) and
             column_constraint(grid, col) and
             subgrid_constraint(grid, row, col))
    grid[row, col] = 0  # Reset cell after checking
    return valid


# Find an empty location in the grid
def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                return (row, col)
    return None


# Solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True  # Puzzle solved

    row, col = empty_loc
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row, col] = num
            if solve_sudoku(grid):
                return True
            grid[row, col] = 0  # Reset cell and backtrack

    return False


if solve_sudoku(grid):
    print("\nSolved Sudoku:")
    print_sudoku(grid)
else:
    print("No solution exists")


# Too long run-time in my system to find the solution.
# impossible_configuration = unsolvable_matrix = [
#     [2, 0, 0, 9, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 6, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [5, 0, 2, 6, 0, 0, 4, 0, 7],
#     [0, 0, 0, 8, 0, 4, 1, 0, 0],
#     [0, 0, 0, 0, 9, 8, 0, 2, 3],
#     [0, 0, 0, 0, 0, 3, 0, 8, 0],
#     [0, 0, 5, 0, 1, 0, 0, 0, 0],
#     [0, 0, 7, 0, 0, 0, 0, 0, 0]
# ]

# grid = np.array(impossible_configuration)


# Print the Sudoku grid
# def print_sudoku(grid):
#     for row in grid:
#         print(row)


# print("\nImpossible Sudoku Grid:")
# print_sudoku(grid)

# if solve_sudoku(grid):
#     print("\nSolved Sudoku:")
#     print_sudoku(grid)
# else:
#     print("\nNo solution exists")
