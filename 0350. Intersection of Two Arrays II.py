#Time Complexity: O(n + m)
#Space Complexity: O(n + m)
#Approach: Hash, Frequency Map
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        for i in nums1:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1
        freq2 = {}
        for i in nums2:
            if i in freq2:
                freq2[i] += 1
            else:
                freq2[i] = 1
        
        res = []
        for i in freq1:
            if i in freq2:
                res += [i] * min(freq1[i], freq2[i])
        return res
