import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from matrix import Matrix

if __name__ == "__main__":

    u = Matrix([[-2., -8., 4.],[1., -23., 4.], [0., 6., 4.],])

    print(u.trace())