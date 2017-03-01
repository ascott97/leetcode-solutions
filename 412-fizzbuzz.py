class Solution(object):
    def fizzBuzz(self, n):
        List = []
        for i in range(1,n+1):
            if i % 15 == 0:
                List.append("FizzBuzz")
            elif i % 5 == 0:
                List.append("Buzz")
            elif i % 3 == 0:
                List.append("Fizz")
            else:
                List.append(str(i))
        return List
