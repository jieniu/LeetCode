'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        index = 0
        sign = 1
        zigzag_array = []
        for c in s:
            if index == 0:
                sign = 1
            elif index == numRows - 1:
                sign = -1
            if len(zigzag_array) < index + 1:
                zigzag_array.append([])

            zigzag_array[index].append(c)
            index += sign
        return "".join(["".join(x) for x in zigzag_array])

s = Solution()
print s.convert("PAYPALISHIRING", 3)
print s.convert("PAYPALISHIRING", 4)



