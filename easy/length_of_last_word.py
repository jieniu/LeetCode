class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        leng = 0
        i = len(s) - 1
        while s[i] == ' ' and i >= 0:
            i -= 1
        
        while i >= 0:
            if s[i] != ' ':
                leng += 1
            else:
                return leng
            i -= 1
            
        return leng
