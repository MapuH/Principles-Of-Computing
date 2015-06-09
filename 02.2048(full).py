"""
Clone of 2048 game.
"""

import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = [x for x in line if x !=0]
    while len(new_line) < len(line):
        new_line.append(0)
    for ind in range(len(new_line)-1):
        if new_line[ind] == new_line[ind+1]:
            new_line[ind] *= 2
            new_line.pop(ind+1)
            new_line.append(0)
    return new_line

def traverse_grid(start_cell, direction, num_steps):
    """
    Helper function that iterates over the cells
    in a grid in a linear direction and returns
    a list of their indices.
    """
    indices = list()
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        indices.append((row, col))
    return indices

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._initial_tiles = {UP: [(0, i) for i in range(self._grid_width)],
                              DOWN: [(self._grid_height-1, i) for i in range(self._grid_width)],
                              LEFT: [(i, 0) for i in range(self._grid_height)],
                              RIGHT: [(i, self._grid_width-1) for i in range(self._grid_height)]}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == 1 or direction == 2:
            steps = self._grid_height
        else:
            steps = self._grid_width
            
        tile_changed = False
            
        for tile in self._initial_tiles[direction]:
            index_list = traverse_grid(tile, OFFSETS[direction], steps)
            
            temp_list = list()
            for ind in index_list:
                value = self.get_tile(ind[0],ind[1])
                temp_list.append(value)
                
            merged = merge(temp_list)
            if merged != temp_list:
                tile_changed = True
            
            for ind, val in zip(index_list, merged):
                self.set_tile(ind[0], ind[1], val)
                
        if tile_changed:
            self.new_tile()
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        weighted_2or4 = [2] * 9 + [4]
        empty_cells = [(i, j) for i in range(self._grid_height) for j in range(self._grid_width) if self._grid[i][j] == 0]
        if len(empty_cells) > 0:
            rand_cell = random.choice(empty_cells)
            rand_value = random.choice(weighted_2or4)
            self.set_tile(rand_cell[0], rand_cell[1], rand_value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))