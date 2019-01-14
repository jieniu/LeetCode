"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = -1
        for str in strs:
            length = len(str)
            if minlen == -1 or length < minlen:
                minlen = length

        ret = ''
        for i in range(0, minlen):
            character = ''
            for str in strs:
                if character == '':
                    character = str[i]
                    continue
                if character != str[i]:
                    return ret
            ret += character

        return ret
