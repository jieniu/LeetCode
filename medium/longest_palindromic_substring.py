'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    class Middle:
        def __init__(self, left, right, offset):
            self._left = left
            self._right = right
            self._offset = offset

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        isSame = True
        for c in s:
            if c != s[0]:
                isSame = False
        if isSame == True:
            return s

        start_pals = []
        max_pal = s[0]

        for i in range(0, len(s)):
            for pals_index in range(0,len(start_pals)):
                left = start_pals[pals_index]._left
                right = start_pals[pals_index]._right
                offset = start_pals[pals_index]._offset = i - right
                if right == 0:
                    continue
                if left - offset < 0 or s[i] != s[left - offset]:
                    if len(max_pal) < right + (offset - 1) - (left - (offset - 1)) + 1:
                        max_pal = s[left - (offset - 1) : right + (offset - 1) + 1]
                    start_pals[pals_index]._right = 0

            if i > 0 and s[i - 1] == s[i]:
                start_pals.append(Solution.Middle(i - 1, i, 0))
            if i > 0 and i + 1 < len(s) and s[i-1] == s[i+1]:
                start_pals.append(Solution.Middle(i - 1, i + 1, 1))

        for m in start_pals:
            if m._right == 0:
                continue
            if len(max_pal) < m._right+m._offset+1 - m._left + m._offset:
                max_pal = s[m._left-m._offset:m._right+m._offset+1]

        return max_pal

s = Solution()
print "bb pal %s" % s.longestPalindrome("bb")
print "bbb pal %s" % s.longestPalindrome("bbb")
print "bbbb pal %s" % s.longestPalindrome("bbbb")
print "bbbbb pal %s" % s.longestPalindrome("bbbbb")
print "cbbd pal %s" % s.longestPalindrome("cbbd")
print "babad pal %s" % s.longestPalindrome("babad")
print "babab pal %s" % s.longestPalindrome("babab")
print "bababx pal %s" % s.longestPalindrome("bababx")
print "aaabaaaa pal %s" % s.longestPalindrome("aaabaaaa")

            #0 1 2 3 4 5 6 7
            #a d c y c d e
            #a d c c d e
            #a d c c d a x
            #a d c y c d a x

            
