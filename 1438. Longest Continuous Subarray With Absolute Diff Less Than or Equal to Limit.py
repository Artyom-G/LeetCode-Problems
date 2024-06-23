#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Sliding Window, Double-Ended Queues
class Solution():
    def longestSubarray(self, nums, limit):
        maxs = deque()
        mins = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while maxs and nums[right] < maxs[-1]:
                maxs.pop()
            maxs.append(nums[right])
            
            while mins and nums[right] > mins[-1]:
                mins.pop()
            mins.append(nums[right])
            
            while mins[0] - maxs[0] > limit:
                if nums[left] == maxs[0]:
                    maxs.popleft()
                if nums[left] == mins[0]:
                    mins.popleft()
                left += 1
                
            max_length = max(max_length, right - left + 1)
        
        return max_length

#Time Complexity: O(n^2)
#Space Complexity: O(1)
#Approach: Sliding Window
#Time Limit Exceeded
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) <= 1:
            return len(nums)
        left = 0
        right = left + 1
        res = 1
        M = max(nums[0], nums[1])
        m = min(nums[0], nums[1])
        while(left < len(nums)):
            #print(left, right)
            if(right >= len(nums)):
                res = max(res, right - left)
                break
            else:
                M = max(M, nums[right])
                m = min(m, nums[right])

            if(M - m > limit):
                res = max(res, right - left)
                left = left + 1
                right = left + 1
                if(right < len(nums)):
                    M = max(nums[left], nums[right])
                    m = min(nums[left], nums[right])
            else:
                right += 1

        return res 

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

