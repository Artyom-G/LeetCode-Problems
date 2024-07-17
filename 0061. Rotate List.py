#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Linked List, Modular Arithmetic

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return None
        n = 1
        cur = head
        while cur.next:
            n+=1
            cur = cur.next
        k = k % n
        cur.next = head

        newTailI = n-k-1
        n = 0
        cur = head
        while n < newTailI:
            cur = cur.next
            n+=1
        
        head = cur.next
        cur.next = None
        return head
