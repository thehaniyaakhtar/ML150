import numpy as np

A = np.array[1, 0, 1]
B = np.array[1, 1, 0]

np.dot(A, B)
# multiply element wise, then sum: reduction

# states how aligned 2 vectors are
# if they point in the same direction: positive
# 0: perpendicular
# negative: opp direction

# Cross Product 
np.cross(A, B)
# returns a vector perpendicular to both A and B
# it requires vectors of the same length
