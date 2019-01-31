import random
import json
import os 
import sys
path_location = os.path.dirname(os.path.realpath(__file__))
sim_paths_location = os.path.join(path_location, '..') 
sys.path.insert(0, sim_paths_location)
import sim_paths

def check_dictionary_comparisons(nodes_dict, transitions_dict):

	# 1428
	check =  {'obstacle2': 0, 'workload': 18, 'obstacle3': 0, 'complete_work_with_robot': 1, 'arriving_at_0': 0, 'r_state': 0, 'workload_add': 0, 'complete_work_at_workstation': 1, 'complete_dropoff_tries': 1, 'next_state_is_workstation': 0, 'complete_dropoff_success': 1, 'wait': 0}

	#3199
	check = {"workload": 20, "obstacle2": 0, "obstacle3": 0, "complete_work_with_robot": 1, "arriving_at_0": 0, "r_state": 3, "workload_add": 0, "complete_work_at_workstation": 1, "complete_dropoff_tries": 0, "next_state_is_workstation": 0, "complete_dropoff_success": 0, "wait": 0}

	# Testing if we can compare dictionaries
	for key, node in nodes_dict.items():
		if nodes_dict[key] == check:
			print "key", key 
			transition_options = transitions_dict[key]
			print "transition_options", transition_options
			print "next node", (random.choice(transition_options))
			

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

	# check_dictionary_comparisons(nodes_dict, transitions_dict)
	test_transitions(nodes_dict, transitions_dict)



if __name__ == '__main__':
	main()
	
