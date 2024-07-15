#Time Complexity: O(n^2)
#Space Complexity: O(1)
#Approach: Bubble Sort
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        previous = nums[0]
        res = 1
        last = len(nums) - 1
        i = 1
        while i <= last:
            if nums[i] == previous:
                count += 1
                res += 1
            else:
                count = 1
            
            previous = nums[i]
            if count > 2:
                j = i
                while j + 1 <= last:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j+=1
                last -= 1

            if count <= 2:
                i += 1

        return last + 1
