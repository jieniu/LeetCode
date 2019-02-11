'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        remainder = n % 2
        middle = n / 2

        lastvalue = 0
        currentvalue = 0
        offset1 = offset2 = 0
        for i in range(0, middle + 1):
            if offset1 > len(nums1) - 1:
                lastvalue = currentvalue
                currentvalue = nums2[offset2]
                offset2 += 1
            elif offset2 > len(nums2) - 1:
                lastvalue = currentvalue
                currentvalue = nums1[offset1]
                offset1 += 1
            elif nums1[offset1] < nums2[offset2]:
                lastvalue = currentvalue
                currentvalue = nums1[offset1]
                offset1 += 1
            else:
                lastvalue = currentvalue
                currentvalue = nums2[offset2]
                offset2 += 1

        if remainder == 1:
            return currentvalue
        else:
            return (currentvalue + lastvalue)*1.0 / 2

s = Solution()
assert s.findMedianSortedArrays([1,2],[3,4]) == 2.5
assert s.findMedianSortedArrays([1,3],[2]) == 2
assert s.findMedianSortedArrays([-2,-1],[3]) == -1
