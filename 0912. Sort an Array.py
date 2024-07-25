#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: QuickSort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low, high):
            pivot = nums[high]
            i = low - 1

            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i+1

        def quicksort(low=0, high=None):
            if high is None:
                high = len(nums) - 1

            if low < high:
                pivot_index = partition(low, high)
                quicksort(low, pivot_index-1)
                quicksort(pivot_index+1, high)

        quicksort()
        return nums
