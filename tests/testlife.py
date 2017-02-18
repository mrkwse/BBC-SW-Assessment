from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):
	def test_no_interaction(self):
		emptyState = [  [0,0,0],
				[0,0,0],
				[0,0,0]  ]
		testLife = Life()
		self.assertEqual(emptyState, testLife.evolve(emptyState))

	def test_underpopulation(self):
		startState = [ [1,0,0],
					   [0,0,0],
					   [0,0,1] ]

		endState =   [ [0,0,0],
					   [0,0,0],
					   [0,0,0] ]

		testLife = Life()
		self.assertEqual(endState, testLife.evolve(startState))

	def test_overcrowding(self):
		startState = [ [1,1,1],
		 			   [1,1,1],
					   [1,1,1] ]

		endState =   [ [1,0,1],
					   [0,0,0],
					   [1,0,1] ]

		testLife = Life()
		self.assertEqual(endState, testLife.evolve(startState))

	def test_survival(self):
		startState = [ [0,1,0],
					   [1,0,1],
					   [0,1,0] ]

		endState =   [ [0,1,0],
					   [1,0,1],
					   [0,1,0] ]

		testLife = Life()
		self.assertEqual(endState, testLife.evolve(startState))

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
