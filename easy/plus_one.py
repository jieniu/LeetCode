class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        idx = len(digits) - 1
        while carry > 0 and idx >= 0:
            tmp = carry
            carry = (digits[idx] + tmp) / 10
            digits[idx] = (digits[idx] + tmp) % 10

            idx -= 1
        
        if carry:
            digits = [carry] + digits
        return digits

