import numpy as np

A = np.array[1, 0, 1]
B = np.array[1, 1, 0]

np.dot(A, B)
# multiply element wise, then sum: reduction

# states how aligned 2 vectors are
# if they point in the same direction: positive
# 0: perpendicular
# negative: opp direction

