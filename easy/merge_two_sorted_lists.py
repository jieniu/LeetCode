'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = None
        curr = None
        while l1 is not None or l2 is not None:
            val = None
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    val = l1.val
                    l1 = l1.next
                else:
                    val = l2.val
                    l2 = l2.next

            elif l1 is not None:
                val = l1.val
                l1 = l1.next

            else:
                val = l2.val
                l2 = l2.next

            if curr is None:
                curr = ListNode(val)
                ret = curr
            else:
                curr.next = ListNode(val)
                curr = curr.next

        return ret

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(1)
l2 = ListNode(2)
l2.next = ListNode(2)
l2.next.next = ListNode(2)

s = Solution()
ret = s.mergeTwoLists(l1,l2)
while ret is not None:
    print ret.val
    ret = ret.next
