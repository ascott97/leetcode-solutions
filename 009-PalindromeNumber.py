class Solution(object):
    def isPalindrome(self, x):
        x = list(str(x))
        FirstHalf = x[:(len(x)//2)]
        SecondHalf = { True: x[(len(x)//2):], False: x[(len(x)//2 +1):] }[len(x) % 2 == 0]
        SecondHalf.reverse()
        
        if FirstHalf == SecondHalf:
            return True
        else:
            return False
