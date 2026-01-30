import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vector import Vector

if __name__ == "__main__":
    u = Vector([2, 3])
    v = Vector([5, 7])
    

    # u.add(v)
    # u.subtraction(v)
    u.scaling(2)
    
    print(u.vector)