N = 6  # You can change this value to solve for different sizes of the board

def printSolution(board):
    """Prints the chessboard with queens placed."""
    for row in board:
        for cell in row:
            print("Q" if cell == 1 else ".", end=" ")
        print()

def isSafe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    """Utilizes backtracking to solve the N-Queens problem."""
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            board[i][col] = 0  # Backtrack

    return False

def solveNQ():
    """Sets up the board and initiates the solving process."""
    board = [[0 for _ in range(N)] for _ in range(N)]  # Create an N x N board

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

if __name__ == '__main__':
    solveNQ()