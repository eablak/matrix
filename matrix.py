import sys
import os

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


    def mul_vec(self, v):
        
        vector = v.createReturnVector(v.returnSize(v.vector))

        index = 0
        for row in self.matrix:
            elem = 0
            for i in range(len(row)):
                elem += row[i] * v.vector[i]
            vector.vector[index] = elem
            index += 1

        return vector.vector
        
    
    def mul_mat(self, v):
        
        matrix = self.createReturnMatrix(self.returnMatrixDimSizes(self))

        for i in range(len(self.matrix)):
            for j in range(len(v.matrix[0])):
                for k in range(len(v.matrix)):
                    matrix.matrix[i][j] += self.matrix[i][k] * v.matrix[k][j]
    
        return matrix.matrix


    def trace(self):

        index, trace = 0, 0
        for row in self.matrix:
            trace += row[index]
            index+=1

        return trace
        

    def transpoze(self):
        
        tr = []
        tr_sizes = []
        for i in range(len(self.matrix[0])):
            tr_list = []
            for row in (self.matrix):
                tr_list.append(row[i])
            tr.append(tr_list)
            tr_sizes.append(len(tr_list))
        

        matrix = self.createReturnMatrix(tr_sizes)
        for i in range(len(matrix.matrix)):
            matrix.matrix[i] = tr[i]
        
        return matrix.matrix
    

    def row_echelon(self):
        
        # this function works as a reduced row echelon form (rref). accordingly ex10 and evo page examples

        mmatrix = self.matrix
        row_len = len(mmatrix)
        col_len = len(mmatrix[0])
        locked_rows = []  # this is for step 2

        # step 1: iterate over the column starting from the left
        for col_i in range(col_len):
            
            # step 2a: select the pivot row
            pivot_row_i = -1

            for row_i in range(row_len):

                # skip this row value, because we are going to zero it out anyway
                if row_i in locked_rows:
                    continue

                # check if the current element is non zero
                if mmatrix[row_i][col_i] != 0:
                    pivot_row_i = row_i
                    break

            # we know the indice of the pivot_row_i
            if pivot_row_i == -1:
                continue

            # step 2b: bring the pivot row to the next locked_row indices
            next_pivot_row_i = (locked_rows[-1] + 1) if len(locked_rows) > 0 else 0


            if pivot_row_i != next_pivot_row_i:
                # swapping
                mmatrix[[next_pivot_row_i, pivot_row_i]] = mmatrix[[pivot_row_i, next_pivot_row_i]]
                pivot_row_i = next_pivot_row_i

            # step 3: scale the pivot row, with our pivot value
            pivot_value = mmatrix[pivot_row_i][col_i]
            # mmatrix[pivot_row_i] = mmatrix[pivot_row_i] / pivot_value
            mmatrix[pivot_row_i] = [x/pivot_value for x in mmatrix[pivot_row_i]]

            # step 4: eliminate all the numbers above and below

            for row_i in range(row_len):

                # skip the pivot row
                if row_i == pivot_row_i:
                    continue

                # eliminate the column element by rescaling the whole row
                lead_coefficient = mmatrix[row_i][col_i]
                # mmatrix[row_i] = mmatrix[row_i] - mmatrix[pivot_row_i] * lead_coefficient
                coeff_row = [x*lead_coefficient for x in mmatrix[pivot_row_i]]
                mmatrix[row_i] = [xi-yi for xi,yi in zip(mmatrix[row_i], coeff_row)]

            # step 5: prepare to move to the next column
            locked_rows.append(pivot_row_i)

        return mmatrix


    def determinant(self):

        matrix_dim_size = len(self.matrix)

        if matrix_dim_size == 1:
            return self.matrix[0][0]
        
        elif matrix_dim_size == 2:
            # detA = a.d -b.c
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        elif matrix_dim_size == 3:
            
            # sarrus method

            self.matrix.append(self.matrix[0])
            self.matrix.append(self.matrix[1])

            right_total = 0
            left_total = 0

            k = 0
            for i in range(3):
                l = k
                m = 2
                right_row = 1
                left_row = 1
                for j in range(3):
                    right_row *= self.matrix[l][j]
                    left_row *= self.matrix[l][m]
                    m-=1
                    l+=1
                k += 1
                right_total += right_row
                left_total += left_row

            return right_total - left_total
        
        elif matrix_dim_size == 4:
            
            # det = a11*A11 + a12*A12 + a13*A13 + a14*A14

            a11 = self.matrix[0][0]
            a12 = self.matrix[0][1]
            a13 = self.matrix[0][2]
            a14 = self.matrix[0][3]

            A11 = (-1) ** (1+1)
            A12 = (-1) ** (1+2)
            A13 = (-1) ** (1+3)
            A14 = (-1) ** (1+4)

            temp = self.matrix
            temp.pop(0)

            A11_matrix, A12_matrix, A13_matrix, A14_matrix = [row[:] for row in temp], [row[:] for row in temp], [row[:] for row in temp], [row[:] for row in temp]

            for row in A11_matrix:
                row.pop(0)
            for row in A12_matrix:
                row.pop(1)
            for row in A13_matrix:
                row.pop(2)
            for row in A14_matrix:
                row.pop(3)

            detA11 = Matrix(A11_matrix).determinant()
            detA12 = Matrix(A12_matrix).determinant()
            detA13 = Matrix(A13_matrix).determinant()
            detA14 = Matrix(A14_matrix).determinant()

            result = (a11 * A11 * detA11) + (a12 * A12 * detA12) + (a13 * A13 * detA13) + (a14 * A14 * detA14)
            return result
        
        else:
            raise TypeError("Result is undefined")
        

    def eliminate(self, base_row, target_row, column, target=0):
        # subtract target row from base row by multiplied with cofactor 
        coffactor = (target_row[column] - target) / base_row[column]
        for i in range(len(target_row)):
            target_row[i] -= coffactor * base_row[i]


    def inverse(self):

        # combine with identity matrix
        combine_matix = [[] for i in self.matrix] 
        for i,row in enumerate(self.matrix):
            combine_matix[i].extend(row + [0]*i + [1] + [0]*(len(self.matrix)-i-1))


        # Gauss-Jordan elimination

        for i in range(len(combine_matix)):
            # if target element is 0, swap it (you can't make it 1)
            if combine_matix[i][i] == 0:
                for j in range(i+1, len(combine_matix)):
                    if combine_matix[j][i] != 0:
                        combine_matix[i], combine_matix[j] = combine_matix[j], combine_matix[i]
                        break
                else:
                    raise ValueError("Matrix is not invertible")
            # make 0 bottom left triangle
            for j in range(i+1, len(combine_matix)):
                self.eliminate(combine_matix[i], combine_matix[j], i)

        # make 0 upper right triangle
        for i in range(len(combine_matix)-1, -1, -1):
            for j in range(i-1, -1, -1):
                self.eliminate(combine_matix[i], combine_matix[j], i)

        # make the diagonal values to 1
        for i in range(len(combine_matix)):
            self.eliminate(combine_matix[i], combine_matix[i], i, target=1)

        # turn as a original matrix
        combine_matix = [combine_matix[i][len(combine_matix[i])//2:] for i in range(len(combine_matix))]
        for i, row in enumerate(combine_matix):
            self.matrix[i] = row

        return self.matrix