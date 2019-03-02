# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, sublists):
        if len(sublists) == 1:
            return sublists[0]
        l1 = sublists[0]
        l2 = sublists[1]

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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 1:
            return lists[0]

        result = []
        for i in range(1+len(lists)/2):
            sublists = lists[i*2:i*2+2]
            if len(sublists) == 0:
                continue
            retlist = self.mergeTwoLists(sublists)
            result.append(retlist)

        return mergeKLists(result)


