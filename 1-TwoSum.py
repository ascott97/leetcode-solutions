class Solution(object):
  def twosum(self, nums, target):
    loop = True
    answer = []
    for i, item in enumerate(nums):
      for j, item2 in enumerate(nums):
        if (item + item2) == target and i != j:
          print(str(item) + " + " + str(item2) + " = " + str(target))
	  answer.append(i)
          answer.append(j)
          loop = False
        else:
          pass
      if not loop:
        break
    return answer
