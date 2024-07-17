#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Sort, Two-Pointer
#I found this problem to be similar to 0084. Largest Rectangle in Histogram
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        R = len(citations)
        M = 0
        for L in range(R):
            M = max(M, min(R-L, citations[L]))
        return M
