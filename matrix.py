import sys

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    
    def check_add_sum(self, matrix2):

        # type check
        for dim in self.matrix:
            if type(dim) != list:
                sys.exit("Result is undefined1")

        for dim in matrix2.matrix:
            if type(dim) != list:
                sys.exit("Result is undefined2")

        # size check

        if len(self.matrix) != len(matrix2.matrix):
            sys.exit("Result is undefined3")

        elem_count = 0
        for i in range(len(self.matrix)):
            if elem_count == 0:
                elem_count = len(self.matrix[i])
            if len(self.matrix[i]) != elem_count or len(matrix2.matrix[i]) != elem_count:
                sys.exit("Result is undefined!")
            if len(self.matrix[i]) != len(matrix2.matrix[i]):
                sys.exit("Result is undefined!!")


    def check_scalar(self, scalar):
        if type(scalar) != int and type(scalar) != float:
            sys.exit("Result is undefined5")


    def add(self, matrix2):
        self.check_add_sum(matrix2)
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                self.matrix[dim][i] = self.matrix[dim][i] + matrix2.matrix[dim][i]


    def subtraction(self, matrix2):
        self.check_add_sum(matrix2)
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                self.matrix[dim][i] = self.matrix[dim][i] - matrix2.matrix[dim][i]

    
    def scaling(self, scalar):
        self.check_scalar(scalar)
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                self.matrix[dim][i] = self.matrix[dim][i] * scalar

