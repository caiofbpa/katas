require "test/unit"

class WordWrapperTests < Test::Unit::TestCase
  def test_should_return_exact_same_word
    assert_equal("word", WordWrapper::wrap("word", 4))
  end
  
  def test_should_break_word_once
    assert_equal("wo\nrd", WordWrapper::wrap("word", 2))
  end
  
  def test_should_break_word_twice
    assert_equal("tes\ntin\ng", WordWrapper::wrap("testing", 3))
  end
  
  def test_should_break_replacing_space
    assert_equal("word\ntest", WordWrapper::wrap("word test", 4))
  end
  
  def test_should_break_replacing_previous_space
    assert_equal("word\ntest", WordWrapper::wrap("word test", 7))
  end
end

class WordWrapper
  def WordWrapper::wrap(text, max_length)
    wrapper = WordWrapper.new(max_length)
    return wrapper.wrap(text)
  end
  
  def initialize(max_length)
    @max_length = max_length
  end
  
  def wrap(text)
    if(text.length() <= @max_length)
      return text
    end
    if(text[@max_length] == " ")
      return break_line_deleting_last_char_at(text, @max_length)
    elsif(text.index(" "))
      return break_line_deleting_last_char_at(text, text.index(" "))
    else
      return break_line_at(text, @max_length)
    end
  end
  
  def break_line_deleting_last_char_at(text, index)
    return break_line(text, index, 1)
  end
  
  def break_line_at(text, index)
    return break_line(text, index, 0)
  end
  
  def break_line(text, index, gap)
    return text[0..index-1] + "\n" + wrap(text[index+gap..text.length()])
  end
end