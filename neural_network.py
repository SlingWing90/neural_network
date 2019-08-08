import math
#import plotly.graph_objects as go
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

	#error_gradient = 0
	#weight_correction = []

	def __init__(self, title, input, theta, prev_neuron):
		self.title = title
		self.input = input
		self.theta = theta
		self.prev_neuron = prev_neuron
		self.weight_correction = []
		self.error_gradient = 0

	def print_neuron(self):
		print("This neuron: ")
		
		print("Prev neurons: ")
		print(self.prev_neuron)

	def print_input(self):
		print(str(self.input))

	def update_weight(self, learning_rate, error):
		self.error_gradient= self.input*(1-self.input)*error
		
		self.update_children_weight(learning_rate, self.error_gradient)


	def update_children_weight(self, learning_rate, error_gradient):
		children_error_gradient = 0

		self.weight_correction = []
		for n in self.prev_neuron:
			#print(n[1].title+" "+str(n[1].input))	
			self.weight_correction.append(learning_rate*n[1].input*error_gradient)
			
			children_error_gradient = n[1].input*(1-n[1].input)*error_gradient*n[0]
			
			if n[1].prev_neuron is not None:
				n[1].update_children_weight(learning_rate, children_error_gradient)

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


	def walkTree(self, children):

		if not children.prev_neuron is None:
			for n in children.prev_neuron:
				print("w"+n[1].title+children.title+": "+str(round(n[0], 5)))
				self.walkTree(n[1])

		if not children.theta is None:
			print("Th"+children.title+": "+str(round(children.theta, 5)))


neuron_1 = neuron("1", 1, None, None);
neuron_2 = neuron("2", 1, None, None);
neuron_3 = neuron("3", None, 0.8, [[0.5, neuron_1], [0.4, neuron_2]])
neuron_4 = neuron("4", None, -0.1, [[0.9, neuron_1], [1.0, neuron_2]])
neuron_5 = neuron("5", None, 0.3, [[-1.2, neuron_3], [1.1, neuron_4]])

X = [[0, 0], [1, 0], [0, 1], [1, 1]]
Y = [0, 1, 1, 0]
learning_rate = 0.1

learning_threshold = 0.001
continue_learning = 1

while continue_learning > 0:	
	table_output = []
	#error_array = []
	error_sum = 0
	for x in range(0, len(X)):
		x_1 = X[x][0]
		x_2 = X[x][1]

		y_desired = Y[x]

		neuron_1.input = x_1
		neuron_2.input = x_2

		neuron_3.calc_y()
		neuron_4.calc_y()
		y = neuron_5.calc_y()
		
		error = y_desired - y
		error_sum = error_sum + (error*error)

		row = [x_1, x_2, y_desired, y, error]

		table_output.append(row)

		neuron_5.update_weight(learning_rate, error);

		loading = "";
		for z in range(0, x):
			loading = loading + "."

		print(loading)

	if error_sum < learning_threshold:
		continue_learning = 0

# RESULT		
print("Final Result")	
print("x1   x2   Yd   Youtput   error") 
for r in table_output:
	print(" "+str(r[0])+"    "+str(r[1])+"    "+str(r[2])+"   "+str(round(r[3], 5))+"   "+str(round(r[4], 5))) 

#fig = go.Figure(data=[go.Table(header=dict(values=['x1', 'x2', 'Yd', 'Youtput', 'error']),
#                 cells=dict(values=[[0,1,0,1],[0,0,1,1],[0,1,1,0],y_output,error_output]))
#                     ])
#fig.show()

print(" ")
print("Weights")
neuron_5.walkTree(neuron_5)