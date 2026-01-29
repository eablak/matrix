import sys

class Vector:
    
    def __init__(self, vector):
        self.vector = vector


    def check_add_sub(self, vector2):

        v1_type = type(self)
        v2_type = type(vector2)
        if (v1_type != v2_type):
            sys.exit("Result is undefined")

        v1_len = len(self.vector)
        v2_len = len(vector2.vector)
        if v1_len != v2_len:
            sys.exit("Result is undefined")


    def check_scl(self, scalar):
        scl_type = type(scalar)
        if scl_type != int and scl_type != float:
            sys.exit("Result is undefined")


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
                sys.exit("Result is undefined!")

        vector_count = len(vectors)
        coefs_count = len(coefs)
        if (vector_count != coefs_count):
            sys.exit("Result is undefined")


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
    