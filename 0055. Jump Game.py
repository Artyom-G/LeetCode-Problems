#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Array, Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = []
        i = 0
        while i < len(nums) - 1:
            stack.append(nums[i])
            if nums[i] == 0:
                j = 0
                while j < len(stack):
                    if nums[len(stack)-j-1] < j + 1:
                        j+=1
                        continue
                    else: break
                else:
                    return False
            i+=1
        return True
