#Time Complexity: O(n^2)
#Space Complexity: O(n)
#Approach: Greedy, Recursion, Sets, Math
#Solution fails on some test cases
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #Property: f you have a range [1, k] patched then adding k+1 will completely patch [1, 2k+1]
        #Step 1: completely patch [1, M] where M is the max value in nums
        res = 0
        M = max(nums)
        patched = set()

        def recursion(arr, removed):
            arr.pop(removed)
            if len(arr) > 0:
                S = sum(arr)
                patched.add(S)
                for i in range(len(arr)):
                    recursion(arr[:], i)
        
        patched.add(sum(nums))
        recursion(nums + [-1], -1)
        
        num_patches = 0
        print(patched)
        while num_patches < M - 1:
            num_patches = 0
            frequency_map = dict()
            for i in range(1, M):
                if i not in patched:
                    frequency_map[i] = 1
                    for j in patched:
                        if j < M:
                            patch = i - j
                            if patch > 0:
                                if patch in frequency_map:
                                    frequency_map[patch] += 1
                                else:
                                    frequency_map[patch] = 1
                else:
                    num_patches += 1
            
            if num_patches >= M - 1:
                break

            #Assume the mode is the number we want to add, if multiple modes then take the max one
            mode = -1
            mode_freq = 0
            for i in frequency_map.keys():
                if frequency_map[i] > mode_freq or (frequency_map[i] == mode_freq and mode < i):
                    mode = i
                    mode_freq = frequency_map[i]

            for i in list(patched):
                patched.add(i + mode)
            patched.add(mode)
            print(mode)
            nums.append(mode)
            res += 1

        #Step 2: continously add S+1 where S is the biggest possible sum and recalculate S
        S = sum(nums)
        while S < n:
            res += 1
            S += S + 1

        return res
