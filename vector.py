class Vector:
    
    def __init__(self, vector):
        self.vector = vector


    def add(self, vector2):
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] + vector2.vector[i]


    def subtraction(self, vector2):
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] - vector2.vector[i]


    def scaling(self, scalar):
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] * scalar


    def linear_combination(self, vectors ,coefs):

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
    