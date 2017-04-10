class Solution(object):
  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False

    originalWordCount = {}
    anagramWordCount = {}

    for char in set(s):
      originalWordCount[char] = s.count(char)
    for char in set(t):
      anagramWordCount[char] = t.count(char)

    if originalWordCount == anagramWordCount:
      return True
    else:
      return False
