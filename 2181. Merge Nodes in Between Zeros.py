#Time Complexity: O(n)
#Space Complexity: O(1) Extra Space
#Approach: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_head = ListNode(0, None)
        new_current = new_head
        new_previous = None
        while current:
            if current.val == 0 and new_head.val != 0:
                new_previous = new_current
                new_current.next = ListNode(0, None)
                new_current = new_current.next
            else:
                new_current.val += current.val
            current = current.next
        new_previous.next = None
        return new_head
