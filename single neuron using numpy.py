import numpy as np

# Vector vs. Vector multiplication 
inputs = [1, 2, 3, 4]
weights = [2.3, 1.9, 0.6, 3]
bias = 1

output = np.dot(weights, inputs) + bias 
# output = np.dot(inputs, weights) + bias -> can be written as this too -> bcz Vector vs. Vector -> np.dot(a,b) = np.dot(b,a)
print(output) 
