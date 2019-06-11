"""
Given two integers dividend and divisor, divide two integers without
using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 
2^31 − 1 when the division result overflows.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            x = 0
            while dividend > divisor << x + 1:
                x += 1

            result += 1 << x
            dividend -= divisor << x

        return min(2147483647, result if sign else -result)


if __name__ == "__main__":
    s = Solution()
    assert s.divide(-10, -3) == 3
    assert s.divide(-10, 3) == -3
    assert s.divide(10, 3) == 3
    assert s.divide(10, -3) == -3
    assert s.divide(10, -1) == -10
    assert s.divide(10, -5) == -2
    assert s.divide(10, 10) == 1 
    assert s.divide(10, 11) == 0 
    assert s.divide(-2147483648, -1) == 2147483647 


