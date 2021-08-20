class Matrix:

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = [*map(lambda x: x.split(),
                            self.matrix_string.split(sep='\n'))]

    def row(self, index):
        if (index < 1) or (index > len(self.matrix)):
            raise Exception("Invalid Index.")
        return [*map(int, self.matrix[index-1])]

    def column(self, index):
        if (index < 1) or (index > len(self.matrix[0])):
            raise Exception("Invalid Index.")
        return [int(self.matrix[x][index-1]) for x in range(len(self.matrix))]

