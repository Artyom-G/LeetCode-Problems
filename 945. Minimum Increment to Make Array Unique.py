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
        
        #print(used)
        used = list(used)
        #print(used)

        while len(nums) > 0:
            try:
                index = used.index(nums[-1])
                while nums[-1] == used[index]:
                    nums[-1] += 1
                    index+=1
                    counter += 1
                used.insert(index, nums[-1])

            except:
                used.append(nums[-1])
                used.sort()
            nums.pop()

        return counter
