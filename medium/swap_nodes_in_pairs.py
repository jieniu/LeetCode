'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = left = ListNode(0)
        ret.next = left.next = head
        cnt = 0
        while head:
            cnt += 1
            if cnt % 2 == 0:
                tmp = head.next 
                head.next = left.next
                left.next.next = tmp
                left.next = head
                left = head.next
                head = left

            head = head.next
            
        return ret.next
