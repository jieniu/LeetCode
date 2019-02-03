'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
#s d v d t s
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        current_substring = [None]*128
        current_substring_len = 0
        begin_index = 0
        for i in s:
            stoi = ord(i)
            if current_substring[stoi] is None or current_substring[stoi] < begin_index:
                current_substring[stoi] = begin_index + current_substring_len
                current_substring_len += 1
            else:
                if maxlen < current_substring_len:
                    maxlen = current_substring_len 
                
                sub_len = current_substring[stoi] - begin_index + 1
                begin_index = current_substring[stoi] + 1
                current_substring_len -= sub_len

                current_substring[stoi] = current_substring_len + begin_index
                current_substring_len += 1

        if maxlen < current_substring_len:
            maxlen = current_substring_len
        return maxlen

if __name__ == "__main__":
    s = Solution()
    print("abcabcbb: %s" % s.lengthOfLongestSubstring("abcabcbb"))
    print("pwwkew: %s" % s.lengthOfLongestSubstring("pwwkew"))
    print("bbbbbbbb: %s" % s.lengthOfLongestSubstring("bbbbbbbb"))
    print("'': %s" % s.lengthOfLongestSubstring(""))
    print("' ': %s" % s.lengthOfLongestSubstring(" "))
    print("dvdf: %s" % s.lengthOfLongestSubstring("dvdf"))
    print("sdvdfs: %s" % s.lengthOfLongestSubstring("sdvdfs"))
            

