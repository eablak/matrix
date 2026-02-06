import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matrix import Matrix

if __name__ == "__main__":

    u = Matrix([[1, 2], [3, 4], [5, 6]])

    print(u.transpoze())