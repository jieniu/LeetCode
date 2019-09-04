class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        ret = ""
        carry = 0
        while i >= 0 and j >= 0:
            ret = str((int(a[i]) + int(b[j]) + carry) % 2) + ret
            carry = (int(a[i]) + int(b[j]) + carry) / 2
            i -= 1
            j -= 1
        while i >= 0:
            ret = str((int(a[i]) + carry) % 2) + ret
            carry = (int(a[i]) + carry) / 2
            i -= 1
        while j >= 0:
            ret = str((int(b[j]) + carry) % 2) + ret
            carry = (int(b[j]) + carry) / 2
            j -= 1
        if carry:
            ret = str(carry) + ret
        return ret

