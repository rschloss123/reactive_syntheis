import json 
import random 
import os

def clean(js):
	"""Eliminate all terminal nodes and return."""

	while True:

		# accumulate list of terminal nodes and remove them from `js`
		terminal_nodes = []
		num_nodes = len(js['nodes'])



		print "here 1"

		for key, node in js['nodes'].items():
			if not node['trans']:
				terminal_nodes.append(int(key))

		print "here 2"

		# remove references to terminal nodes
		for key, node in js['nodes'].items():
			node['trans'] = [t for t in node['trans'] if t not in terminal_nodes]

		print "here 3"

		for t in terminal_nodes:
			del js['nodes'][str(t)]

		
		if not terminal_nodes:
			return js

def variables_to_base10(node, name_and_bits):

	state_binary = node['state']
	count = 0 

	list_local = []
	variable_dictionary = {}


	for j in name_and_bits:

		# j is equal to a dictionary
		name = j['name']
		bits = j['bits']

		# create array slice from an array of numbers
		bin_string = state_binary[count:count+bits] # grab the section 
		bin_string = bin_string[::-1] # reverse the section
		# make an array of strings 
		bin_string = [str(str_var) for str_var in bin_string] 
		# make into string
		bin_string = ''.join(bin_string)

		val_base_10 = int(bin_string,2)

		print name+":", val_base_10
		 

		list_local.append(val_base_10)
		
		variable_dictionary[name] = val_base_10
		transitions = node['trans']
		count+=bits 



	return list_local, variable_dictionary, transitions	




class Controller():

	def __init__(self, name_and_bits, file_name):
		# 'with' is context block
		# 'r' is read mode
		# 'open' is a file handle and is being stored as f 
		with open(file_name, 'r') as f :
			self.file_content = json.load(f)
			self.file_content = clean(self.file_content)

		self.num_nodes = len(self.file_content['nodes'])
		self.name_and_bits = name_and_bits



	def simulate(self, node_init, num_steps):

		node_num = node_init

		var_list = []


		for i in range (0, num_steps):
			node = self.file_content['nodes'][node_num] 
			print " "
			print "Node #", node_num

			list_local, _, _ = variables_to_base10(node, self.name_and_bits)

			var_list.append(list_local)	
			transition_options =  node['trans']

			not_empty = 0
			
			node_num = str(random.choice(transition_options))
			while not_empty == 0:
				next_node = self.file_content['nodes'][node_num] 
				if next_node['trans'] == []:
					node_num = str(random.choice(transition_options))
				else:
					not_empty = 1

		
		# var_list is for simulation
		return var_list

	def json_to_dictionary(self):

		node_dictionary = {}
		transition_dictionary = {}

		for key, node in self.file_content['nodes'].items():
			_, dictionary_local, transition_local = variables_to_base10(node, self.name_and_bits)

			node_dictionary[str(key)] = dictionary_local
			transition_dictionary[str(key)] = transition_local

		return (node_dictionary, transition_dictionary)

	def save_dictionary_as_json(self, dictionary, filename):
		with open(filename, 'w') as f:
			json.dump(dictionary, f)



def get_lookup():

	lookup = [
		{'name': 'wait', 'bits': 1},
		{'name': 'obstacle2', 'bits': 1},
		{'name': 'obstacle3', 'bits': 1},
		{'name': 'workload', 'bits': 5},
		{'name': 'complete_work_at_workstation', 'bits': 1},
		{'name': 'complete_dropoff_success', 'bits': 1},
		{'name': 'complete_dropoff_tries', 'bits': 2},
		{'name': 'workload_stays_constant', 'bits': 1},
		{'name': 'r_state', 'bits': 3},
		{'name': 'workload_add', 'bits': 4},
		{'name': 'next_state_is_workstation', 'bits': 1},
		{'name': 'complete_work_with_robot', 'bits': 1},
		{'name': 'arriving_at_0', 'bits': 1},
		{'name': 'arriving_at_2', 'bits': 1},
		{'name': 'arriving_at_3', 'bits': 1},

	]

	# lookup = [
	# 	{'name': 'obstacle2', 'bits': 1},
	# 	# {'name': 'obstacle3', 'bits': 1},
	# 	{'name': 'r_state', 'bits': 3},
	# ]

	return lookup


def main(): 
	


	path_location = os.path.dirname(os.path.realpath(__file__))
	delivery_file = os.path.join(path_location, 'hri_reactive_synthesis', 'ctrl.json')
	
	delivery_lookup = get_lookup()

	delivery_sim = Controller(delivery_lookup, delivery_file)
	node_init = '0'
	# var_list = delivery_sim.simulate(node_init, 50)
	
	(node_dictionary, transition_dictionary) = delivery_sim.json_to_dictionary()

	node_file = os.path.join(path_location, 'hri_reactive_synthesis', 'node_dictionary.json')
	transition_file = os.path.join(path_location, 'hri_reactive_synthesis', 'transition_dictionary.json')
	delivery_sim.save_dictionary_as_json(node_dictionary, node_file)
	delivery_sim.save_dictionary_as_json(transition_dictionary, transition_file)



	

if __name__ == '__main__':
	main()


