#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Frequency Map
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_count = [0, 0, 0]
        for i in nums:
            color_count[i] += 1

        i = 0
        for color in range(3):
            for j in range(color_count[color]):
                nums[i] = color
                i+=1
