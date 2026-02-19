import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from matrix import Matrix

if __name__ == "__main__":

    # u = Matrix([[8., 5., -2.],
    #             [4., 7., 20.],
    #             [7., 6., 1.],])
    
    # u = Matrix([[ 8., 5., -2., 4.],
    #             [ 4., 2.5, 20., 4.],
    #             [ 8., 5., 1., 4.],
    #             [28., -4., 17., 1.],])

    u = Matrix([[1,0,0],[0,1,0],[0,0,1]])

    print(u.determinant())