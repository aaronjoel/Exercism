class Matrix:
    def __init__(self, matrix_string):
        self.mat_string = matrix_string
        _mat_gen = list(map(int, _row.split()) for _row in self.mat_string.split('\n'))
        self.matrix = [list(row_gen) for row_gen in _mat_gen]
        self.nrows = len(self.matrix)
        self.ncols = len(self.matrix[0])

    def row(self, index):
        try:
            indx = index - 1
            return self.matrix[indx]
        except IndexError:
            raise Exception('index out of range')

    def column(self, index):
        try:
            indx = index - 1
            return [self.matrix[i][indx] for i in range(self.nrows)]
        except IndexError:
            raise Exception('index out of range')
