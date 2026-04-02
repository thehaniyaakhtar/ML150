# reshaping tensors
# changing shape

import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])

x.reshape(2, 3)

# figure it out automatically:
x.reshape(2, -1)

# transposing; flipping axes

A = np.array([[1, 2, 3],
              [4, 5, 6]])
              
z = x.T
