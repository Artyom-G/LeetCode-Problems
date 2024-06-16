#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length+=1
        n = length - n

        if n == 0:
            return head.next

        current = head
        for i in range(n - 1):
            current = current.next
        prev = current
        current = prev.next
        next = current
        if current: next = current.next
        del current
        prev.next = next
        return head
        
