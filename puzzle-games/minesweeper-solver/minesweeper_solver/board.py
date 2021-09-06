import random
from tile import Tile

class Board:
    def __init__(self, width, height, num_mines):
        self.board = []
        self.width = width
        self.height = height
        self.num_mines = num_mines

        self.add_tiles_to_board()
    
    def __str__(self):
        return f'{str(self.__class__)}'
    
    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield self.board[i][j]
            
    def _is_inbounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    def add_tiles_to_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Tile((i,j)))
            self.board.append(row)

    def add_mines(self, tile):
        """
        Randomly add the number of mines to the board.
        """

        i = tile.i 
        j = tile.j

        ignore_tiles = set()
        ignore_tiles.add((i,j)) 

        for neighbour_tile in self.get_neighbours(tile):
            ignore_tiles.add((neighbour_tile.i, neighbour_tile.j))

        mines_to_add = self.num_mines

        while mines_to_add > 0:
            ri = random.randint(0, self.height - 1)
            rj = random.randint(0, self.width - 1)
            new_tile = self.board[ri][rj]
            # dont place a mine in the same spot twice
            if new_tile.is_mine() or (new_tile.i, new_tile.j) in ignore_tiles:
                continue
            new_tile.make_mine()
            self.increment_adjacents(new_tile)
            mines_to_add -= 1

    def increment_adjacents(self, tile):
        """
        increments all adjacents of mines by 1 that are not mines
        """

        for neighbour_tile in self.get_neighbours(tile):
            neighbour_tile.num_adjacent_mines += 1
            neighbour_tile._is_blank = False
    
    def get_neighbours(self, tile):
        """
        Returns a list of all inbounds coorinates of the given
        i & j. 
        """

        i, j = tile.i, tile.j
        
        directions = [
            (i - 1, j), # up
            (i + 1, j), # down
            (i, j - 1), # left
            (i, j + 1), # right
            (i - 1, j - 1), # top_left
            (i - 1, j + 1), # top_right
            (i + 1, j - 1), # bottom_left
            (i + 1, j + 1), # bottom_right
        ]

        for ni, nj in directions:
            if self._is_inbounds(ni,nj):
                yield self.board[ni][nj]