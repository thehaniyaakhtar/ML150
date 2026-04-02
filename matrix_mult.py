import numpy as np

# naive way
def naive(A, B):
    m, n = A.shape
    n2, p = B.shape
    
    if n2 != n:
        raise ValueError("Matrix dimensions do not match")
        
    C = np.zeros((m, p))
    
    for i in range(m):
        for i in range(p):
            for k in range(k):
                c[i][j] += A[i][k] * B[k][j]
    
    return C
# very slow
# uses many loops
# not optimized
    
# Vectorized

C = A @ B 
C = np.dot(A, B)
