def print_board(board):
    """Prints the Sudoku board with grid lines."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("= = = = = = = = = = = = = = = = = = = = = =")

        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" || ", end="")
            elif j != 0:
                print(" | ", end="")
            print(str(num) if num != 0 else '.', end=" ")
        print()

def find_empty_location(board):
    """Finds an empty location in the board."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_safe(board, row, col, num):
    """Checks if it's safe to place a number in a given cell."""
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True

    row, col = empty_location
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def validate_board(board):
    """Validates the initial Sudoku board."""
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                if not is_safe(board, row, col, num):
                    return False
                board[row][col] = num
    return True

def input_board():
    """Inputs the Sudoku board from the user."""
    board = []
    print("Enter the Sudoku puzzle, use 0 for empty cells:")
    for i in range(9):
        row = list(map(int, input(f"Enter row {i+1} (9 numbers separated by space): ").split()))
        if len(row) != 9:
            print("Each row must contain exactly 9 numbers.")
            return None
        board.append(row)
    return board

def main():
    """Main function to run the Sudoku solver."""
    board = input_board()
    if board:
        if validate_board(board):
            if solve_sudoku(board):
                print("Sudoku puzzle solved:")
                print_board(board)
            else:
                print("No solution exists.")
        else:
            print("The input board is invalid.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()