from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):
    # Scenario 0,5
    def test_no_interaction(self):
        emptyState = [  [0,0,0],
                        [0,0,0],
                        [0,0,0]  ]
        testLife = Life()
        self.assertEqual(emptyState, testLife.evolve(emptyState))

    # Scenario 1
    def test_underpopulation(self):
        startState = [ [1,0,0],
                       [0,0,0],
                       [0,0,1] ]

        endState =   [ [0,0,0],
                       [0,0,0],
                       [0,0,0] ]

        testLife = Life()
        self.assertEqual(endState, testLife.evolve(startState))

    # Scenario 2
    def test_overcrowding(self):
        startState = [ [1,1,1],
                       [1,1,1],
                       [1,1,1] ]

        endState =   [ [1,0,1],
                       [0,0,0],
                       [1,0,1] ]

        testLife = Life()
        self.assertEqual(endState, testLife.evolve(startState))

    # Scenario 3
    def test_survival(self):
        startState = [ [0,1,0],
                       [1,0,1],
                       [0,1,1] ]

        endState =   [ [0,1,0],
                       [1,0,1],
                       [0,1,1] ]

        testLife = Life()
        self.assertEqual(endState, testLife.evolve(startState))

    # Scenario 4
    def test_creation(self):
        startState = [ [0,1,0],
                       [1,1,1],
                       [0,1,0] ]

        endState =   [ [1,1,1],
                       [1,0,1],
                       [1,1,1] ]

        testLife = Life()
        self.assertEqual(endState, testLife.evolve(startState))

    # Scenario 6 & larger 2D arrays
    def test_seeded_outcome(self):
        startState = [ [0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,1,1,1,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0] ]

        nextState =  [ [0,0,0,0,0],
                       [0,0,1,0,0],
                       [0,0,1,0,0],
                       [0,0,1,0,0],
                       [0,0,0,0,0] ]

        testLife = Life()
        self.assertEqual(nextState, testLife.evolve(startState))
        self.assertEqual(startState, testLife.evolve(nextState))

    def test_non_square(self):
        startState = [ [0,0,0,0,0],
                       [0,1,1,1,0],
                       [0,0,0,0,0] ]

        nextState =  [ [0,0,1,0,0],
                       [0,0,1,0,0],
                       [0,0,1,0,0]]

        testLife = Life()
        self.assertEqual(nextState, testLife.evolve(startState))
    	self.assertEqual(startState, testLife.evolve(nextState))
