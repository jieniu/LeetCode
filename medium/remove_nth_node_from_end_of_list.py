'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def travelList(self, node, parent, info):
        if node.next is None:
            info.append(parent)
        else:
            self.travelList(node.next, node, info)
            info.append(parent)

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        info = []
        self.travelList(head, None, info)
        if n < 1 or n > len(info):
            return head

        if info[n-1] == None:
            head = head.next
        else:
            parent = info[n-1]
            parent.next = parent.next.next

        return head

l1 = ListNode(5)
s = Solution()
head = s.removeNthFromEnd(l1, 1)
assert head is None
        
l5 = ListNode(5)
l4 = ListNode(4)
l4.next = l5
l3 = ListNode(3)
l3.next = l4
l2 = ListNode(2)
l2.next = l3
l1 = ListNode(1)
l1.next = l2

s = Solution()
head = s.removeNthFromEnd(l1, 0)
assert head == l1
head = s.removeNthFromEnd(l1, 6)
assert head == l1

head = s.removeNthFromEnd(l1, 2)
while head is not None:
    print head.val
    head = head.next

print '----'
head = s.removeNthFromEnd(l1, 4)
l1 = head
while head is not None:
    print head.val
    head = head.next
print '----'
head = s.removeNthFromEnd(l1, 1)
while head is not None:
    print head.val
    head = head.next
