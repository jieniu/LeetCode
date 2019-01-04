# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
class Solution(object):
    def __init__(self):
        # python 中的 dict 是用 hash table 实现的
        self.differences = {}

    def twoSum(self, nums, target):
        index = 0
        for number in nums:
            if number in self.differences:
                begin_index = self.differences[number]
                end_index = index
                return [begin_index, end_index]
            else:
                difference = target - number
                if difference in self.differences:
                    index += 1
                    continue
                self.differences[difference] = index

            index += 1
        return None

s = Solution()
print s.twoSum([2,7,11,15], 9)
