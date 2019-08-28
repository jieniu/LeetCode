class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        mid = len(nums) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if mid == 0: return 1
            return mid + self.searchInsert(nums[mid+1:], target) + 1
        else:
            if mid == 0: return 0
            return self.searchInsert(nums[:mid], target)
