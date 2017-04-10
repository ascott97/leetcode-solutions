import sys
class Solution(object):
  def reverseWords(self, s):
    newString = []
    s = s.split()
    print(list(newString))
    for word in s:
      newString.append(word[::-1])
    newString = ' '.join(newString)
    return newString


a = Solution()

print(a.reverseWords("let's take leetcode contect"))
