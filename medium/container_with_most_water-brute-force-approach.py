'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for width in range (len(height) - 1, 0, -1):
            left = 0
            right = left + width
            while right <= len(height) - 1:
                h = min(height[left], height[right])
                if max_area < h * width:
                    max_area = h * width
                left += 1
                right += 1

        return max_area


s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49, s.maxArea([1,8,6,2,5,4,8,3,7])
assert s.maxArea([8,1,6,2,5,4,8,3,7]) == 56, s.maxArea([8,1,6,2,5,4,8,3,7])
assert s.maxArea([8,1]) == 1, s.maxArea([8,1])
assert s.maxArea([1,2,3,4,5,22,22,1,2,3]) == 22, s.maxArea([1,2,3,4,5,22,22,1,2,3])


