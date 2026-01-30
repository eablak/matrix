import sys

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    
    def check_add_sum(self, matrix2):

        # type check
        for dim in self.matrix:
            if type(dim) != list:
                raise TypeError("Result is undefined")

        for dim in matrix2.matrix:
            if type(dim) != list:
                raise TypeError("Result is undefined")

        # size check

        if len(self.matrix) != len(matrix2.matrix):
            raise TypeError("Result is undefined")

        elem_count = 0
        for i in range(len(self.matrix)):
            if elem_count == 0:
                elem_count = len(self.matrix[i])
            if len(self.matrix[i]) != elem_count or len(matrix2.matrix[i]) != elem_count:
                raise TypeError("Result is undefined")
            if len(self.matrix[i]) != len(matrix2.matrix[i]):
                raise TypeError("Result is undefined")


    def check_scalar(self, scalar):
        if type(scalar) != int and type(scalar) != float:
            raise TypeError("Result is undefined")


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

    def check_lerp(self, u, v, t):
        if (type(u) != Matrix or type(v) != Matrix or (type(t) != int and type(t) != float)):
            raise TypeError("Result is undefined")
        
        if (len(self.matrix) != len(u.matrix) or len(self.matrix) != len(u.matrix)):
            raise TypeError("Result is undefined")

        elem_count = 0
        for dim in range(len(self.matrix)):
            if elem_count == 0:
                elem_count = len(self.matrix[dim])
            if len(self.matrix[dim]) != elem_count or len(u.matrix[dim]) != elem_count or len(v.matrix[dim]) != elem_count:
                raise TypeError("Result is undefined")
            

    def lerp(self, u, v, t):
        
        self.check_lerp(u,v,t)

        for dim in range(len(u.matrix)):
            for i in range(len(u.matrix[dim])):
                self.matrix[dim][i] = u.matrix[dim][i] + t * (v.matrix[dim][i] - u.matrix[dim][i])
        
        return self.matrix
