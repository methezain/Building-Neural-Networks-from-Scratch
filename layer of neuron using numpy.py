import numpy as np

# Vector vs. Matrix multiplication 
inputs = [1, 2, 3, 4]

weights = [
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]

bias = [2.4, 3.1, 0.5]

output = np.dot(weights, inputs) + bias 
# can't be written as np.dot(inputs, weights) + bias -> bcz Vector vs. Matrix -> np.dot(a,b) != np.dot(b,a)
print(output) 
