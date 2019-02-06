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

	# check = {'workload':14, 'obstacle2': 0, 'obstacle3': 0, 'workload_stays_constant': 0, 'complete_work_with_robot': 0, 'arriving_at_0': 0, 'r_state': 2, 'workload_add': 0, 'complete_work_at_workstation': 1, 'complete_dropoff_tries': 0, 'next_state_is_workstation': 0, 'complete_dropoff_success': 0, 'wait': 0}

	# node_num 10322
	check = {'workload':21, 'obstacle2': 0, 'obstacle3': 0, 'workload_stays_constant': 1, 'complete_work_with_robot': 1, 'arriving_at_0': 1, 'r_state': 2, 'workload_add': 0, 'complete_work_at_workstation': 1, 'complete_dropoff_tries': 0, 'next_state_is_workstation': 0, 'complete_dropoff_success': 0, 'wait': 0}
	

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

	key_options = nodes_dict.keys()
	

	key = str(random.choice(key_options))

	for i in range(0, test_steps):
		print "key", key
		r_state = nodes_dict[key]['r_state']
		print "r_state:", r_state

		transition_options = transitions_dict[key]
		print "transition options:", transition_options
		key = str((random.choice(transition_options)))

	return 



def test_commands(nodes_dict, transitions_dict):


	test_steps = 500

	key_options = nodes_dict.keys()
	node_num = str(random.choice(key_options)) #'15230'  


	commands = ['r_state', 'workload_add', 'next_state_is_workstation', 'complete_work_with_robot', 'arriving_at_0']
	# environment = ['wait', 'obstacle2', 'obstacle3', 'workload', 'complete_work_at_workstation', 'complete_dropoff_success', 'complete_dropoff_tries', 'workload_stays_constant']
	environment = ['wait', 'obstacle2', 'workload', 'complete_work_at_workstation', 'complete_dropoff_success', 'complete_dropoff_tries', 'workload_stays_constant']



	for i in range(0, test_steps):

		current_node_states = nodes_dict[node_num]
		print "current state"
		print "node_num", node_num
		for key, val in nodes_dict[node_num].items():
			print key, val 

		transition_options = [str(i) for i in transitions_dict[node_num]]
		print "transition options", transition_options, "\n"


		node_num = (random.choice(transition_options))

		next_states = {}
		for key, val in nodes_dict[node_num].items():
			next_states[key] = val

		# print "next_states"
		# for key, val in next_states.items():
		# 	print key, val 

		environment_states = {}
		for states in environment:
			environment_states[states] = next_states[states]


		# testing if we don't get a match
		# if (current_node_states['obstacle2'] == 0 and current_node_states['obstacle3'] == 0) and all(nodes_dict[node]['obstacle2']== 0 and nodes_dict[node]['obstacle3'] == 0  for node in transition_options):
		

		if (current_node_states['obstacle2'] == 0) and all(nodes_dict[node]['obstacle2']== 0 for node in transition_options):
			r = random.choice([0, 1])
			# if all(nodes_dict[key]['r_state'] == 2 for key in transition_options):
			#  	environment_states['obstacle3'] = r
			#  	next_states['obstacle3'] = r
			if all(nodes_dict[key]['r_state'] == 3 for key in transition_options):
			 	environment_states['obstacle2'] = r
			 	next_states['obstacle2'] = r

			# print "TEST"
			# print node_num
			# exit()
			

		print "next_states"
		for key, val in next_states.items():
			print key, val 
		print "\n"

		success = False 
		while success == False: 

			for node_options in transition_options:
				print "node", node_options 
				print "r_state", nodes_dict[node_options]['r_state']
					
				for key in environment:
					
					print key, nodes_dict[node_options][key]
				if all(nodes_dict[node_options][key] == environment_states[key] for key in environment):
					node_num = node_options
					print "SELECTED OPTION", node_num
					success = True 
				print "\n"

			match = False  
			if success == False: 
				for key, node in nodes_dict.items():
					if nodes_dict[key] == next_states:
						print "NO MATCH"
												
						print "selected key", key 

						node_num = key 


						success = True 

						match = True 

					if match == True:
						break 


		robot_commands = {}
		for c in commands:
			robot_commands[c] = nodes_dict[node_num][c]


		# print "robot_commands", robot_commands
		

		


		
		# # update node_num to where robot is expected to go
		# node_num = random.choice(transition_options)	

	exit()

def main():

	node_file = os.path.join(path_location, 'node_dictionary.json')
	transition_file = os.path.join(path_location, 'transition_dictionary.json')

	with open(node_file, 'r') as f:
	    nodes_dict = json.load(f)

	with open(transition_file, 'r') as f:
	    transitions_dict = json.load(f)

	# check_dictionary_comparisons(nodes_dict, transitions_dict)
	# test_transitions(nodes_dict, transitions_dict)
	# test_deviations(nodes_dict, transitions_dict)
	test_commands(nodes_dict, transitions_dict)


if __name__ == '__main__':
	main()
	



# def test_deviations(nodes_dict, transitions_dict):

# 	random_binary = [0,1]
# 	random_2 = [1,2]
# 	random_3 = [0,1,2]

# 	obstacle_dict = {2: 'obstacle2', 3: 'obstacle3'}

# 	test_steps = 100
# 	node_num = '0'

# 	current_state = nodes_dict[node_num]


# 	for i in range(0, test_steps):

# 		print "test num", i , "\n"

# 		print "current_state", current_state, "\n"

# 		# transition options from where I am currenlty
# 		transition_options = transitions_dict[node_num]

# 		print "transition options", transition_options, "\n"
		
# 		# update node_num to where robot is expected to go
# 		node_num = random.choice(transition_options)

# 		print "node num", node_num, "\n"

# 		# next expected states
# 		next_expected = nodes_dict[str(node_num)]

# 		print "next_expected", next_expected, "\n"

# 		# initialize next actual states, which will be updated
# 		next_actual = {}
# 		for key, val in next_expected.items():
# 			next_actual[key] = val 

# 		# update actual state randomly 

# 		# workload state and 'workload_stays_constant'
# 		if next_expected['r_state'] != 4: 
# 			if current_state['workload_stays_constant']:
# 				next_actual['workload'] = current_state['workload'] - random.choice(random_2)
# 				next_actual['workload_stays_constant'] = 0
# 			else: 
# 				next_actual['workload'] = current_state['workload'] - random.choice(random_3)
# 				if next_actual['workload'] == current_state['workload']: 
# 					next_actual['workload_stays_constant'] = 1
# 				else: 
# 					next_actual['workload_stays_constant'] = 0
# 		else:
# 			# workload, workload add, and workload_stays_constant are already configured by dictionary if the robot is in state 4 
# 			continue 




# 		# waiting state
# 		if next_actual['workload'] > 0 or next_actual['r_state'] == 4:
# 			next_actual['wait'] = 0 
# 		else: 
# 			next_actual['wait'] = 1

# 		# obstacles
# 		for pos_o, obstacle in obstacle_dict.items(): 

# 			if next_actual['r_state'] == pos_o:
# 					next_actual[obstacle] = 0 
# 			else: 
# 				if current_state[obstacle] == 0:
# 					next_actual[obstacle] = random.choice(random_binary)
# 				else: 
# 					next_actual[obstacle] = 0

# 		print "next_actual", next_actual
		
# 		success = False 

# 		# update where we actual are
# 		for key, node in nodes_dict.items():

# 			if nodes_dict[key] == next_actual:


# 				print "selected key", key 
				
# 				node_num = key
				
# 				success = True
				 
# 		if success == False:
# 			"unsuccessful"
# 			exit()
# 	exit()

# 	return 