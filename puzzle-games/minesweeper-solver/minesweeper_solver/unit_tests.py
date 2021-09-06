from game_board import GameBoard
from game_tile import GameTile
from game import Game
from solver import MineSweeperSolver

########## BOARD TEST ##########

def test_board_no_mines():
    board = GameBoard(5, 5, 5)

    print(board.board)

    assert len(board.board) == 5
    assert len(board.board[0]) == 5 

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            game_tile = board.board[i][j]
            assert isinstance(game_tile, GameTile)
            assert game_tile.i == i
            assert game_tile.j == j

            assert game_tile.is_mine() is False
            assert game_tile.is_blank() is True
            assert game_tile.num_adjacent_mines == 0

def test_board_invisible_tiles():
    board = GameBoard(5, 5, 5)

    invisible_tiles_counter = 5 * 5

    for row in board.board:
        for game_tile in row:
            if not game_tile.is_selected():
                invisible_tiles_counter -= 1
    
    assert invisible_tiles_counter == 0

def test_board_blanks():
    board = GameBoard(5, 5, 5)

    for row in board.board:
        for game_tile in row:
            # if tile val is 0, assert that it is blank
            if game_tile.num_adjacent_mines == 0:
                assert game_tile.is_blank()

            # if tile is blank, assert that val is 0
            if game_tile.is_blank():
                assert game_tile.num_adjacent_mines == 0

            # if tile is not blank, assert that val is great than 0
            else:
                assert game_tile.num_adjacent_mines >= 0

def test_board_with_mines_counter():
    board = GameBoard(5, 5, 6)
    game_tile = board.board[1][1]
    board.select(game_tile)

    assert game_tile.is_mine() is False

    mine_counter = 0
    blank_tile_counter = 0
    all_blank_tiles = (board.width * board.height) - 6

    for row in board.board:
        for new_game_tile in row:
            if new_game_tile.is_mine():
                mine_counter += 1

    assert mine_counter == 6

def test_board_with_mines_adjacent_vals():
    board = GameBoard(5, 5, 5)
    game_tile = board.board[1][1]
    board.add_mines(game_tile)

    for row in board.board:
        for game_tile in row:
            if game_tile.num_adjacent_mines > 0:
                adjacent_mines = 0

                for neighbour_tile in board.get_neighbours(game_tile):
                    if neighbour_tile.is_mine():
                        adjacent_mines += 1
            
                assert game_tile.num_adjacent_mines == adjacent_mines


########## GAME TEST ##########

def test_game_init():
    game = Game(4, 4, 5)

    assert game.board.game_won() is False
    assert game.board.game_lost() is False
    assert game.board.game_over() is False

    assert len(game.board.board) == 4
    assert len(game.board.board[0]) == 4
    assert game.width == 4
    assert game.height == 4
    assert game.num_mines == 5

def test_generate_board_on_select():
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)

    assert game.board.game_won() is False
    assert game.board.game_lost() is False
    assert game.board.game_over() is False

    assert type(game.board) == GameBoard

def test_generate_board_select():
    game = Game(4, 4, 5)
    clicked_tile = game.board.board[1][1]
    game.board.select(clicked_tile)

    assert clicked_tile.is_mine() is False
    assert clicked_tile.is_selected() is True

########## SOLVER TEST ##########

def test_solver_init():
    solver = MineSweeperSolver(4, 4, 5)

    assert len(solver.game.board.board) == 4
    assert len(solver.game.board.board[0]) == 4
    assert solver.game.width == 4
    assert solver.game.height == 4
    assert solver.game.num_mines == 5

