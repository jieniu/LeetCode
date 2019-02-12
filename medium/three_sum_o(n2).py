class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) < 3:
            return []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                        
        return ret
        

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
print s.threeSum([-1,0,1,-4,3])
print s.threeSum([0,0,0,0])
print s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])


