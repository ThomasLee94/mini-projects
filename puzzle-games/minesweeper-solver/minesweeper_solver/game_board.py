from board import Board
from game_tile import GameTile

class GameBoard(Board):
    def __init__(self, width, height, num_mines):
        super().__init__(width, height, num_mines)
        self.total_selections = 0
        self.mine_selected = False

    def add_tiles_to_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(GameTile((i,j)))
            self.board.append(row)

    def select(self, game_tile):
        '''
        Selects given tile if it is selectable, if the tile
        is blank recursively select all of its neighbours
        '''
        if self.total_selections == 0:
            self.add_mines(game_tile)

        if game_tile.is_selected() or game_tile.is_flagged():
            return

        self.total_selections += 1
        game_tile._is_selected = True

        if game_tile.is_mine():
            self.mine_selected = True

        # if selected tile is blank, recurse over its blank neighbours.
        if game_tile.is_blank():
            for neighbour_tile in self.get_neighbours(game_tile):
                if neighbour_tile.is_blank():
                    self.select(neighbour_tile)

    def flag(self, game_tile):
        """
        Flags/deflags at the given coordinate
        """
        # deflag
        if game_tile.is_flagged():
            game_tile._is_flagged = False
        # flag
        else:
            game_tile._is_flagged = True

    def game_over(self):
        return self.game_won() is True or self.game_lost() is True

    def game_won(self):
        return self.width * self.height - self.num_mines == self.total_selections
    
    def game_lost(self):
        return self.mine_selected