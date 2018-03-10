import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        most = collections.Counter(nums).most_common()[:k]
        return [x[0] for x in most] 
