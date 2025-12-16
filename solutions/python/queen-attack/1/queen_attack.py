from itertools import chain

class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row >= 8:
            raise ValueError("row not on board")
        self.row = row
        if column < 0:
            raise ValueError("column not positive")
        if column >= 8:
            raise ValueError("column not on board")
        self.column = column

    def can_attack(self, another_queen):
        if another_queen.row == self.row and another_queen.column == self.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        if self.row == another_queen.row or self.column == another_queen.column:
            return True
            
        
        pos = self.row, self.column
        other = another_queen.row, another_queen.column

        diags = list(chain([pos], zip(range(self.row-1, -1, -1), range(self.column-1, -1, -1)),
                           zip(range(self.row+1, 8, 1), range(self.column+1, 8, 1)),
                           zip(range(self.row+1, 8, 1), range(self.column-1, -1, -1)),
                           zip(range(self.row-1, -1, -1), range(self.column+1, 8, 1))))
        if pos in diags and other in diags:
            return True
            
        return False
        
    