import sys

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix


    def returnType(self, param):
        return type(param)
    

    def returnMatrixDimTypes(self, matrix):
        types = []

        for dim in matrix.matrix:
            types.append(type(dim))
        return types
    

    def returnMatrixDimSizes(self, matrix):
        sizes = []
        
        for i in range(len(matrix.matrix)):
            sizes.append(len(matrix.matrix[i]))
        return sizes
    
    
    def createReturnMatrix(self, sizes):

        matrix = Matrix([])

        for size in sizes:
            matrix.matrix.append([0] * size)
        return matrix


    def add(self, matrix2):

        if (self.returnType(matrix2) != Matrix):
            raise TypeError("Result is undefined")

        if (self.returnMatrixDimTypes(self) != self.returnMatrixDimTypes(matrix2)):
            raise TypeError("Result is undefined")
        
        if (self.returnMatrixDimSizes(self) != self.returnMatrixDimSizes(matrix2)):
            raise TypeError("Result is undefined")

        returnMatrix = self.createReturnMatrix(self.returnMatrixDimSizes(self))

        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                returnMatrix.matrix[dim][i] = self.matrix[dim][i] + matrix2.matrix[dim][i]

        return returnMatrix


    def subtraction(self, matrix2):

        if (self.returnType(matrix2) != Matrix):
            raise TypeError("Result is undefined")

        if (self.returnMatrixDimTypes(self) != self.returnMatrixDimTypes(matrix2)):
            raise TypeError("Result is undefined")
        
        if (self.returnMatrixDimSizes(self) != self.returnMatrixDimSizes(matrix2)):
            raise TypeError("Result is undefined")
        
        returnMatrix = self.createReturnMatrix(self.returnMatrixDimSizes(self))
        
        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                returnMatrix.matrix[dim][i] = self.matrix[dim][i] - matrix2.matrix[dim][i]

        return returnMatrix


    def scaling(self, scalar):

        if self.returnType(scalar) != int and self.returnType(scalar) != float:
            raise TypeError("Result is undefined")
        
        returnMatrix = self.createReturnMatrix(self.returnMatrixDimSizes(self))

        for dim in range(len(self.matrix)):
            for i in range(len(self.matrix[dim])):
                returnMatrix.matrix[dim][i] = self.matrix[dim][i] * scalar

        return returnMatrix


    def lerp(self, u, v, t):
        
        if (self.returnType(u) != self.returnType(v) != Matrix):
            raise TypeError("Result is undefined")
        if (self.returnType(t) != int and self.returnType(t) != float):
            raise TypeError("Result is undefined")
        if (self.returnMatrixDimTypes(u) != self.returnMatrixDimTypes(v)):
            raise TypeError("Result is undefined")
        if (self.returnMatrixDimSizes(u) != self.returnMatrixDimSizes(v)):
            raise TypeError("Result is undefined")

        returnMatrix = self.createReturnMatrix(self.returnMatrixDimSizes(u))

        for dim in range(len(u.matrix)):
            for i in range(len(u.matrix[dim])):
                returnMatrix.matrix[dim][i] = u.matrix[dim][i] + t * (v.matrix[dim][i] - u.matrix[dim][i])
        
        return returnMatrix.matrix
