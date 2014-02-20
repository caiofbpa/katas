import unittest
from BowlingGame import BowlingGame

class BowlingGameTest(unittest.TestCase):
	def setUp(self):
		self.game = BowlingGame()

	def rollMany(self, pins, times):
		for i in xrange(0, times):
			self.game.roll(pins)

	def rollSpare(self):
		self.game.roll(5)
		self.game.roll(5)

	def rollStrike(self):
		self.game.roll(10)

	def test_worstGame(self):
		self.rollMany(0, 20)
		self.assertEqual(0, self.game.get_score())

	def test_onePin(self):
		self.rollMany(1, 20)
		self.assertEqual(20, self.game.get_score())

	def test_spare(self):
		self.rollSpare()
		self.game.roll(2)
		self.rollMany(0, 17)
		self.assertEqual(14, self.game.get_score())

	def test_strike(self):
		self.rollStrike()
		self.game.roll(3)
		self.game.roll(4)
		self.rollMany(0, 17)
		self.assertEqual(24, self.game.get_score())

	def test_double_strike(self):
		self.rollStrike()
		self.rollStrike()
		self.game.roll(4)
		self.game.roll(2)
		self.rollMany(0, 16)
		self.assertEqual(46, self.game.get_score())

	def test_perfect_game(self):
		self.rollMany(10, 12)
		self.assertEqual(300, self.game.get_score())

if __name__ == '__main__':
    unittest.main()