#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:38:04 2024

@author: ryan
"""



def isValid(grid, row, col, num):
    # Check if num is not in the current row
    for i in range(9):
        if num == grid[row][i]:
            return False
    # Check if num is not in the current column
    for j in range(9):
        if num == grid[j][col]:
            return False
    # Check if num is not in the 3x3 subgrid

    gridX = (col//3) *3
    gridY = (row//3) *3
    
    for k in range(3):
        for l in range(3):
            if num == grid[gridY + k][gridX + l]:
                return False
    
    return True  # or False

def findEmpty(grid):
    # Loop through the grid row by row
    for r in range(9):  # Loop through rows
        for c in range(9):  # Loop through columns
            if grid[r][c] == 0:  # Check if cell is empty
                return (r, c)  # Return the first empty cell
    
    # If no empty cell is found, return None
    return None


def solve(grid):
    # Base case: if no empty cells, puzzle is solved
    empty = findEmpty(grid)
    if not empty:
        return True
    
    row, col = empty

    for num in range(1, 10):
        if isValid(grid, row, col, num):
            # Place the number
            grid[row][col] = num

            # Recursively attempt to solve the grid
            if solve(grid):
                return True

            # If it doesn't work, reset the cell (backtrack)
            grid[row][col] = 0
    
    return False


def print_grid(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:  # Add horizontal line after every 3 rows (but not the first row)
            print("-" * 21)  # 21 dashes to fit the grid formatting
        
        for c in range(9):
            if c % 3 == 0 and c != 0:  # Add vertical line after every 3 columns (but not the first column)
                print("|", end=" ")
            
            # Print the number with a space after it
            print(grid[r][c] if grid[r][c] != 0 else ".", end=" ")

        print()  # Move to the next line after each row

def main():
    grid = [
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

    if solve(grid):
        print("Solved Sudoku:")
        print_grid(grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
