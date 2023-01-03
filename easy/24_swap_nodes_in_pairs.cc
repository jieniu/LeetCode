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
    ListNode* swapPairs(ListNode* head) {
        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *cur = dummy;
        
        while (cur->next != NULL && cur->next->next != NULL) {
            ListNode *first = cur->next;
            ListNode *sec = cur->next->next;
            first->next = sec->next;
            sec->next = first;
            cur->next = sec;
            
            cur = cur->next->next;
        }
        head = dummy->next;
        delete dummy;
        return head;
    }
};
