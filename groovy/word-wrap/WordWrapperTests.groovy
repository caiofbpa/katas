class WordWrapperTests extends GroovyTestCase {
	void test_shouldReturnExactSameWord(){
		assertEquals("word", WordWrapper.wrap("word", 4))
	}
	
	void test_shouldBreakWordOnce(){
		assertEquals("wo\nrd", WordWrapper.wrap("word", 2))
	}
	
	void test_shouldBreakWordTwice(){
		assertEquals("tes\ntin\ng", WordWrapper.wrap("testing", 3))
	}
	
	void test_shouldBreakReplacingSpace(){
		assertEquals("space\ntest", WordWrapper.wrap("space test", 5))
	}
	
	void test_shouldBreakPreviousSpace(){
		assertEquals("space\ntest", WordWrapper.wrap("space test", 8))
	}
}

class WordWrapper {
	
	Integer maxLength;
	
	public static String wrap(String text, Integer maxLength){
		WordWrapper wrapper = new WordWrapper(maxLength)
		return wrapper.wrap(text)
	}
	
	WordWrapper(Integer maxLength){
		this.maxLength = maxLength
	}
	
	public String wrap(String text){
		if(text.length() <= maxLength)
			return text
		if(text[maxLength] == " ")
			return breakLine(text, maxLength, 1)
		else if(text.indexOf(" ") > 0)
			return breakLine(text, text.indexOf(" "), 1)
		else
			return breakLine(text, maxLength, 0)
	}
	
	private String breakLine(String text, Integer index, Integer gap){
		return text.substring(0, index) + "\n" + wrap(text.substring(index + gap, text.length()))
	}
}