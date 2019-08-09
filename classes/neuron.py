import math

class Neuron:

	#error_gradient = 0
	#weight_correction = []

	def __init__(self, title, theta, prev_neuron):
		self.title = title
		self.theta = theta
		self.prev_neuron = prev_neuron
		self.input = 0
		self.weight_correction = []
		self.error_gradient = 0
		
	#def print_neuron(self):
	#	print("This neuron: ")
	#	
	#	print("Prev neurons: ")
	#	print(self.prev_neuron)

	#def print_input(self):
	#	print(str(self.input))

	def update_weight(self, learning_rate, error):
		self.error_gradient= self.input*(1-self.input)*error
		
		self._update_children_weight(learning_rate, self.error_gradient)


	def _update_children_weight(self, learning_rate, error_gradient):
		children_error_gradient = 0

		self.weight_correction = []
		for n in self.prev_neuron:
			#print(n[1].title+" "+str(n[1].input))	
			self.weight_correction.append(learning_rate*n[1].input*error_gradient)
			
			children_error_gradient = n[1].input*(1-n[1].input)*error_gradient*n[0]
			
			if n[1].prev_neuron is not None:
				n[1]._update_children_weight(learning_rate, children_error_gradient)

		# THETA HERE?
		theta_correction = learning_rate*(-1)*error_gradient

		# Weight Correction
		loop_count = 0;
		for wc in self.weight_correction:
			self.prev_neuron[loop_count][0] = self.prev_neuron[loop_count][0] + wc
			loop_count = loop_count + 1; 

		self.theta = self.theta + theta_correction


	def calc_y(self):
		y = 0

		for n in self.prev_neuron:
			y = y + n[1].input*n[0]
		
		y = y - self.theta

		self.input = self.sigmoid(y)
		
		return self.input

	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x)) 

	# DEPRECATED: Use print_weight from Processor
	#def walkTree(self, children):
	#
	#	if not children.prev_neuron is None:
	#		for n in children.prev_neuron:
	#			print("w"+n[1].title+children.title+": "+str(round(n[0], 5)))
	#			self.walkTree(n[1])
	#
	#	if not children.theta is None:
	#		print("Th"+children.title+": "+str(round(children.theta, 5)))
