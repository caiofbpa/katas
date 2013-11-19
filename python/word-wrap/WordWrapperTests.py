import unittest

class WordWrapperTest(unittest.TestCase):
	def test_should_return_same_exact_text(self):
		self.assertEqual("Test", WordWrapper.wrapText("Test", 4))
	
	def test_should_break_word(self):
		self.assertEqual("Te\nst", WordWrapper.wrapText("Test", 2))
	
	def test_should_break_word_twice(self):
		self.assertEqual("Tes\ntin\ng", WordWrapper.wrapText("Testing", 3))
	
	def test_should_replace_space(self):
		self.assertEqual("Test\ntest", WordWrapper.wrapText("Test test", 4))
	
	def test_should_replace_previous_space(self):
		self.assertEqual("Test\ntest", WordWrapper.wrapText("Test test", 7))

class WordWrapper:
	@staticmethod
	def wrapText(text, maxLength):
		wrapper = WordWrapper(maxLength)
		return wrapper.wrap(text)
	
	def __init__(self, maxLength):
		self.maxLength = maxLength
	
	def wrap(self, text):
		if(len(text) <= self.maxLength):
			return text
		if(text[self.maxLength] == " "):
			return self.break_line(text, self.maxLength, 1)
		elif(text.find(" ") > 0):
			return self.break_line(text, text.find(" "), 1)
		else:
			return self.break_line(text, self.maxLength, 0)
	
	def break_line(self, text, index, gap):
		return text[0 : index] + "\n" + self.wrap(text[index + gap : len(text)])

if __name__ == '__main__':
	unittest.main()