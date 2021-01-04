# SudokuSolver
An Application of Backtracking in Python. 
This is a program where user can **Create** and **Get Solutions** for their Sudoku puzzels.

# Logic
The algorithm works by placing a number in an empty cell of the puzzle, and checks if it is valid for the row, column, and the smaller 3 * 3 box, and moves on to the next empty box. When it comes across a situation when it cannot put a valid number, it **BACKTRACKS** to previous filled spot and tries to look for another number. It's way faster than the Brute force approach, which have an exponential run time.

# Try it out in GitPod
(https://gitpod.io#https://github.com/mahak999/sudokuSolver)

# Additional Resources
I used this [video](https://www.youtube.com/watch?v=lK4N8E6uNr4&t=98s) to understand the process behind backtracking. Huge thanks to Tim @ Tech with tim for the wonderful explanation.
