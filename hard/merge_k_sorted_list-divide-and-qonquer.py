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

        ret = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return ret.next


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = lists
        while len(result) > 1:
            tmp = []
            for i in range(1+len(result)/2):
                sublists = result[i*2:i*2+2]
                if len(sublists) == 0:
                    continue
                retlist = self.mergeTwoLists(sublists)
                tmp.append(retlist)
            result = tmp

        return result[0] if len(result) > 0 else result
