# Time Complexity: O(n)
# Space Complexity: O(1) auxiliry but O(n)
# Approach: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        root = head
        while head.next != None:
            if head.val == head.next.val:
                temp = head.next
                head.next = head.next.next
                del temp
            else:
                head = head.next
        return root
