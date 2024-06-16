#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        output = []

        #This is a huge time saver
        seen_add = seen.add
        
        for i in nums:
            if(i not in seen):
                output.append(i)
            seen_add(i)
        for i in range(len(seen)):
            nums[i] = output[i]
        return len(seen)

