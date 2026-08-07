# Time Complexity: O(n)
# Space Complxity: O(n)
# Approach: DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
            
        left_profits = [0] * n
        right_profits = [0] * n
        
        min_so_far = prices[0]
        for i in range(1, n):
            min_so_far = min(min_so_far, prices[i])
            left_profits[i] = max(left_profits[i-1], prices[i] - min_so_far)
            
        max_so_far = prices[-1]
        for i in range(n-2, -1, -1):
            max_so_far = max(max_so_far, prices[i])
            right_profits[i] = max(right_profits[i+1], max_so_far - prices[i])
            
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profits[i] + right_profits[i])
            
        return max_total

# Time Complexity: O(n^2) (Time Limit Exceeded)
# Space Complxity: O(n)
# Approach: DP, Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # RangeMin[i][j] = min{prices[k]} where k in i..j
        # profit1[i] profit by selling on ith day
        # profit1[i] = prices[i] - RangeMin[0][i-1]
        # profit2[i] max profit by selling second time on ith day 
        # profit2[i] = max(maxProfit1[j] + prices[i] - RangeMin[index][i-1]) for all j

        n = len(prices)
        if n == 0:
            return 0
        profit1 = [0] * n
        min_so_far = prices[0]
        
        for i in range(1, n):
            # min_so_far represents RangeMin[0][i-1]
            profit1[i] = prices[i] - min_so_far
            # Update min_so_far for the next iteration
            min_so_far = min(min_so_far, prices[i])
        
        profit2 = [0] * n
        for i in range(1, n):
            max_p2 = 0
            
            # This variable will represent RangeMin[j][i-1] dynamically
            range_min = float('inf')
            # Loop backwards so we can build the minimum from i-1 down to 0
            for j in range(i - 1, -1, -1):
                range_min = min(range_min, prices[j])
                curr_profit = profit1[j] + prices[i] - range_min
                max_p2 = max(max_p2, curr_profit)
            profit2[i] = max_p2

        m = 0
        for i in range(n):
            m = max(m, profit1[i], profit2[i])
        return m
