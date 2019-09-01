class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nex = 0
        ret = 0
        for i, num in enumerate(nums):
            nex = max(nex+num, num)
            if i == 0:
                ret = nex
            else:
                ret = max(nex, ret)
            
        return ret
