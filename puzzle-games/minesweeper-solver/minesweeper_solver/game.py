from game_board import GameBoard

class Game:
    def __init__(self, width, height, num_mines):
        self.board = GameBoard(width, height, num_mines)
        
        self.width = width
        self.height = height
        self.num_mines = num_mines
        
    def __str__(self):
        return f'{str(self.__class__)}'

    def play_game(self):
        """
        Starts the game and asks for user input for terminal game. 
        Runs the rest of the game turn based logic.
        """

        while not self.board.game_over():
            # ask user if they want to place flag or select tile
            f_or_s = None
            while f_or_s != 'f' and f_or_s != 's':
                f_or_s = input('Do you want to (f) Flag or (s) Select? ')

            # ask user for coord to select s or f
            # repeat asking until they give valid input
            i = -1
            while i > self.height or i < 0:
                i = input('i? ')
                if i.isdigit():
                    i = int(i)
                else:
                    i = -1

            j = -1
            while j > self.width or j < 0:
                j = input('j? ')
                if j.isdigit():
                    j = int(j)
                else:
                    j = -1
            
            if not self.board._is_inbounds(i, j):
                print('try again, coordinates out of bounds')
            
            tile = self.board.board[i][j]

            if tile.is_selected():
                print("try again, this tile is already selected")
            elif tile.is_flagged() and f_or_s == 's':
                print('try again, this tile is already flagged')
            elif f_or_s == 's':
                self.board.select(tile)
            elif f_or_s == 'f':
                self.board.flag(tile)
            
            self.display_board()
        
        if self.board.game_lost():
            print("You lost")
        else:
            print("You won")
    
    ########################### VISUALISE BOARD ###########################
    def tile_representation(self, tile):
        """
        Display terminal board function
        """

        if not tile.is_selected() and not tile.is_flagged():
            # block representation of blocked tile
            return '\u2588'

        elif tile.is_flagged():
            # red block to show flag
            return '\033[91m\u2588\033[0m'

        elif tile.is_blank():
            # blank visible tile
            return ' '

        elif tile.is_mine():
            return '\033[91m*\033[0m'
        else:
            # the number on the visible tile
            return str(tile)
    
    def display_board(self):
        """
        Display terminal board function
        """
        rows = []

        for row in self.board.board:
            row_str = ""
            for tile in row:
                row_str += self.tile_representation(tile)
            rows.append(row_str)
        
        for row in rows:
            print(row)
        print()


def debug(game):
    """
    Useful debug function
    """
    for r in game.board.board:
        print(r)

    print()

    for r in game.board.board:
        print(r)

    print()

    game.display_board()


if __name__ == '__main__':
    game = Game(4, 4, 5)
    # debug(game)
    game.play_game()






        

    

