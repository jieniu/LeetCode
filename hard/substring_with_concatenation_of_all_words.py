'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        slen = len(s)
        num = len(words)
        wlen = len(words[0])
        ret = []
        for i in range(len(s)-num*wlen+1):
            seen = {}
            j = 0
            while j < num:
                sub = s[i+wlen*j:i+wlen*(j+1)]
                if word_count.has_key(sub):
                    seen[sub] = seen.get(sub, 0) + 1
                else:
                    break
                if seen[sub] > word_count[sub]:
                    break
                j += 1

            if j == num:
                ret.append(i)

        return ret



