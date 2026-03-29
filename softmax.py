# softmax turns vectors into probabilities

# input
x = [2.0, 1.0, 0.1]

# output [0.66, 0.24, 0.10] sums to 1
# Bigger number → bigger probability
# softmax(xᵢ) = exp(xᵢ) / sum(exp(x))
 import numpy as np
 
 def softmax(x):
     x = x - np.max(x) # stability check, subtracting a constant doesnt change probabilities
     exp_x = np.exp(x)
     return exp_xx / np.sum(exp_x)
     
# for a 2d tensor

def softmax_2d(x):
    x = x - np.max(x, axis = 1, keepdims = True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=1, keepdims = True)
    
# softmax exponentiates: makes the difference bigger
# normalizes: divides by total
# Result: How big is it compared to others

