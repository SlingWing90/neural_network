import math
#import numpy as numpy

# Learning XOR
# -----------
# X1 | X2 | Y
# -----------
# 0  | 0  | 0
# 0  | 1  | 1
# 1  | 0  | 1
# 1  | 1  | 0
# -----------


class neuron:

	error_gradient = 0;
	weight_correction = []

	def __init__(self, input, theta, prev_neuron):
		self.input = input
		self.theta = theta
		self.prev_neuron = prev_neuron

	def print_neuron(self):
		print("This neuron: ")
		
		print("Prev neurons: ")
		print(self.prev_neuron)

	def print_input(self):
		print(str(self.input))

	#def print_error_gradient(self):
	#	print(str(self.error_gradient));
	
	#def update_weight(self, error):

	def update_weight(self, learning_rate, error):
		self.error_gradient= self.input*(1-self.input)*error
		print(self.error_gradient);
		

		count = 0;
		for n in self.prev_neuron:
			self.weight_correction.append(learning_rate*n[1].input*self.error_gradient)
			count = count + 1;

		#self.theta = self.theta + learning_rate*(-1)*self.error_gradient

		print(self.weight_correction)
		print(learning_rate*(-1)*self.error_gradient) #Theta correction gradient
		#self.theta = self.theta + learning_rate*(-1)*self.error_gradient

		#print(self.theta)

		#for n in self.prev_neuron:


	def update_children_weight(self, error_gradient):
		print("test")

	def calc_y(self):
		y = 0;

		for n in self.prev_neuron:
			y = y + n[1].input*n[0]
		
		y = y - self.theta

		self.input = self.sigmoid(y)
		
		return self.input

	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x)) 

	

neuron_1 = neuron(1, None, None);
neuron_2 = neuron(1, None, None);

neuron_3 = neuron(None, 0.8, [[0.5, neuron_1], [0.4, neuron_2]])
#neuron_3.print_neuron()
print(str(neuron_3.calc_y()))

neuron_4 = neuron(None, -0.1, [[0.9, neuron_1], [1.0, neuron_2]])
print(str(neuron_4.calc_y()))

neuron_5 = neuron(None, 0.3, [[-1.2, neuron_3], [1.1, neuron_4]])
y = neuron_5.calc_y()
print(str(y))

# Error
error = 0 - y;
print("error: "+str(error))

neuron_5.update_weight(0.1, error);

#neuron_5.print_error_gradient();

#error_gradient= y*(1-y)*error
#print("error gradient: "+str(error_gradient))

#neuron_5.set_weight_correction(0.1, error_gradient)
