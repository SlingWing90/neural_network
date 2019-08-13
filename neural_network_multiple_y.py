### EXAMPLE

from classes.neuron import Neuron
from classes.processor import Processor

# LEARNING XOR
# -----------
# X1 | X2 | Y
# -----------
# 0  | 0  | 0
# 0  | 1  | 1
# 1  | 0  | 1
# 1  | 1  | 0
# -----------

neuron_1 = Neuron("1", None, None);
neuron_2 = Neuron("2", None, None);
neuron_3 = Neuron("3", 0.8, [[0.5, neuron_1], [0.4, neuron_2]])
neuron_4 = Neuron("4", -0.1, [[0.9, neuron_1], [1.0, neuron_2]])
neuron_5 = Neuron("5", 0.3, [[-1.2, neuron_3], [1.1, neuron_4]])

neuron_6 = Neuron("6", 0.5, [[-0.2, neuron_3], [0.2, neuron_4]])

neuronal_network = [];
neuronal_network.append(neuron_1)
neuronal_network.append(neuron_2)
neuronal_network.append(neuron_3)
neuronal_network.append(neuron_4)
neuronal_network.append(neuron_5)

neuronal_network.append(neuron_6)

X = [[0, 0], [1, 0], [0, 1], [1, 1]]
#Y = [[0], [1], [1], [0]]
#Y = [[0, 1], [1, 0], [1, 0], [0, 1]]
Y = [[0, 1], [1, 0], [1, 0], [0, 1]]

#learning_rate = 0.1
#learning_threshold = 0.001

pr = Processor(neuronal_network, X, Y)

print("Weights:")
pr.print_weight(neuron_5)

#print("Weights:")
pr.print_weight(neuron_6)

# TEST
#val = pr.process([1, 1])
#print(val)


print("")
print("Example: ")
for n in X:
	x1 = n[0]
	x2 = n[1]

	val = pr.process([x1, x2])
	print(str(x1)+" "+str(x2))
	print(val)
print("")

pr.learn(1)

print("")
print("Result: ")
pr.print_result()

print("")
print("Weights:")
pr.print_weight(neuron_5)

#print("")
print("Weights 2:")
pr.print_weight(neuron_6)

print("")
print("Example: ")
for n in X:
	x1 = n[0]
	x2 = n[1]

	val = pr.process([x1, x2])
	print(str(x1)+" "+str(x2))
	print(val)
