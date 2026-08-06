# Time Complexity: O(n^2) worst but O(n) average
# Space Complexity: O(1)
# Approach: Quick-Select, Divide and Conquer
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k  # kth largest = (n-k)th smallest

        def partition(left, right):
            # Pick a random pivot
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[right] = nums[right], nums[i]
            return i

        left, right = 0, len(nums) - 1

        while True:
            pivot_idx = partition(left, right)

            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1
