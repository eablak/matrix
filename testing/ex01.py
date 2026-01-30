import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vector import Vector

vector = Vector([0,0,0])

e1 = Vector([1,0,0])
e2 = Vector([0,1,0])
e3 = Vector([0,0,1])

v1 = Vector([1, 2, 3])
v2 = Vector([0, 10, -100])

# combination_vector = vector.linear_combination([e1, e2, e3], [10, -2, 0.5])
combination_vector = vector.linear_combination([v1, v2], [10, -2])
print(combination_vector.vector)