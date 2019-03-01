class Solution(object):
    def nParenthesis(self, n):
        if n < 1:
            return [""]

        ret = []
        n_minus_1 = self.nParenthesis(n-1)

        for i in range(n, 0, -1):
            if i == n:
                ret.append('('*n + ')'*n)
            else:
                for item in n_minus_1:
                    if ')' in item[:i-1]:
                        continue
                    ret.append(item[:i-1] + "()" + item[i-1:])
        return ret



    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.nParenthesis(n)

s = Solution()
print s.nParenthesis(0)
print '---'

print s.nParenthesis(1)
print '---'
print s.nParenthesis(2)
print '---'
print s.nParenthesis(3)
print '---'

print s.nParenthesis(4)
print '---'

