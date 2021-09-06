# Solver 
# write an algo that picks a 100% safe box with given info, and store mines that 
# adding more bombs & grids makes it more difficult

# avoid bombs in the coordinate that the user chooses

# search for all zeros that are connected to ititial 0 (bfs or dfs)
 
from game import Game
import random

class MineSweeperSolver:
    def __init__(self, width, height, num_mines):
        self.game = Game(width, height, num_mines) 
    
    def get_selected_tiles(self):
        """
        Returns a list of all selected tiles
        """
        visible_nums = []

        for row in self.game.board.board:
            for tile in row:
                if tile.is_selected():
                    visible_nums.append(tile)
        
        return visible_nums
    
    def get_adjacent_flags(self, tile):
        """
        Returns a list of all adjacents that are
        flags from i & j.
        """
        flags = []

        for neighbour_tile in self.game.board.get_neighbours(tile):
            if neighbour_tile.is_flagged():
                flags.append(neighbour_tile)
        
        return flags
    
    def get_hidden_neighbours(self, tile):
        """
        Returns a list of all neighbours that are hidden
        from coord i & j.
        """
        hidden_neighbours = []

        for neighbour_tile in self.game.board.get_neighbours(tile):
            if not neighbour_tile.is_selected():
                hidden_neighbours.append(neighbour_tile)
        
        return hidden_neighbours

    def is_satisfied(self, tile):
        """
        If the number of flags next to a numbered tile is equal to the tiles number
        """
        flags = self.get_adjacent_flags(tile)
        return len(flags) == tile.num_adjacent_mines
    
    def make_random_selection(self):
        """
        Select a random tile that has not yet been selected or flagged.
        """

        i = random.randint(0, self.game.height - 1)
        j = random.randint(0, self.game.width - 1)

        tile = self.game.board.board[i][j]

        if not tile.is_selected():
            self.game.board.select(tile)
        else:
            self.make_random_selection()

    def identify_selections(self):
        """
        Find all selections with 100% certainty.
        """

        for tile in self.get_selected_tiles():
            if self.is_satisfied(tile):
                neighbours = self.game.board.get_neighbours(tile)
                for neighbour in neighbours:
                    if (not neighbour.is_selected() and not neighbour.is_flagged()):
                        yield neighbour
    
    def identify_flags(self):
        """
        Finds all flags with 100% certainty.
        """

        for tile in self.get_selected_tiles():
            hidden_neighbours = self.get_hidden_neighbours(tile)
            if self.hidden_neighbours_are_mines(tile, hidden_neighbours):
                for neighbour in hidden_neighbours:
                    if not neighbour.is_flagged():
                        yield neighbour
    
    def hidden_neighbours_are_mines(self, tile, hidden_neighbours):
        return tile.num_adjacent_mines == len(hidden_neighbours) 

    def solve(self):
        """
        Runs the solver.
        """
        self.make_random_selection()
        self.game.display_board()

        while not self.game.board.game_lost() and not self.game.board.game_won():
            change_made = False

            for tile in self.identify_flags():
                change_made =  True
                self.game.board.flag(tile)
            print('Flaggings')
            self.game.display_board()

            for tile in self.identify_selections():
                change_made = True
                self.game.board.select(tile)
            print('Selections')
            self.game.display_board()

            if not change_made:
                self.make_random_selection()
                print('----- Random selection -----')
                self.game.display_board()
        
        if self.game.board.game_won():
            print("You won!")
        else:
            print("You Lost")

if __name__ == "__main__":
    game = MineSweeperSolver(10, 10, 10)
    print(game.game)
    print(game.solve())
