#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Two Pointer, Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        before_head = ListNode(0)
        after_head = ListNode(0)
        
        before = before_head
        after = after_head
        
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next


#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Two Pointer, Linked List
#Failed on test case 139/168 bruh idk

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        headPtr = ListNode(0, head)
        L = head
        if head.val >= x: L = headPtr
        R = L.next
        while R and R.next:
            if R.next.val >= x:
                R = R.next
            elif L.next.val >= x:
                L.next, R.next.next, R.next = R.next, L.next, R.next.next
                L = L.next
            else: 
                R = R.next
                L = L.next
        R.next = None
        return headPtr.next
