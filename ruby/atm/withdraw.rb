class Withdraw
  def execute(amount)
    result = {}
    bills = [10, 5, 2, 1]
    for bill in bills
      while(amount >= bill)
        result[bill] = result[bill].to_i + 1
        amount -= bill
      end
    end
    return result
  end
end