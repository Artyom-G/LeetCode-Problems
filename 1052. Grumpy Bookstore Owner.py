#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Sliding Window
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat = []
        sat_negative = []
        M = 0
        for i in range(len(customers)):
            M += customers[i] * (1-grumpy[i])
            sat.append(customers[i] * (1-grumpy[i]))
            sat_negative.append(customers[i] * grumpy[i])

        M_negative = sum(sat_negative[:minutes])
        M_negative_current = M_negative
        for i in range(minutes, len(sat_negative)):
            M_negative_current = M_negative_current - sat_negative[i-minutes] + sat_negative[i]
            M_negative = max(M_negative, M_negative_current) 

        return M + max(M_negative, 0)
