import plotly.graph_objects as go
import networkx as nx

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
			
	def _get_prev_neuron(self, neur, posX, posY):
		x = posX - 1
		y = 0
		pos_array = []
		result_array = []
		for pre_ne in neur.prev_neuron:
			#print(neur.title +" " + pre_ne[1].title)
			if pre_ne[1].prev_neuron is not None:
				#print(neur.title +" " + pre_ne[1].title)
				#print("X: "+str(x) + " - Y: "+str(y));
				pos_array.append([x, y, neur.title + pre_ne[1].title])
				y = y + 1
				#result_array.append([x, y])
				pos_array = pos_array + self._get_prev_neuron(pre_ne[1], x, y)
			else: 
				#print(neur.title +" " + pre_ne[1].title)
				#print("X: "+str(x) + " - Y: "+str(y))
				pos_array.append([x, y, neur.title + pre_ne[1].title])
				y = y + 1
				
		return pos_array
				
				
			
	def print_graph(self):
		G = nx.random_geometric_graph(200, 0.125)
		
		x_pos = len(self.network) #5 Testwise
		y_pos = 0
		nodes = []
		for x in range(len(self.network) - len(self.y_table[0]), len(self.network)):
			pre_ne = self.network[x].prev_neuron
			nodes.append([x_pos, y_pos, self.network[x].title])
			prev_nodes = self._get_prev_neuron(self.network[x], x_pos, y_pos)
			nodes = nodes + prev_nodes
			y_pos = y_pos + 1
		
		node_x = []
		node_y = []
		for n in nodes:
			node_x.append(n[0])
			node_y.append(n[1])
				
		edge_x = []
		edge_y = []
		x0 = 0
		y0 = 0
		x1 = 0
		y1 = 0
		
		print(nodes)
		for n in nodes:
			x0 = n[0]
			y0 = n[1]
			act_node = n[2]
			if len(act_node) > 1:
				act_node = n[2][1]
			#print(act_node)	
			for ne in nodes:
				if len(ne[2]) > 1 and ne[2][0] == act_node:
					x1 = ne[0]
					y1 = ne[1]
					
					edge_x.append(x0)
					edge_x.append(x1)
					edge_x.append(None)
					edge_y.append(y0)
					edge_y.append(y1)
					edge_y.append(None)
					
		edge_trace = go.Scatter(
			x=edge_x, y=edge_y,
			line=dict(width=0.5, color='#888'),
			hoverinfo='none',
			mode='lines')

		node_trace = go.Scatter(
			x=node_x, y=node_y,
			mode='markers',
			#hoverinfo='text',
			marker=dict(
				showscale=False,
				# colorscale options
				#'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
				#'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
				#'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
				colorscale='YlGnBu',
				reversescale=False,
				color=[],
				size=10,
				colorbar=dict(
					thickness=15,
					title='Node Connections',
					xanchor='left',
					titleside='right'
				),
				line_width=2))
		
		#node_adjacencies = []
		node_adjacencies = (0, {1})
		
		fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    #text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
		fig.show()