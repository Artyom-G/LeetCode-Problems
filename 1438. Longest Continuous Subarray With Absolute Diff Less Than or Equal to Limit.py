#Time Complexity: O(n)
#Space Complexity: O(1)
#Approach: Sliding Window
#I misintrepreated the question and thought they wanted to count the number of valid subarrays lol
#PS this also undercounts in the case where: M - m > limit and the algorithm updates left = right but nums[left] was a minimum. In this case it should update to left += 1 instead.
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) <= 1:
            return len(nums)
        left = 0
        right = left + 1
        #Any subarray with size 1 is valid and wont be checked
        count = len(nums)
        M = max(nums[0], nums[1])
        m = min(nums[0], nums[1])
        while(left < len(nums)):
            print(left, right)
            if(M - m > limit or right >= len(nums) - 1):
                left = right
                right = left + 1
                if(right < len(nums)):
                    M = max(nums[left], nums[right])
                    m = min(nums[left], nums[right])

                #All subarrays in-between are valid, count those
                n = right - left
                count += n*(n+1)//2

            else:
                M = max(M, nums[right])
                m = min(m, nums[right])
                right += 1
        
        return count 

