# -*- coding: utf-8 -*-

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

	Input: 123
	Output: 321

Example 2:

	Input: -123
	Output: -321

Example 3:

	Input: 120
	Output: 21
"""

class Solution_s1(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		if x < -2147483648 or x > 2147483647:
			return 0

		sign = cmp(x, 0)
		src = abs(x)

		res = 0
		while src > 0:
			res = res * 10 + src % 10
			src = src / 10

		res = res * sign

		if res < -2147483648 or res > 2147483647:
			return 0

		return res

class Solution_s2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = cmp(x,0) * int(str(abs(x))[::-1])
        if result < -2 ** 31 or result >= 2 ** 31:
            return 0
        else:
            return result
