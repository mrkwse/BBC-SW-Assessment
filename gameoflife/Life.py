# -*- coding: utf-8 -*-

import sys
class Life(object):

	def evolve(self,state):
		# raise NotImplementedError("Please implement the 'evolve' method")


		# Initialize array of arrays of zeroes of equal dimension to states
		# array.

		state_out = []

		for row in state:
			state_out.append([])
			for cell in row:
				state_out[-1].append(0)

		y = 0

		# Iterate through every row of state
		while y < len(state):
			x = 0

			# Iterate through every cell of every row
			while x < len(state):
				state_out[y][x] = self.setCell(state,[y,x])
				x += 1
			y += 1

		return state_out

	##
	# Input state as passed to Life.evolve and current cell (array [x,y]).
	# FIXME: Could also input explicit value of current cell rather than
	# implicit via state[current[0]][current[1]].
	def setCell(self,state,current):
		neighbours = 0

		# if (current[0] == (0 or len(state)) and (current[1] == (0 or len(state[0])))):
		# 	to_check = 3
		# elif (current[0] == (0 or len(state)) ^ (current[1] == (0 or len(state[0])))):
		# 	to_check = 5
		# else:
		# 	to_check = 8
		neighbour_subset = [[current[0] - 1, current[0] + 2],
						    [current[1] - 1, current[1] + 2]]

		# Ensure lower bound isn't negative (slice would go to end of array)
		for axis in neighbour_subset:
			if axis[0] < 0:
				axis[0] = 0

		if neighbour_subset[0][1] > (len(state)):
			neighbour_subset[0][1] = (len(state))

		if neighbour_subset[1][1] > (len(state[0])):
			neighbour_subset[1][1] = (len(state[0]))

		# Iterate through every neighbouring row
		for row in state[neighbour_subset[0][0]:neighbour_subset[0][1]]:
			# Iterate through every neighbouring cell of a row
			for cell in row[neighbour_subset[1][0]:neighbour_subset[1][1]]:

				# If cell == 1, note as an additional neighbour
				if cell == 1:
					neighbours += 1

		# Iteration counts current cell, so subject to account for this
		# if necessary
		if state[current[0]][current[1]] == 1:
			neighbours -= 1


		# Return evolved state as defined by scenarios

		# Scenarios 1:3
		if state[current[0]][current[1]] == 1:
			# Scenario 1,2
			if neighbours < 2 or neighbours > 3:
				return 0
			# Scenario 3
			else:
				return 1
		# Scenarios 0,4,5
		else:
			# Scenario 4
			if neighbours == 3:
				return 1
			# Scenario 0,5
			else:
				return 0
