inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output_layer = []

for neuron_weights, neuron_bias in zip(weights, biases): 
    neuron = 0
    for neuron_weights, input in zip(neuron_weights, inputs):
        neuron += neuron_weights * input                     # y = w*x 
    
    neuron += neuron_bias     # = w*x + b
    output_layer.append(neuron) 

print(output_layer) # it should give 3 outputs
