//https://leetcode.com/problems/design-linked-list/description/
class Mynode {
public:
    int val;
    Mynode* next;
};

class MyLinkedList {
public:
    MyLinkedList() {
        dumy_head = new Mynode();
        dumy_head->next = NULL;
    }
    
    int get(int index) {
        if (index < 0) {
            return -1;
        }

        Mynode* cur = dumy_head->next;
        while (index--) {
            cur = cur->next;
            if (cur == NULL) {
                return -1;
            }
        }
        if (cur == NULL) {
            return -1;
        }

        return cur->val;
    }
    
    void addAtHead(int val) {
        Mynode* newnode = new Mynode();
        newnode->val = val;
        newnode->next = dumy_head->next;
        dumy_head->next = newnode;
    }
    
    void addAtTail(int val) {
        Mynode *cur = dumy_head;
        while (cur->next) {
            cur = cur->next;
        }

        Mynode* newnode = new Mynode();
        newnode->val = val;
        newnode->next = NULL;
        cur->next = newnode;
    }
    
    void addAtIndex(int index, int val) {
        Mynode* cur = dumy_head;
        while (index--) {
            cur = cur->next;
            if (cur == NULL) {
                return;
            }
        }
        
        Mynode *nn = new Mynode();
        nn->val = val;
        nn->next = cur->next;
        cur->next = nn;
        
    }
    
    void deleteAtIndex(int index) {
        Mynode* cur = dumy_head;
        
        while (index--) {

            cur = cur->next;
            if (cur == NULL) {
                return;
            }
        }
        Mynode* tmp = cur->next;
        if (tmp) {
            cur->next = tmp->next;
        } else {
            cur->next = NULL;
        }        
        delete tmp;
    }
private:
    Mynode* dumy_head;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
