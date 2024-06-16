#Time Complexity: O(n*k)
#Space Complexity: O(log(k))
#Approach: Merge Sort, Divide and Conquer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSort(l1, l2):
            temp = ListNode(0)
            curr = temp
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 is not None else l2
            return temp.next
        
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
            
        mid = len(lists) // 2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return mergeSort(left,right)
        

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
