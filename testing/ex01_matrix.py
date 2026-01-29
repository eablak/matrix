import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matrix import Matrix

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
    u.scaling(2)
    
    """

    u.subtraction(v)
    print(u.matrix)