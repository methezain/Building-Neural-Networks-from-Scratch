# layer 1 = 3 neurons 
# layer 2 = 3 neurons 
# layer 3 = 2 neurons

import numpy as np 

inputs = [[1, 2, 3, 2.5],
          [2., 5., -1., 2],
          [-1.5, 2.7, 3.3, -0.8]] # -> 4 inputs in each batch

weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]] # -> 3 neurons, 4 weights

biases = [2, 3, 0.5]

weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]] # -> 3 neurons, 3 weights

biases2 = [-1, 2, -0.5]

weights3 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33]] # -> 2 neurons, 3 weights

biases3 = [1, -2] 

# Convert lists to numpy arrays
inputs_array = np.array(inputs)
weights_array = np.array(weights)
biases_array = np.array(biases)
weights2_array = np.array(weights2)
biases2_array = np.array(biases2)
weights3_array = np.array(weights3)
biases3_array = np.array(biases3)

layer1_outputs = np.dot(inputs_array, weights_array.T) + biases_array

layer2_outputs = np.dot(layer1_outputs, weights2_array.T) + biases2_array

layer3_outputs = np.dot(layer2_outputs, weights3_array.T) + biases3_array
print(layer3_outputs)
