class Solution(object):
  def isPowerOfTwo(self, n):
    while n > 1:
      if n % 2 != 0:
        return False
      n /= 2
    return True

