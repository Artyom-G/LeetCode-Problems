#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Linked List
#Follow-up: Could you do it in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        L, L2, R, R2 = None, None, None, None
        i = 1
        prev = None
        while current and i <= right + 1:
            if i == left - 1: L = current
            elif i == left: L2 = current
            if i == right: R = current
            elif i == right + 1: R2 = current
            if i >= left and i <= right:
                temp = current.next
                current.next = prev
                i+=1
                prev = current
                current = temp
            else:
                i+=1
                prev = current
                current = current.next

        if L: L.next = R
        if L2: L2.next = R2

        if L2 == head: head = R 
        if head.next == head: head.next = None

        return head 
