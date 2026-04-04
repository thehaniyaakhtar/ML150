# forward
# y = xW + b

# backward
# dW = x^t dY
# db = ∑dY
# dx = dY W^T


import numpy as np

class Linear:
    def __init__(self, in_features, out_features):
        # Initialize weights and biases
        self.W = np.random.randn(in_features, out_features) * 0.01
        self.b = np.zeros((1, out_features))
        
        # Gradients
        self.dW = None
        self.db = None
        # Cache
        self.x = None
    
    def forward(self, x):
        # x: (batch_size, in_features)
        # returns: (batch_size, out_features)
        self.x = x 
        out = x @ self.W + self.b
        return out
    
    def backward(self, dout):
        # dout: batch_size, out_features
        # Gradients
        self.dW = self.x.T @ dout # (in_features, out_features)
        self.db = np.sum(dout, axis = 0, keepdims=True) # (1, out_features)
        dx = dout @ self.W.T # (batch_size, in_features)
        
        return dx
