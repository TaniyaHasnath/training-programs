def solve_n_queen(n, board, row, col, diag, rev_diag, asf):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        print()
        return

    for i in range(n):
        if col[i] == 0 and diag[row - i + n - 1] == 0 and rev_diag[row + i] == 0:
            board[row][i] = 1
            col[i] = 1
            diag[row - i + n - 1] = 1
            rev_diag[row + i] = 1
            asf += str(row) + " " + str(i) + " "
            solve_n_queen(n, board, row + 1, col, diag, rev_diag, asf)
            board[row][i] = 0
            col[i] = 0
            diag[row - i + n - 1] = 0
            rev_diag[row + i] = 0
            asf = asf[:-4]

def main():
    n = 4
    board = [[0 for i in range(n)] for j in range(n)]
    col = [0 for i in range(n)]
    diag = [0 for i in range(2 * n - 1)]
    rev_diag = [0 for i in range(2 * n - 1)]
    asf = ' '
    solve_n_queen(n, board, 0, col, diag, rev_diag, asf)

main()