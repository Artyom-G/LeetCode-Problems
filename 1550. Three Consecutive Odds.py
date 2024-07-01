#Time Complexity: O(n)
#Space Comlplexity: O(1)
#Approach: Array
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 == 1:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 0
        return False
