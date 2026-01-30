import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scalar import Scalar
from vector import Vector
from matrix import Matrix

u = 21
v = 42
t = 0.3

scalar = Scalar()
# print(scalar.lerp(u, v, t))

vector = Vector([0,0])
u = Vector([2,1])
v = Vector([4,2])
t = 0.3

# print(vector.lerp(u,v,t))

matrix = Matrix([[0,0], [0,0]])
u = Matrix([[2,1], [3, 4]])
v = Matrix([[20,10], [30, 40]])
t = 0.5
print(matrix.lerp(u,v,t))