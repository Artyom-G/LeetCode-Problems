//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Two Pointer, Linked List

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;
        do{
            if(fast == NULL) return false;
            fast = fast->next;
            if(fast == NULL) return false;
            fast = fast->next;
            slow = slow->next;
        }while(slow != fast); 
        return true;
    }
};

//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Set, Linked List

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> seen;
        ListNode* cur;
        cur = head;
        while(cur!=NULL && !seen.contains(cur)){
            cout << cur->val << ' ';
            seen.insert(cur);
            cur = cur->next;
        }
        if(cur == NULL) return false;
        return true;
    }
};
