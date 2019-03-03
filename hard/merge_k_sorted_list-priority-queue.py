from Queue import PriorityQueue
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))

        res = ListNode(0)
        curr = res
        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next

            node = node.next
            if node:
                q.put((node.val, node))

        return res.next


def transfer_list_queue(l):
    n = ListNode(0)
    h = n
    for i in l:
        n.next = ListNode(i)
        n = n.next
    return h.next


