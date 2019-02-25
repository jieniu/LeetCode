'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution(object):
    def nSum(self, nums, target, nSum, prefix, ret):
        if len(nums) < nSum or nSum < 2 or target < nSum * nums[0] or target > nSum * nums[-1]:
            return

        if nSum == 2:
            l = 0 
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    ret.append(prefix + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        else:
            for i in range(0, len(nums) - nSum + 1):
                if i > 0 and nums[i-1] == nums[i]:
                    continue

                self.nSum(nums[1+i:], target - nums[i], nSum - 1, prefix + [nums[i]], ret)
     
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        self.nSum(nums, target, 4, [], ret)

        return ret

s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)

