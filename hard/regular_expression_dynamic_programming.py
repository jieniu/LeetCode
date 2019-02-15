class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        mem = {}
        def dp(i, j):
            if (i, j) in mem:
                return mem[(i, j)]

            if j >= len(p):
                res = i >= len(s)
            else:

                first_match = i <= len(s) - 1 and p[j] in {s[i], '.'}

                if j <= len(p) - 2 and p[j+1] == '*':
                    res = dp(i, j+2) or first_match and dp(1+i, j)
                else:
                    res = first_match and dp(1+i, 1+j)

            mem[(i, j)] = res
            return res

        return dp(0, 0)



s = Solution()
assert s.isMatch("", ".") == False
assert s.isMatch("a", "") == False
assert s.isMatch("a", "a") == True
assert s.isMatch("a", ".") == True
assert s.isMatch("", "") == True
assert s.isMatch("aa", "a*") == True
