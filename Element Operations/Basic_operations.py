# Element wise operations
# apply a function independently to each element 
# A = [1, 2, 3]
# B = [4, 5, 6]
# A + B = [5, 7, 9]

import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(A+B)
print(A-B)
print(A*B)
print(A/B)

# Shapes must match OR be broadcastable
