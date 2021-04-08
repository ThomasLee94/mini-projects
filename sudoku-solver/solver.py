recursion = 0

def solve_sudoku_single(board, blanks=None):
    """
    Do not return anything, modify board in-place instead.
    """
    if blanks is None:
        blanks = find_all_blanks(board)

    # print_board(board, blanks) # UNCOMMENT to see all insertions

    global recursion 
    recursion += 1

    if is_solved(board):
        print_board(board, blanks)
        return board
    
    i, j = find_first_blank(board)

    # fill with valid num
    for num in valid_insertions(board, i, j):
      board[i][j] = str(num)
      solution = solve_sudoku_single(board, blanks)
      if solution:
        return solution

    board[i][j] = '.'

def find_all_blanks(board):
    blanks = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                blanks.append((i,j))
    
    return blanks

def find_first_blank(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == ".":
        return i, j
  
def is_solved(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == ".":
        return False
  
  return True

def valid_insertions(board, i, j):
    box_nums = set(get_box_nums(board, i, j))
    row_nums = set()
    col_nums = set()

    for nj in range(9):
      if board[i][nj] != ".":
          if int(board[i][nj]) in row_nums:
              return False
          else:
              row_nums.add(board[i][nj])
    
    for ni in range(9):
      if board[ni][j] != ".":
          if int(board[ni][j]) in col_nums:
              return False
          else:
              col_nums.add(board[ni][j])

    all_nums = set(map(str, range(1, 10)))
    illegal_nums = row_nums.union(col_nums).union(box_nums)

    return all_nums.difference(illegal_nums)


def get_box_nums(board, i, j):
    tl_i = i // 3 * 3
    tl_j = j // 3 * 3

    nums = []
    for ni in range(tl_i, tl_i + 3):
        for nj in range(tl_j, tl_j + 3):
           if board[ni][nj] != ".":
            nums.append(board[ni][nj])
    return nums

def print_board(board, blanks=None):
    ENDC = '\033[0m'
    RED = '\033[91m'
    GRN = '\033[92m'
    BLU = '\033[94m'
    PNK = '\033[95m'

    if blanks is None:
        blanks = []

    res = ""

    for i in range(9):
        if i % 3 == 0:
            res += "\n"
            res += "-" * 25
        res += "\n"
        
        for j in range(9):
            if j % 3 == 0:
                res += "| " 
            if (i,j) in blanks:
                res += RED
            if board[i][j] == ".":
                res += "  " 
            else:
                res += board[i][j]
                res += " "
            if (i,j) in blanks:
                res += ENDC
        res += "|"
    res += "\n"
    res += "-" * 25

    print(res)
  
if __name__ == "__main__":

    board_hard = [
    ['6', '8', '.', '.', '.', '7', '3', '.', '.'],
    ['.', '.', '1', '8', '.', '.', '.', '.', '.'],
    ['4', '.', '.', '.', '.', '.', '.', '8', '.'],
    ['.', '.', '9', '7', '.', '1', '.', '4', '3'],
    ['.', '.', '.', '.', '3', '.', '6', '.', '7'],
    ['.', '.', '.', '.', '.', '.', '.', '9', '.'],
    ['.', '.', '6', '.', '.', '.', '9', '.', '4'],
    ['.', '.', '7', '.', '5', '8', '.', '.', '.'],
    ['.', '9', '.', '.', '.', '.', '.', '.', '.']
    ]

    board_easy = [
    ['3', '.', '6', '5', '.', '8', '4', '.', '.'], 
    ['5', '2', '.', '.', '.', '.', '.', '.', '.'], 
    ['.', '8', '7', '.', '.', '.', '.', '3', '1'], 
    ['.', '.', '3', '.', '1', '.', '.', '8', '.'], 
    ['9', '.', '.', '8', '6', '3', '.', '.', '5'], 
    ['.', '5', '.', '.', '9', '.', '6', '.', '.'], 
    ['1', '3', '.', '.', '.', '.', '2', '5', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', '7', '4'], 
    ['.', '.', '5', '2', '.', '6', '3', '.', '.']]

    print("Given Board")
    print_board(board_easy)

    solve_sudoku_single(board_easy)
    print('\n')
    print(recursion)