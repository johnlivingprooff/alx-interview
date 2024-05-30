#!/usr/bin/python3
"""NxN queens problem"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for c in range(col):
        if board[c] == row or \
           board[c] - c == row - col or \
           board[c] + c == row + col:
            return False
    return True


def solve(board, col):
    """Solve N queens problem"""
    if col == N:
        print([[c, board[c]] for c in range(N)])
        return
    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            solve(board, col + 1)


if __name__ == "__main__":
    solve([0 for i in range(N)], 0)
