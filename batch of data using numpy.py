# batch of data : example of matrix vs. matric multiplication

import numpy as np

inputs = [
    [1.0, 2.0, 3.0, 2.5], 
    [2.0, 5.0, -1.0, 2.0], 
    [-1.5, 2.7, 3.3, -0.8]
    ]

weights = [
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]

biases = [2.0, 3.0, 0.5]

inputs_array = np.array(inputs)
weights_array = np.array(weights)
biases_array = np.array(biases)

outputs = np.dot(weights_array, inputs_array.T) + biases_array
# outputs = np.dot(inputs_array, weights_array.T) + biases_array -> Can also be written as this
print(outputs)
