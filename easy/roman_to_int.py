class Solution(object):
	def __init__(self):
		self._single = {
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000
		}
		self._double = {
			'IV': 4,
			'IX': 9,
			'XL': 40,
			'XC': 90,
			'CD': 400,
			'CM': 900
		}
		self._special = ['I', 'X', 'C']

	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		last = ''
		number = 0
		for x in s:
			if x in self._special and last is '':
				last = x

			elif last != '':
				last = last + x
				if last in self._double:
					number += self._double[last]
					last = ''
				else:
					number += self._single[last[0]]
					last = last[1]
			else:
				number += self._single[x]
				if last != '':
					number += self._single[last]

		return number

s = Solution()
print s.romanToInt("MDCCCLXXXIV")

