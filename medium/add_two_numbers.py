# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ret = None
        last = None
        while l1 is not None:
            l1_val = l1.val
            l1 = l1.next

            l2_val = 0
            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next

            val = l1_val + l2_val + carry
            carry = val / 10
            val = val % 10

            if ret is None:
                last = ListNode(val)
                ret = last
            else:
                last.next = ListNode(val)
                last = last.next


        while l2 is not None:
            l2_val = l2.val
            l2 = l2.next
            
            val = l2_val + carry
            carry = val / 10
            val = val % 10
            last.next = ListNode(val)
            last = last.next

        if carry == 1:
            last.next = ListNode(carry)

        return ret

def printRet(ret):
    while ret is not None:
        print ret.val
        ret = ret.next
    print '----------'

if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(0)
    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    printRet(ret)

    l2.next = ListNode(1)
    ret = s.addTwoNumbers(l1, l2)
    printRet(ret)

    l1 = ListNode(9)
    l2 = ListNode(1)
    l2.next = ListNode(9)
    tmp = l2.next
    tmp.next = ListNode(9)

    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    printRet(ret)

    l2 = ListNode(9)
    l1 = ListNode(1)
    l1.next = ListNode(9)
    tmp = l1.next
    tmp.next = ListNode(9)

    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    printRet(ret)
