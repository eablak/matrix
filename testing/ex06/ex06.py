import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from vector import Vector

if __name__ == "__main__":

    u = Vector([4,2,-3])
    v = Vector([-2,-5,16])
    
    print(u.cross_product(u, v))