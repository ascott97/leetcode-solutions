class Solution(object):
  def addDigits(self, num):
    if len(str(num)) == 1:
      return num
    else:
      num = [int(number) for number in str(num)]
      newNum = sum(num)
      return self.addDigits(newNum)
