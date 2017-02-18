# -*- coding: utf-8 -*-

import sys
class Life(object):

    def evolve(self,state):

        # Initialize array of arrays of zeroes of equal dimension to states
        # array for output of novel array.
        state_out = []
        for row in state:
            state_out.append([])
            for cell in row:
                state_out[-1].append(0)

        rrow = 0

        # Iterate through every row of state
        while rrow < len(state):
            ccell = 0

            # Iterate through every cell of every row
            while ccell < len(state[rrow]):
                state_out[rrow][ccell] = self.setCell(state,[rrow,ccell])
                ccell += 1
            rrow += 1

        return state_out

    ##
    # Input state as passed to Life.evolve and current cell (array [x,y]).
    # setCell evaluates neighbours of a cell and returns evolved value
    def setCell(self,state,current):
        neighbours = 0

        # Array defines bounds for neighbouring [rows, cells] to compare
        neighbour_subset = [[current[0] - 1, current[0] + 2],
                            [current[1] - 1, current[1] + 2]]

        # Ensure lower bound isn't negative (slice would go to end of array)
        for axis in neighbour_subset:
            if axis[0] < 0:
                axis[0] = 0

        # Previous upper bound fix gone as for [x:y] slice, y-1 is last val.

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
        # Scenarios 0,4
        else:
            # Scenario 4
            if neighbours == 3:
                return 1
            # Scenario 0
            else:
                return 0
