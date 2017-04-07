class Solution(object):
  def lengthOfLastWord(self, s):
    if not any(word.isalpha() for word in s):
      return 0
    words = s.split()
    print(words)
    lastWord = words[-1]
    if lastWord.isalpha():
      return len(lastWord)
    else:
      return 0
