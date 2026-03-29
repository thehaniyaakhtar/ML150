# masking

import numpy as np
A = np.array([10, 20, 30, 40, 50])

mask = A > 20
print(mask)

# helps filter data
# conditional modifications

A[A > 2] = 0
print(A)
# Replace values based on conditions

# combine conditions
A = np.array([5, 10, 15, 20])
mask = (A > 5) & (A < 20)
print(A[mask])
# [10, 15]

# flattening outputs using masking
A = np.array([
    [1, 2],
    [3, 4]
])
print(A[A > 2])

# Mask + Reduction
A = np.array([1, 2, 3, 4, 5])

mean = np.mean(A[A>2])
print(mean)
# compute stats of only selected values

# uses

# ReLU Activation
A = np.array([-2, -1, 0, 1, 2])
A[A < 0] = 0

# ignoring padding
A = np.array([1, 2, 0, 0, 0, 0])
mask = A != 0
print(np.mean(A[mask]))
# ignores useless values

# Loss Functions
errors = np.array([1.0, 0.5, 2.0, 0.2])
large_errors = errors > 1
print(errors[large_errors])
# print large errors

# Clipping values
A = np.array([1, 5, 10, 20])
A[A > 10] = 10
# preventing exploding values
