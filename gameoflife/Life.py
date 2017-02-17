import sys
class Life(object):

	def evolve(self,state):
		raise NotImplementedError("Please implement the 'evolve' method")

	##
	# Input state as passed to Life.evolve and current cell (array [x,y]).
	# FIXME: Could also input explicit value of current cell rather than
	# implicit via state[current[0]][current[1]].
	def setCell(self,state,current):
		neighbours = 0

		if (current[0] == (0 or len(state)) and (current[1] == (0 or len(state[0])))):
			to_check = 3
		else if (current[0] == (0 or len(state)) ^ (current[1] == (0 or len(state[0])))):
			to_check = 5
		else:
			to_check = 8
		cell_to_check = [(current[0] - 1), (current[1] - 1)]
		cells_checked = 0
		while cells_checked < to_check:

			# If starting cell to
			if cell_to_check[0] < 0:
				cell_to_check[0] = 1
			if cell_to_check[1] < 0:
				cell_to_check[1] = 1

			if cell_to_check != current:
				if state[cell_to_check[0]][cell_to_check[1]] == 1:
					neighbours += 1

			cell_to_check = cell_to_check[1] += 1
			cell_to_check[0] += 1
			cell_to_check[1] = 0

		if state[current[0]][current[1]] == 1:
			if neighbours < 2 or neighbours > 3:
				state[current[0]][current[1]] = 0
		else:
			if neighbours == 3:
				state[current[0]][current[1]] = 1
