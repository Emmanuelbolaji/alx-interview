#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid: A 2D grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    land_cells = 0
    adjacent_connections = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                land_cells += 1

                if r < len(grid) - 1 and grid[r+1][c] == 1:
                    adjacent_connections += 1
                if c < len(grid[0]) - 1 and grid[r][c+1] == 1:
                    adjacent_connections += 1

    return 4 * land_cells - 2 * adjacent_connections
