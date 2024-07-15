#Time Complexity: O(logn)
#Space Complexity: O(1)
#Approach: Modular Arithmetic
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles_empty = 0
        res = 0
        while numBottles > 0 or bottles_empty > numExchange:
            res += numBottles
            bottles_empty += numBottles
            numBottles = 0
            numBottles = bottles_empty // numExchange
            bottles_empty = bottles_empty % numExchange
        return res
