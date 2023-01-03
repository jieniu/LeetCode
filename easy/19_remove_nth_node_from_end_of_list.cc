/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *fast = dummy;
        ListNode *slow = dummy;
        ListNode *pre = slow;

        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }
        while (fast) {
            pre = slow;
            fast = fast->next;
            slow = slow->next;
        }

        pre->next = slow->next;
        delete slow;
        head = dummy->next;
        delete dummy;
        return head;

    }
};
