class Processor:
	def __init__(self, network, x_table, y_table, learning_rate = 0.1, learning_threshold = 0.001):
		#print("initialize")
		self.network = network
		self.x_table = x_table
		self.y_table = y_table
		self.learning_rate = learning_rate
		self.learning_threshold = learning_threshold
		self.table_output = []

	def learn(self, print_error = 0):
		continue_learning = 1
		learning_threshold = self.learning_threshold

		while continue_learning > 0:	

			self.table_output = []
			#row = []

			error_sum = 0
				
			for x in range(0, len(self.x_table)):
				#for y_t in range(0, len(self.y_table[x])):
				for y_t in range(len(self.y_table[x]), 0, -1):
			
					row = []
					y_desired = self.y_table[x][y_t-1]

					for v in range(0, len(self.x_table[x])):
						self.network[v].input = self.x_table[x][v] 
						row.append(self.x_table[x][v])
					
					row.append(y_desired)

					y = 0
					for v in range(len(self.x_table[x]), len(self.network)):
						#print("V: "+str(v))
						y = self.network[v].calc_y();
					
					# Get last Y of this neuron
					y = self.network[len(self.network) - y_t].calc_y();
					#################
					row.append(y)

					error = y_desired - y
					error_sum = error_sum + (error*error)
					
					row.append(error)
					# - y_t
					#print("Y_T: "+str(y_t))
					#self.network[len(self.network)-1].update_weight(self.learning_rate, error); original
					#print(str(len(self.network)-(y_t)))
					self.network[len(self.network)-(y_t)].update_weight(self.learning_rate, error)

					self.table_output.append(row)
			
			if print_error == 1:
				print(str(error_sum))

			if error_sum < learning_threshold:
				continue_learning = 0

		return self.network

	def print_result(self):	

		x_output = ""
		for v in range(0, len(self.x_table[0])):
			x_output = x_output + "x"+str(v)+"   "

		print(x_output+"Yd   Youtput   error") 
		for r in self.table_output:
			print(" "+str(r[0])+"    "+str(r[1])+"    "+str(r[2])+"   "+str(round(r[3], 5))+"   "+str(round(r[4], 5))) 

	def process(self, x_input):
		for v in range(0, len(x_input)):
			self.network[v].input = x_input[v] 
			
		#print(str(len(self.y_table[0])))
		y = 0
		for v in range(len(x_input), len(self.network)):
			#print(str(v))
			y = self.network[v].calc_y();
		
		#
		y_val = []
		#for v in range(len(self.network) - len(self.y_table[0]), len(self.network)):
		for v in range(len(self.network)-1, len(self.network) - len(self.y_table[0])-1, -1):
			#print(str(v))
			y = self.network[v].calc_y();
			y_val.append(y)
		
		#print(y_val)
		return y_val #round(y, 0)

	def print_weight(self, children):
		if not children.prev_neuron is None:
			for n in children.prev_neuron:
				print("w"+n[1].title+children.title+": "+str(round(n[0], 5)))
				self.print_weight(n[1])

		if not children.theta is None:
			print("Th"+children.title+": "+str(round(children.theta, 5)))