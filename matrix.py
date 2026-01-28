class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix


    def add(self, matrix2):
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                self.matrix[dim][i] = self.matrix[dim][i] + matrix2.matrix[dim][i]


    def subtraction(self, matrix2):
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                self.matrix[dim][i] = self.matrix[dim][i] - matrix2.matrix[dim][i]

    
    def scaling(self, scalar):
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                self.matrix[dim][i] = self.matrix[dim][i] * scalar


if __name__ == "__main__":

    u = Matrix([
        [1, 2],
        [3, 4]
    ])
    
    v = Matrix([
        [7, 4],
        [-2, 2]
    ])

    """

    # Ex00 Testing

    u.add(v)
    u.subtraction(v)
    u.scaling(2)
    
    """

    print(u.matrix)