#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: Sorting 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1
        return count
