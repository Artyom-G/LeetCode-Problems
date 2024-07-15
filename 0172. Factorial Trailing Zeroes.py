#Time Complexity: O(1)
#Space Complexity: O(0)
#Approach: Modular Arithmetic, Math
#This is better than LeetCode's Follow-Up of "Could you write a solution that works in logarithmic time complexity?"
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n // 5 + n // 25 + n // 125 + n // 625 + n // 3125

#Time Complexity: O(nlogn)
#Space Complexity: O(1)
#Approach: Modular Arithmetic, Math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        twos = 0
        fives = 0
        for i in range(2, n + 1):
            num = i
            while num % 2 == 0:
                twos += 1
                num //= 2
            num = i
            while num % 5 == 0:
                fives += 1
                num //= 5
        return min(twos, fives)
