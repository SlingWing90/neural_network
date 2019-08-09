from classes.neuron import Neuron
from classes.processor import Processor

# Learning XOR
# -----------
# X1 | X2 | Y
# -----------
# 0  | 0  | 0
# 0  | 1  | 1
# 1  | 0  | 1
# 1  | 1  | 0
# -----------

neuron_1 = Neuron("1", 1, None, None);
neuron_2 = Neuron("2", 1, None, None);
neuron_3 = Neuron("3", None, 0.8, [[0.5, neuron_1], [0.4, neuron_2]])
neuron_4 = Neuron("4", None, -0.1, [[0.9, neuron_1], [1.0, neuron_2]])
neuron_5 = Neuron("5", None, 0.3, [[-1.2, neuron_3], [1.1, neuron_4]])

neuronal_network = [];
neuronal_network.append(neuron_1)
neuronal_network.append(neuron_2)
neuronal_network.append(neuron_3)
neuronal_network.append(neuron_4)
neuronal_network.append(neuron_5)

X = [[0, 0], [1, 0], [0, 1], [1, 1]]
Y = [0, 1, 1, 0]
#learning_rate = 0.1
#learning_threshold = 0.001

pr = Processor(neuronal_network, X, Y)

pr.print_weight(neuron_5)

pr.learn(1)

print("")
pr.print_result()

print("")
pr.print_weight(neuron_5)