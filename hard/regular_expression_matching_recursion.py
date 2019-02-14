class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])


s = Solution()
assert s.isMatch("", ".") == False
assert s.isMatch("a", "") == False
assert s.isMatch("a", "a") == True
assert s.isMatch("a", ".") == True
assert s.isMatch("", "") == True
assert s.isMatch("aa", "a*") == True
