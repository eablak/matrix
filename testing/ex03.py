import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vector import Vector

if __name__ == "__main__":

    u = Vector([-1, 6])
    v = Vector([3, 2])
    
    w = u.dot(u,v)
    
    print(w)