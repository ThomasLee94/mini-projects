from tile import Tile

class GameTile(Tile):
    def __init__(self, coords, num_adjacent_mines=0, is_mine=False):
        super().__init__(
            coords, num_adjacent_mines=num_adjacent_mines, is_mine=is_mine
        )
        
        self._is_selected = False
        self._is_flagged = False
    
    def __repr__(self):
        return f'GameTile(coords={self.i, self.j}, selected={self._is_selected}, mine={self.is_mine()})'

    def is_flagged(self):
        return self._is_flagged

    def is_selected(self):
        return self._is_selected
