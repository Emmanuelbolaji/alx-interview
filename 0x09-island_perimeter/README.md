sland_perimeter
Description
This project implements a solution to calculate the perimeter of an island in a 2D grid. The challenge involves analyzing a grid where 1 represents land and 0 represents water, and determining the total perimeter of the island.
Concepts

2D Arrays (Matrices)
Conditional Logic
Perimeter Calculation
Grid Navigation

Requirements

Python 3.4.3
Ubuntu 20.04 LTS
PEP 8 style guide (version 1.7)
No external module imports

Function Specification
island_perimeter(grid):

Input: 2D list of integers
Output: Integer representing the island's perimeter
Constraints:

Grid cells are 1x1 squares
Cells connected horizontally/vertically
Only one island or no island
No internal water "lakes"



Usage
pythonCopygrid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
Author
Osundiran Omobolaji
