//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Set

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
