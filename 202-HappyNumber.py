class Solution(object):
  def isHappy(self, n):
    tested = []
    while n != 1:
      n = sum([int(number) ** 2 for number in str(n)])
      if n in tested:
        return False
      else:
        tested.append(n)
    else:
      return True
