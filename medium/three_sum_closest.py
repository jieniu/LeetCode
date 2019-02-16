'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i = 0
        (min_sum,ret) = (None,None)
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summary = nums[i] + nums[j] + nums[k] 
                
                if min_sum == None:
                    min_sum = abs(summary - target)
                    ret = summary
                elif min_sum > abs(summary - target):
                    min_sum = abs(summary - target)
                    ret = summary

                if summary < target:
                    j += 1
                elif summary > target:
                    k -= 1
                else:
                    return target
            i += 1
        return ret

s = Solution()
assert s.threeSumClosest([-1,2,1,-4], 1) == 2, s.threeSumClosest([-1,2,1,-4], 1)
assert s.threeSumClosest([1,1,1,0], -100) == 2, s.threeSumClosest([1,1,1,0], -100)
