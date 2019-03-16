class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        if m == 0 and n == 0:
            return None

        begin = 0
        end = m
        i = j = 0
        while True:
            i = (begin + end) / 2
            j = (m + n + 1) / 2 - i

            if (i == 0 or j == n or nums2[j] >= nums1[i-1]) and\
                    (i == m or j == 0 or nums1[i] >= nums2[j-1]):
                left_max = 0
                if i == 0: left_max = nums2[j-1]
                elif j == 0: left_max = nums1[i-1]
                else: left_max = max(nums1[i-1],nums2[j-1])
                
                if (m+n)%2 != 0:
                    return left_max

                right_min = 0
                if i == m: right_min = nums2[j]
                elif j == n: right_min = nums1[i]
                else: right_min = min(nums1[i], nums2[j])

                return (left_max + right_min)*1.0/2


            elif j < n and i > 0 and nums2[j] < nums1[i-1]:
                end = i - 1
            elif j > 0 and i < n and nums1[i] < nums2[j-1]:
                begin = i + 1


s = Solution()
assert s.findMedianSortedArrays([1,2,3],[2,4,6,8]) == 3, s.findMedianSortedArrays([1,2,3],[2,4,6,8])
assert s.findMedianSortedArrays([5,6,8],[1,2,3,4]) == 4, s.findMedianSortedArrays([5,6,8],[1,2,3,4])
assert s.findMedianSortedArrays([],[1]) == 1, s.findMedianSortedArrays([],[1])
assert s.findMedianSortedArrays([1,2],[3,4]) == 4, s.findMedianSortedArrays([5,6,8],[1,2,3,4])
