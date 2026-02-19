import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from vector import Vector

if __name__ == "__main__":

    u = Vector([0, 0, 0])
    u = Vector([1, 2, 3])
    # u = Vector([-1, 2])
    
    print(u.norm_1())
    print(u.norm())
    print(u.norm_inf())