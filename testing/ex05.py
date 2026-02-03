import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vector import Vector

if __name__ == "__main__":

    u = Vector([1,2,3])
    v = Vector([4,5,6])
    
    print(u.angle_cos(u, v))