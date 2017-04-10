class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    if len(nums) != len(set(nums)):
      return True 
    return False
