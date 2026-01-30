import sys

class Vector:
    
    def __init__(self, vector):
        self.vector = vector


    def check_add_sub(self, vector2):

        v1_type = type(self)
        v2_type = type(vector2)
        if (v1_type != v2_type):
            raise TypeError("Result is undefined")


        v1_len = len(self.vector)
        v2_len = len(vector2.vector)
        if v1_len != v2_len:
            raise TypeError("Result is undefined")


    def check_scl(self, scalar):
        scl_type = type(scalar)
        if scl_type != int and scl_type != float:
            raise TypeError("Result is undefined")


    def add(self, vector2):
        self.check_add_sub(vector2)
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] + vector2.vector[i]


    def subtraction(self, vector2):
        self.check_add_sub(vector2)
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] - vector2.vector[i]


    def scaling(self, scalar):
        self.check_scl(scalar)
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] * scalar


    def check_combination(self, vectors, coefs):

        len_vector = 0
        for vector in vectors:
            if len_vector == 0:
                len_vector = len(vector.vector)
            if len_vector != len(vector.vector):
                raise TypeError("Result is undefined")

        vector_count = len(vectors)
        coefs_count = len(coefs)
        if (vector_count != coefs_count):
            raise TypeError("Result is undefined")


    def linear_combination(self, vectors ,coefs):

        self.check_combination(vectors, coefs)

        i = 0
        temp = []
        vector_len = 0
        for vector in vectors:
            temp_list = []
            vector_len = len(vector.vector)
            for v in vector.vector:
                temp_list.append(v * coefs[i])
            i += 1
            temp.append(Vector(temp_list))

        # for t in temp:
        #     print(t.vector)

        combination_vector = Vector([0] * vector_len)

        for i in range(vector_len):
            sum = 0
            for t in temp:
                sum += t.vector[i]
            combination_vector.vector[i] = sum

        return combination_vector
    

    def check_lerp(self, u, v, t):
        if (type(u) != Vector or type(v) != Vector or (type(t) != int and type(t) != float)):
            raise TypeError("Result is undefined")
        if (len(self.vector) != len(u.vector) or len(self.vector) != len(v.vector)):
            raise TypeError("Result is undefined")

    """
    linear interpolation:
        If the two known points are given by the coordinates (x0 , y0) and (x1 , y1), the linear interpolant is the straight line between these points. 

        y-y0/x-x0 = y1-y0/x1-x0

        y = (x-x0)(y1-y0)/(x1-x0) + y0
            -> (x-x0)/(x1-x0) = t(eğim)
        y = (y1-y0)*t + y0
            -> y0 = u, y1 = v
        y = (v-u)*t + u

        lerp(u, v, t) = u + (t * (v - u))
    """
    def lerp(self, u, v, t):

        self.check_lerp(u, v, t)

        for i in range(len(u.vector)):
            self.vector[i] = u.vector[i] +  t * (v.vector[i] - u.vector[i])
        
        return self.vector