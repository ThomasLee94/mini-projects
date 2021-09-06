class Tile:
    def __init__(self, coords, num_adjacent_mines=0, is_mine=False):
        i, j = coords

        self.i = i
        self.j = j

        self._is_blank = True 
        self._is_mine = is_mine
        self.num_adjacent_mines = num_adjacent_mines

    def __repr__(self):
        return f'Tile(coords={self.i, self.j}, num_adj_mines={self.num_adjacent_mines}, is_mine={self.is_mine()})'
    
    def __str__(self):
        if self.is_mine():
            return '\033[91m*\033[0m'
        elif self.is_blank():
            # blank visible tile
            return ' '
        else:
            ENDC = '\033[0m'
            colors = [
                None,
                '\033[92m',  # 1 green
                '\033[94m',  # 2 blue
                '\033[91m',  # 3 red
                '\033[95m',  # 4 pink/purple
                '\033[96m',  # 5+ light blue
            ]
            color = colors[min(self.num_adjacent_mines, 5)]
            return f'{color}{self.num_adjacent_mines}{ENDC}'
    
    def __hash__(self):
        return hash((self.i, self.j))
    
    def __eq__(self, other_tile):
        return id(self) == id(other_tile)

    def is_mine(self):
        return self._is_mine

    def is_blank(self):
        return self._is_blank

    def make_mine(self):
        self._is_mine = True
        self._is_blank = False
    