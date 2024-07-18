#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: Sort, Array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        arr = []
        current = head
        i = 0
        while current:
            arr.append((current.val, i, current))
            current = current.next  
            i += 1
        if len(arr) == 1: return arr[0][2]

        arr.sort()
        arr[0][2].next = arr[1][2]
        for i in range(1, len(arr)):
            arr[i-1][2].next = arr[i][2]
        arr[len(arr)-1][2].next = None

        return arr[0][2]
