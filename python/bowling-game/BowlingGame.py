class BowlingGame(object):
	def __init__(self):
		self.rolls = [0] * 21
		self.score = 0
		self.frameIndex = 0
		self.currentRoll = 0

	def roll(self, pins):
		self.rolls[self.currentRoll] = pins
		self.currentRoll += 1

	def is_spare(self):
		return self.rolls[self.frameIndex] + self.rolls[self.frameIndex + 1] == 10

	def spare_bonus(self):
		return self.rolls[self.frameIndex + 2]

	def is_strike(self):
		return self.rolls[self.frameIndex] == 10

	def strike_bonus(self):
		return self.rolls[self.frameIndex + 1] + self.rolls[self.frameIndex + 2]

	def get_score(self):
		for frame in xrange(0,10):
			if(self.is_strike()):
				self.score += 10 + self.strike_bonus()
				self.frameIndex += 1
			elif(self.is_spare()):
				self.score += 10 + self.spare_bonus()
				self.frameIndex += 2;
			else:
				self.score += self.rolls[self.frameIndex] + self.rolls[self.frameIndex + 1]
				self.frameIndex += 2;
		return self.score