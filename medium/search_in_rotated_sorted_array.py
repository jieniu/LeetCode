class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1 and nums[0] != target:
            return -1

        mid = int(len(nums)/2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid] and target <= nums[len(nums)-1]:
            return -1 if self.search(nums[mid+1:], target) == -1 else mid + self.search(nums[mid+1:], target) + 1
        elif target >= nums[0] and target < nums[mid]:
            return self.search(nums[:mid], target)
        elif nums[mid] <= nums[len(nums)-1] and mid > 0:
            return self.search(nums[:mid], target)
        elif mid < len(nums)-1:
            return -1 if self.search(nums[mid+1:], target) == -1 else mid + self.search(nums[mid+1:], target) + 1
        else:
            return -1

s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1, s.search([4,5,6,7,0,1,2], 3) 
assert s.search([4,2], 3) == -1
assert s.search([4,2], 5) == -1
assert s.search([4,2], 1) == -1
assert s.search([4,2], 2) == 1 
assert s.search([4,2], 4) == 0,s.search([4,2], 4)
assert s.search([2,4], 4) == 1,s.search([4,2], 4)
assert s.search([2,4], 2) == 0,s.search([4,2], 4)
assert s.search([2], 2) == 0,s.search([4,2], 4)
assert s.search([2], 4) == -1,s.search([4,2], 4)
assert s.search([2], 4) == -1,s.search([4,2], 4)
assert s.search([], 4) == -1,s.search([4,2], 4)
