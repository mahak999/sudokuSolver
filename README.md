# SudokuSolver
An Application of Backtracking in Python

# Logic
The algorithm works by placing a number in an empty cell of the puzzle, and checks if it is valid for the row, column, and the smaller 3 * 3 box, and moves on to the next empty box. When it comes across a situation when it cannot put a valid number, it BACKTRACKS to previous filled spot and tries to look for another number. It's way faster than the Brute force approach, which have an exponential run time.
