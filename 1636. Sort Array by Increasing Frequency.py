#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: Sort, HashMap
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for i in nums:
            if i not in freqs: freqs[i] = 1
            else: freqs[i] += 1
           
        nums_freqs = [[i, freqs[i]] for i in nums]
        nums_freqs.sort(key=lambda x: (x[1], -x[0]))
        return [i[0] for i in nums_freqs]
