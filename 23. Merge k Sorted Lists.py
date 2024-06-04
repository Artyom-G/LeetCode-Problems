#Time Complexity: O(n*k)
#Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def findSmallest(arr):
            j = 0
            while(j<len(arr)):
                if(arr[j] == None):
                    arr.pop(j)
                else:
                    j+=1
            if len(arr) == 0: return None
            smallest = arr[0]
            smallest_i = 0
            for i in range(1, len(arr)):
                if smallest.val > arr[i].val:
                    smallest = arr[i]
                    smallest_i = i
            if smallest != None: arr[smallest_i] = smallest.next
            return smallest

        def printLists(arr):
            for i in arr:
                if i: print(i.val)
                else: print(None)
            print("----------------")

        root = findSmallest(lists)
        current = root
        #printLists(lists)
        while(True):
            smallest = findSmallest(lists)
            if smallest == None:
                break
            current.next = smallest
            current = current.next
            #printLists(lists)

        return root
