#Time Complexity O(n)
#Space Complexity O(n)
#Approach: Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(lambda: None) 
        for i in range(len(nums)):
            second = target - nums[i]
            if dic[second] != None:
                return [i, dic[second]]
            dic[nums[i]] = i


"""
#Time Complexity O(nlogn) and O(logn) without having to sort
#Space Complexity O(n)
#Approach: Sorted List and Binary Search
#Note: This does not pass LeetCode due to mismatching indicies but this is really useful for some other problems
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        for x in range(len(nums)):
            y = self.binary_search(nums, target - nums[x])
            if(y != -1):
                return [x, y]

    #Binary Search: GEEKS FOR GEEKS
    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
"""

