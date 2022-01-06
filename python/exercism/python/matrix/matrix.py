class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string        

    def row(self, index):
        rows = self.matrix_string.split('\n')
        return [int(x) for x in rows[index - 1].split()]

    def column(self, index):
        rows = self.matrix_string.split('\n')
        rows = [[int(x) for x in row.split()] for row in rows]
        return [row[index -1] for row in rows]