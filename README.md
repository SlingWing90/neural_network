# neural_network
Creates a corrected Neural-Network with corrected weights.
Calculates Y-output, error and corrected weights in a neural network. 

## Getting Started
1. This package needs classes "neuron.py" and "processor.py" for calculation.

2. To build a network, class "neuron.py" is needed.
	```
	Syntax:
	neuron(title, theta, prev_neuron)

	Example:
	neuron("Neuron_3", 0.8, [[0.5, neuron_1], [-0.7, neuron_2]])

	Parameters:
	title: string 
	Title for this neuron to display in Weight-Results

	theta: float or NONE
	Theta value

	prev_neuron: array of neurons or NONE
	Contains an array with weight and neuron. 
	Syntax: prev_neuron = [[weight, neuron], [weight, neuron]] 
	Example: prev_neuron = [[0.5, neuron_1], [-0.7, neuron_2]]
	```


2. Build a network like above and append them in ascending order into an array
	```
	neuronal_network = []
	neuronal_network.append(neuron_1)
	neuronal_network.append(neuron_2)
	neuronal_network.append(neuron_3)
	``` 

3. Next create an instance of class "processor.py" and add your neuronal_network-array as first parameter:
	```
	Syntax: 
	processor(network, x_table, y_table, learning_rate = 0.1, learning_threshold = 0.001)

	Example: 
	processor(network, x_table, y_table, learning_rate = 0.1, learning_threshold = 0.001)

	Parameters:
	network: array of neurons
	See "neuronal_network" in above example

	x_table: array
	Truth-Table with Input-Values
	Example:
	Table-Style 
	X1 I X2
	-------
	 0 I  0
	 1 I  0
	 0 I  1
	 1 I  1
	 Array-Style
	 X = [[0, 0], [1, 0], [0, 1], [1, 1]]

	 y_table: array
	 Truth-Tables with desired Output-Values. Needs to have thesame count of rows like x_table
	 Example:
	 Table-Style
	 Y
	 -
	 0
	 1
	 1
	 0
	 Array-Style
	 Y = [0, 1, 1, 0]

	learning_rate: float - Default: 0.1

	learning_threshold: float - Default: 0.001
	```


4. Activate the learning with:
	```
	processor.learn( error_output = 0 )

	Parameter:
	error_output: Integer( 0 or 1 ) Default 0. 
	Prints out error-value for each iteration

	Returns: array of network with updated weights 
	```


5. Print out weight with:
	```
	processor.print_weight( last_neuron )

	Parameter: 
	last_neuron: Neuron
	Last neuron added
	```


6. Print out result (after learn())
	```
	processor.print_result()
	```

## Example
A full Example can be found in "neural_network.py" which solves a XOR-Problem

## Prerequisites
Python 2.7.15+

## Built With
Python 2.7.15+

## Authors
- Brandon Höltgen

## License
This project is licensed under the MIT License - see the LICENSE file for details