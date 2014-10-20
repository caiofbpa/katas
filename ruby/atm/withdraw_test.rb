require "minitest/autorun"
require_relative "withdraw"

class WithdrawTest < MiniTest::Test
  def setup
    @withdraw = Withdraw.new
  end
  
  def test_one
    assert_equal({1 => 1}, @withdraw.execute(1))
  end
  
  def test_two
    assert_equal({2 => 1}, @withdraw.execute(2))
  end
  
  def test_three
    assert_equal({2 => 1, 1 => 1}, @withdraw.execute(3))
  end
  
  def test_four
    assert_equal({2 => 2}, @withdraw.execute(4))
  end
  
  def test_five
    assert_equal({5 => 1}, @withdraw.execute(5))
  end
  
  def test_six
    assert_equal({5 => 1, 1 => 1}, @withdraw.execute(6))
  end
  
  def test_seven
    assert_equal({5 => 1, 2 => 1}, @withdraw.execute(7))
  end
  
  def test_ten
    assert_equal({10 => 1}, @withdraw.execute(10))
  end
end