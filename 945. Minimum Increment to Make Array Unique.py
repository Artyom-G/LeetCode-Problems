class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        used = set()
        counter = 0
        i=0
        while i < len(nums):
            if nums[i] not in used:
                used.add(nums[i])
                nums.pop(i)
            else:
                i+=1
        
        while len(nums) > 0:
            while nums[-1] in used:
                nums[-1] += 1
                counter += 1
            used.add(nums[-1])
            nums.pop(-1)

        return counter
