#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        k = 2
        current = head
        lists = []
        i = k
        while current:
            if i == k:
                lists.append([])
                i = 0
            lists[-1].append(current)
            current = current.next
            i+=1

        for l in range(0, len(lists) - 1):
            lists[l].reverse()
        if len(lists[-1]) == k: lists[-1].reverse()
        
        head = lists[0][0]
        lists[0].pop(0)
        previous = head

        for l in lists:
            for j in l:
                previous.next = j
                previous = j
        
        previous.next = None
        return head
