#!/usr/bin/python3

# solver.py
# python 3.8
# Sudoku solver


def main():
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    print("\n================== SUDOKU SOLVER ==================\n"
    "")
    printBoard(board)
    solve(board)
    enter = input("\nPress Enter to solve this sudoku...\n")
    if enter == '':
        printBoard(board)


def solve(board):
    """
    Solve sudoku using backtracking algorithm
    """
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, num, pos):
    """
    Find digit for the cell, that is not already
    in row or column or box of that cell
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def printBoard(board):
    """
    Pretty print of board
    """
    print("----------------------------------")
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")
            print(board[i][j]," ", end="")
        print("|")
        if (i+1) % 3 == 0:
            print("----------------------------------")

def findEmpty(board):
    """
    Find cell filled with 0
    This cell is not does not contain any digit from 1 to 9
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    return None


if __name__ == "__main__":
    main()


