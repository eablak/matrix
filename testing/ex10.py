import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matrix import Matrix

if __name__ == "__main__":

    u = Matrix([[8., 5., -2., 4., 28.],
                [4., 2.5, 20., 4., -4.],
                [8., 5., 1., 4., 17.],])


    print(u.row_echelon())