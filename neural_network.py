from classes.neuron import Neuron

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



neuron_1 = Neuron("1", 1, None, None);
neuron_2 = Neuron("2", 1, None, None);
neuron_3 = Neuron("3", None, 0.8, [[0.5, neuron_1], [0.4, neuron_2]])
neuron_4 = Neuron("4", None, -0.1, [[0.9, neuron_1], [1.0, neuron_2]])
neuron_5 = Neuron("5", None, 0.3, [[-1.2, neuron_3], [1.1, neuron_4]])

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