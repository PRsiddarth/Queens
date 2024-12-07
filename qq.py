n = 4

def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_util(board, col):
        if col >= n:
            result.append([''.join('Q' if cell else '.' for cell in row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve_util(board, col + 1)
                board[i][col] = 0

    result = []
    board = [[0] * n for _ in range(n)]
    solve_util(board, 0)
    return result

# Example usage

solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()