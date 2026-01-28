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


if __name__ == "__main__":
    
    u = Vector([2, 3])
    v = Vector([5, 7])
    

    """
    
    # Ex00 Testing

    u.add(v)
    u.subtraction(v)
    u.scaling(2)
    
    
    """
    print(u.vector)