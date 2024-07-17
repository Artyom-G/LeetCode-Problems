//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Hash, Linked List

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> map;
        Node* cur = head;
        Node* newPrev = NULL;
        Node* newCur = NULL;
        while(cur != NULL){
            newCur = new Node(cur->val);
            map[cur] = newCur;
            if(newPrev != NULL) newPrev->next = newCur;
            newPrev = newCur;
            cur = cur->next;
        }

        Node* newHead = map[head];
        cur = head;
        while(cur != NULL){
            map[cur]->random = map[cur->random];
            cur = cur->next;
        }

        return newHead;
    }
};
