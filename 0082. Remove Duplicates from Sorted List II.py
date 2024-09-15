#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        last = None
        while cur != None:
            if prev and prev.val != cur.val:
                last = prev
            else:
                if prev and head.val == cur.val: head = cur.next
                if last: 
                    del last.next
                    last.next = cur.next
                    if cur.next and cur.next.val != cur.val:
                        prev = cur
                        cur = cur.next
            prev = cur
            if cur: cur = cur.next
        return head
