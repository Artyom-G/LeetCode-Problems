#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: strings

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(100000)
        current = head
        num = ""
        while(current):
            num += str(current.val)
            current = current.next
        num = str(int(num) * 2)

        head = ListNode(int(num[0]), None)
        prev = head
        for i in num[1:]:
            current = ListNode(int(i), None)
            prev.next = current
            prev = current
        
        return head
