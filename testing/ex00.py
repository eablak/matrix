import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vector import Vector
from matrix import Matrix


if __name__ == "__main__":

    # check Vector
    u = Vector([2, 3])
    v = Vector([5, 7])
    

    # res = u.add(v)
    # res = u.subtraction(v)
    res = u.scaling(2)
    
    print(res.vector)


    # check Matrix
    """ u = Matrix([
        [1, 2],
        [3, 4]
    ])
    
    v = Matrix([
        [7, 4],
        [-2, 2]
    ])


    # res = u.add(v)
    # res = u.subtraction(v)
    res = v.scaling(2)

    print(res.matrix)"""