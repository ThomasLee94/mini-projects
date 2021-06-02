from collections import deque
import copy

def slidingPuzzle(board) -> int:
    if is_solved(board): return 0

    queue = deque()
    seen = set()
    
    # enqueue the state of the board
    seen.add(board_to_string(board))
    queue.append((board, 0))
    
    while queue:
        popped_board, depth = queue.popleft()
        i, j = find_zero(popped_board)
        next_boards = next_moves(popped_board, i, j)
        
        for new_board in next_boards:
            if board_to_string(new_board) not in seen:
                # if board is solved state, return num moves
                if is_solved(new_board):
                    return depth + 1

                queue.append((new_board, depth + 1))
                seen.add(board_to_string(new_board))
    return -1

def next_moves(board, i, j):
    boards = []
    
    # swap left
    if valid_indicies(board, i, j-1):
        tmp = copy.deepcopy(board)
        tmp[i][j-1], tmp[i][j] = tmp[i][j], tmp[i][j-1]
        boards.append(tmp)
        
    # swap right
    if valid_indicies(board, i, j+1):
        tmp = copy.deepcopy(board)
        tmp[i][j+1], tmp[i][j] = tmp[i][j], tmp[i][j+1]
        boards.append(tmp)
        
    # swap up
    if valid_indicies(board, i-1, j):
        tmp = copy.deepcopy(board)
        tmp[i-1][j], tmp[i][j] = tmp[i][j], tmp[i-1][j]
        boards.append(tmp)
        
    # swap down
    if valid_indicies(board, i+1, j):
        tmp = copy.deepcopy(board)
        tmp[i+1][j], tmp[i][j] = tmp[i][j], tmp[i+1][j]
        boards.append(tmp)
    
    return boards

def valid_indicies(board, i, j):
    if i < 0 or i > len(board) - 1: return False
    if j < 0 or j > len(board[0]) - 1: return False
    
    return True

def is_solved(board):
    board = board_to_string(board)
    
    if int(board[-1]) != 0: return False
    
    for i in range(1, len(board)-1):
        if int(board[i-1]) > int(board[i]): return False
    
    return True
            

def board_to_string(board):
    string = ""
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            string += str(board[i][j])
    
    # print(string)
    return string

def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i,j

if __name__ == "__main__":
    board = [[4,1,2], 
            [5,0,3]]  
    
    #board = [[1, 2, 3],
    #         [0, 4, 5]]

    board_solved = [
        [1,2,3],
        [4,5,0]
    ]
    
    res = slidingPuzzle(board)
    # res = slidingPuzzle(board_solved)
    print(res)

    # print(is_solved(board))
    # print(is_solved(board_solved))