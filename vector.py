import sys

class Vector:
    
    def __init__(self, vector):
        self.vector = vector


    def returnType(self, param):
        return type(param)


    def returnSize(self, param):
        return len(param)
    

    def createReturnVector(self, sizes):
        
        vector = Vector([])
        vector.vector = [0] * sizes
        return vector


    def add(self, vector2):

        if self.returnType(self) != self.returnType(vector2) != Vector:
            raise TypeError("Result is undefined")
        
        if self.returnSize(self.vector) != self.returnSize(vector2.vector):
            raise TypeError("Result is undefined")

        returnVector = self.createReturnVector(self.returnSize(self.vector))

        for i in range(len(self.vector)):
            returnVector.vector[i] = self.vector[i] + vector2.vector[i]

        return returnVector


    def subtraction(self, vector2):

        if self.returnType(self) != self.returnType(vector2) != Vector:
            raise TypeError("Result is undefined")
        
        if self.returnSize(self.vector) != self.returnSize(vector2.vector):
            raise TypeError("Result is undefined")
        
        returnVector = self.createReturnVector(self.returnSize(self.vector))
        
        for i in range(len(self.vector)):
            returnVector.vector[i] = self.vector[i] - vector2.vector[i]

        return returnVector
        

    def scaling(self, scalar):

        if self.returnType(scalar) != int and self.returnType(scalar) != float:
            raise TypeError("Result is undefined")
        
        returnVector = self.createReturnVector(self.returnSize(self.vector))

        for i in range(len(self.vector)):
            returnVector.vector[i] = self.vector[i] * scalar

        return returnVector


    def linear_combination(self, vectors ,coefs):

        if (self.returnSize(vectors) != self.returnSize(coefs)):
            raise TypeError("Result is undefined")

        len_vector = self.returnSize(vectors[0].vector)
        for vector in vectors:
            if len_vector != self.returnSize(vector.vector):
                raise TypeError("Result is undefined")

        returnVector = self.createReturnVector(len_vector)

        for i in range(len(vectors)):
            multipliedVector = [elem * coefs[i] for elem in vectors[i].vector]
            for j in range(len(returnVector.vector)):
                returnVector.vector[j] += multipliedVector[j]

        return returnVector 


    def lerp(self, u, v, t):

        if (self.returnType(u) != self.returnType(v) != Vector):
            raise TypeError("Result is undefined")
        if (self.returnType(t) != int and self.returnType(t) != float):
            raise TypeError("Result is undefined")
        if (self.returnSize(u.vector) != self.returnSize(v.vector)):
            raise TypeError("Result is undefined")
        
        returnVector = self.createReturnVector(self.returnSize(u.vector))

        for i in range(len(returnVector.vector)):
            returnVector.vector[i] = u.vector[i] +  t * (v.vector[i] - u.vector[i])
        
        return returnVector.vector
    

    def dot(self, u, v):
        
        if (self.returnSize(u.vector) != self.returnSize(v.vector)):
            raise TypeError("Result is undefined")
        
        res = 0
        for i in range(len(u.vector)):
            res += u.vector[i] * v.vector[i]

        return res
    

    def norm_1(self):
        
        norm1 = 0

        for elem in self.vector:
            if elem < 0:
                elem = elem * -1
            norm1 += elem
        
        return norm1
    

    def norm(self):
        
        res = 0
        for elem in self.vector:
            res += pow(elem,2)

        return res ** 0.5
    

    def norm_inf(self):
        
        norm_inf = 0
        for elem in self.vector:
            if elem < 0:
                elem = elem * -1
            if elem > norm_inf:
                norm_inf = elem

        return norm_inf
    