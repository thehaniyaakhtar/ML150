# Vector Norm
# Measures the magnitude of a vector

# L1 Norm: Manhattan Norm
# Sum of absolute values
# Taking sum of all elements with their magnitudes
# used for sparsity/ feature selection

# L2 Norm: Euclidean Norm
# Straight Line distance
# for smooth stable solutions

import math
x = [3, -4, 5]
l1 = sum(abs(i) for i in x)
l2 = math.sqrt(sum(i**2) for i in x)
print("L1 Norm", l1)
print("L2 Norm", l2)
