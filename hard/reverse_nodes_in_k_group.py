# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 0:
            return head

        ret = ListNode(0)
        ret.next = head
        h = ret
        n = head
        count = 0
        while n:
            count += 1
            if count % k == 0:
                rh, rt = self.reverse_list(h.next, k, n.next)
                h.next = rh
                h = n = rt
            n = n.next

        return ret.next

    def reverse_list(self, head, count, next):
        ret = ListNode(0)
        ret.next = next
        n = head
        while n and count > 0:
            tmp = n.next
            n.next = ret.next
            ret.next = n
            n = tmp
            count -= 1

        return ret.next, head

def test():
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    s = Solution()
    h = s.reverseKGroup(h, 1)

    while h:
        print(h.val)
        h = h.next


if __name__ == "__main__":
    test()

