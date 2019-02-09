'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42

Example 3:
Input: "4193 with words"
Output: 4193

Example 4:
Input: "words and 987"
Output: 0

Example 5:
Input: "-91283472332"
Output: -2147483648
'''
class Solution(object):
    int_min = -2147483648
    int_min_backward = -214748364
    int_max = 2147483647
    int_max_backward = 214748364
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number = None
        sign = 1
        for c in str:
            if number == None and c == ' ':
                continue
            elif number == None and c == '-':
                sign = -1
                number = 0
                continue
            elif number == None and c == '+':
                sign = 1
                number = 0
                continue
            elif number == None and (ord(c) < 48 or ord(c) > 57):
                return 0
            elif number == None and (ord(c) >= 48 and ord(c) <= 57):
                number = 0
            elif number != None and (ord(c) < 48 or ord(c) > 57):
                return number

            if number > Solution.int_max_backward or \
                    (number == Solution.int_max_backward and int(c) > 7):
                return Solution.int_max
            if number < Solution.int_min_backward or \
                    (number == Solution.int_min_backward and int(c) > 8):
                return Solution.int_min

            number = number * 10 + sign * int(c)

        if number == None:
            return 0
        return number

s = Solution()
assert s.myAtoi("words and 987") == 0, s.myAtoi("words and 987")
assert s.myAtoi("-91283472332") == -2147483648, s.myAtoi("-91283472332")
assert s.myAtoi(" +123 456") == 123, s.myAtoi(" +123 456")
assert s.myAtoi(" -42") == -42, s.myAtoi(" -42")
assert s.myAtoi("42") == 42, s.myAtoi("42")
assert s.myAtoi("0") == 0, s.myAtoi("0")
assert s.myAtoi("") == 0, s.myAtoi("")
assert s.myAtoi(" ") == 0, s.myAtoi(" ")
assert s.myAtoi("+-2") == 0, s.myAtoi("+-2")
