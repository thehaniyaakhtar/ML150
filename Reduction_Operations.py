# Reduction Operations
# collapses a tensor along one or more axes into fewer values
# instead of keeping all elements, reduce them to a summary
# sum, mean, max

import numpy as np
A = np.array([1, 2, 3, 4])

np.sum(A)
np.mean(A)
np.max(A)
# Entire tensor into a single value

# 2D Tensor
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Axis 0: (down rows)
# Axis 1: (across columns)

np.sum(A, axis = 0) # colapses rows, keeps columns; [1+4, 2+5, 3+6] = [5, 7, 9]
np.sum(A, axis = 1) # colapses columns, keeps rows; [1+2+3, 4+5+6] = [6, 15]

np.max(A, axis=0) # [4, 5, 6]
np.max(A, axis=1) # [3, 6]


# keepsdims
np.sum(A, axis=1, keepdims=True)



