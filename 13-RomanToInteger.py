class Solution(object):
    def romanToInt(self, s):
        s = list(s.lower())
        nums = {'i': 1, 'v': 5, 'x': 10,
                'l': 50, 'c': 100, 'd': 500, 'm': 1000 }
        
        total = nums[s[-1]]
        for i in range(0, len(s) - 1):
                if nums[s[i]] < nums[s[i+1]]:
                    total -= nums[s[i]]
                else:
                    total += nums[s[i]]
        return total 

