"""
使用堆栈来存储左边括号，右边括号收尾时，有 2 种情况
1. 包围方式：(()())，此时用最右边的')'的位置减去最左边的'('的位置即为有效长度
2. 相邻方式：()()()()，此时每对括号结束时，需要加上上一对括号的长度，将上一对括号长度存储到 dict 中可以加速查找
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        previous_len = {}
        max_len = 0
        for i, c in enumerate(s):
            if c == ')' and len(stack) == 0:
                continue
            elif c == ')':
                begin = stack.pop()
                l = i - begin + 1
                if begin - 1 in previous_len:
                    l += previous_len[begin-1]
                previous_len[i] = l
                if l > max_len:
                    max_len = l
            elif c == '(':
                stack.append(i)
            else:
                raise Exception('invalid character, should be "(" or ")"')

        return max_len

s = Solution()
assert s.longestValidParentheses('(()') == 2, s.longestValidParentheses('(()') 
assert s.longestValidParentheses(')()())') == 4
assert s.longestValidParentheses(')()(())') == 6
assert s.longestValidParentheses(')()(())()') == 8
assert s.longestValidParentheses(')())(())()') == 6
assert s.longestValidParentheses(')())(())(()') == 4
