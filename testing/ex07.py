import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vector import Vector
from matrix import Matrix

if __name__ == "__main__":

    u = Matrix([[2,0],[0,2]])
    v = Vector([4,2])
    
    # print(u.mul_vec(v))


    u = Matrix([[3,-5],[6,8]])
    v = Matrix([[2,1],[4,2]])

    print(u.mul_mat(v))