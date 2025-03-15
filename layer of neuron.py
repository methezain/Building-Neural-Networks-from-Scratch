# A single layer of neurons with 4 inputs, and 3 outputs

inputs = [1, 2, 3, 4]

weights = [
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]

bias = [2.4, 3.1, 0.5]

neuron1 = weights[0][0]*inputs[0] + weights[0][1]*inputs[1] + weights[0][2]*inputs[2] + weights[0][3]*inputs[3] + bias[0] 
neuron2 = weights[1][0]*inputs[0] + weights[1][1]*inputs[1] + weights[1][2]*inputs[2] + weights[1][3]*inputs[3] + bias[1]
neuron3 = weights[2][0]*inputs[0] + weights[2][1]*inputs[1] + weights[2][2]*inputs[2] + weights[2][3]*inputs[3] + bias[2]

outputs = [neuron1, neuron2, neuron3]
print(outputs) 