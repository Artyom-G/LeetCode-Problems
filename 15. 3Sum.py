#Time Complexity O(n^3) but O(n^2) on average
#Space Complexity O(n)
#Approach: fix x value and get y and z with Two Sum
#This solution passed all test cases on Leet Code but was rejected for the Exceeding Time Limit
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            dic = defaultdict(lambda: None) 
            output = []
            for i in range(len(nums)):
                second = target - nums[i]
                if dic[second] != None:
                    output.append([i, dic[second]])
                dic[nums[i]] = i
            return output
        
        nums.sort()
        output = []
        output_dic = {}
        seen = set()
        for x in range(len(nums)):
            if(nums[x] not in seen):
                solutions = twoSum(self, nums, -nums[x])
                for solution in solutions:
                    y, z = solution
                    #print(y, z)
                    if(y != x != z):
                        sol = sorted([nums[x], nums[y], nums[z]])
                        #print(sol)
                        if tuple(sol) not in output_dic:
                            output_dic[tuple(sol)] = 1
                            output.append(sol)
                seen.add(nums[x])
        
        return output
