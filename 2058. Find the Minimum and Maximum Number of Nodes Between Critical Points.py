#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Linked List, Greedy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        previous = head
        current = previous.next
        next = current.next
        minPos = -1
        maxPos = -1
        pos = 0
        previousPos = -1
        currentPos = -1
        m = -1
        while next:
            if (previous.val < current.val and next.val < current.val) or (previous.val > current.val and next.val > current.val):
                if minPos == -1:
                    minPos = pos
                maxPos = pos
                previousPos = currentPos
                currentPos = pos
                if previousPos != -1 and currentPos != -1:
                    if m != -1:
                        m = min(currentPos - previousPos, m)
                    else:
                        m = currentPos - previousPos
            pos += 1
            previous, current, next = current, next, next.next
        
        if m != -1:
            return [m, maxPos-minPos]
        else:
            return [-1, -1]
