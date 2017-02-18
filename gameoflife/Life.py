# -*- coding: utf-8 -*-

import sys
class Life(object):

	def evolve(self,state):
		# raise NotImplementedError("Please implement the 'evolve' method")

		state_out = state[:]

		y = 0
		x = 0

		while y < len(state):
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

		if (current[0] == (0 or len(state)) and (current[1] == (0 or len(state[0])))):
			to_check = 3
		elif (current[0] == (0 or len(state)) ^ (current[1] == (0 or len(state[0])))):
			to_check = 5
		else:
			to_check = 8
		neighbour_subset = [[current[0] - 1, current[0] + 1],
						    [current[1] - 1, current[1] + 1]]

		# Ensure lower bound isn't negative (slice would go to end of array)
		for axis in neighbour_subset:
			if axis[0] < 0:
				axis[0] = 0

		if neighbour_subset[0][1] > (len(state) - 1):
			neighbour_subset[0][1] = (len(state) - 1)

		if neighbour_subset[1][1] > (len(state[0]) - 1):
			neighbour_subset[1][1] = (len(state[0]) - 1)

		for row in state[neighbour_subset[0][0]:neighbour_subset[0][1]]:
			for cell in row[neighbour_subset[1][0]:neighbour_subset[1][1]]:
				if cell == 1:
					neighbours += 1

		if state[current[0]][current[1]] == 1:
			neighbours -= 1

		if state[current[0]][current[1]] == 1:
			if neighbours < 2 or neighbours > 3:
				return 0
		else:
			if neighbours == 3:
				return 1
