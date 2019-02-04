import random
import json
import os 
import sys
path_location = os.path.dirname(os.path.realpath(__file__))
sim_paths_location = os.path.join(path_location, '..') 
sys.path.insert(0, sim_paths_location)
import sim_paths

def check_dictionary_comparisons(nodes_dict, transitions_dict):


	num_nodes = len(nodes_dict)
	
	key_options = nodes_dict.keys()
	

	key_random = str(random.choice(key_options))


	check = nodes_dict[key_random]

	check = {'workload':15, 'obstacle2': 0, 'obstacle3': 0, 'workload_stays_constant': 1, 'complete_work_with_robot': 0, 'arriving_at_0': 0, 'r_state': 2, 'workload_add': 0, 'complete_work_at_workstation': 1, 'complete_dropoff_tries': 0, 'next_state_is_workstation': 0, 'complete_dropoff_success': 0, 'wait': 0}
	# print "random key", key_random

	# Testing if we can compare dictionaries
	for key, node in nodes_dict.items():

		if nodes_dict[key] == check:

			print "selected key", key 
			transition_options = transitions_dict[key]
			print "transition_options", transition_options
			next_node = random.choice(transition_options)
			print "next node", (next_node)
			
			print nodes_dict[key]['r_state']

	return

def test_transitions(nodes_dict, transitions_dict):

	test_steps = 5
	key = '0'

	for i in range(0, test_steps):
		print "key", key
		r_state = nodes_dict[key]['r_state']
		print "r_state:", r_state

		transition_options = transitions_dict[key]
		print "transition options:", transition_options
		key = str((random.choice(transition_options)))

	return 


def main():

	node_file = os.path.join(path_location, 'node_dictionary.json')
	transition_file = os.path.join(path_location, 'transition_dictionary.json')

	with open(node_file, 'r') as f:
	    nodes_dict = json.load(f)

	with open(transition_file, 'r') as f:
	    transitions_dict = json.load(f)

	check_dictionary_comparisons(nodes_dict, transitions_dict)
	# test_transitions(nodes_dict, transitions_dict)



if __name__ == '__main__':
	main()
	
