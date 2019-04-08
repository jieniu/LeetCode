"""
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this
by modifying the input array in-place with O(1) extra memory.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        index = -1
        for i, num in enumerate(nums):
            if last != num:
                index += 1
                if i != index:
                    nums[index] = num
                last = num

        return index + 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2]
    assert s.removeDuplicates(nums) == 2, s.removeDuplicates(nums)
    assert nums[:2] == [1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]
    nums = []
    assert s.removeDuplicates(nums) == 0
