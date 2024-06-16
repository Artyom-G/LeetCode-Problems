#Time Complexity: O(n+m)
#Space Complexity: O(n+m)
#Approach: Strings
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = ""
        list2 = ""
        node = l1
        while(node != None):
            list1 += str(node.val)
            node = node.next
        node = l2
        while(node != None):
            list2 += str(node.val)
            node = node.next
        num1 = int(list1[::-1])
        num2 = int(list2[::-1])
        num = str(num1 + num2)[::-1]
        i = 0
        node = ListNode(int(num[i]), None)
        root = node
        while(i < len(num)-1):
            i += 1
            node.next = ListNode(int(num[i]), None)
            node = node.next
        return root
