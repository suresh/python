class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(e) for e in r.split()] for r in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col = [e[index -1] for e in self.matrix]
        return col
