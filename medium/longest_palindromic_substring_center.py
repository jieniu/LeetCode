'''
Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''


class Solution():
    """
    solution for this problem
    """
    def expand(self, left, right, s):
        """
        expand from middle point
        """
        if right >= len(s) or s[left] != s[right]:
            return 0

        while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
            left -= 1
            right += 1

        return right + 1 - left

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        middle = 0
        max_len = 0
        for i in range(len(s)):
            len1 = self.expand(i, i, s)
            len2 = self.expand(i, i+1, s)
            longer = max(len1, len2)
            if longer > max_len:
                max_len = longer
                middle = i

        begin = middle-int((max_len-1)/2)
        return s[begin:begin+max_len]


def main():
    """
    main
    """
    solution = Solution()
    assert solution.longest_palindrome('cbbd') == 'bb'
    assert solution.longest_palindrome('babad') == 'bab'
    assert solution.longest_palindrome('c') == 'c'
    assert solution.longest_palindrome('ccccc') == 'ccccc'
    assert solution.longest_palindrome('') == ''


if __name__ == "__main__":
    main()
