# Time Complexity: O(n^2)
# Space Complxity: O(n^2)
# Approach: 2D DP, Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # RangeMin[i][j] = min{prices[k]} where k in i..j
        # profit1[i] profit by selling on ith day
        # profit1[i] = prices[i] - RangeMin[0][i-1]
        # maxProfit1[i] is the max profit by ith day and the index of the sell
        # profit2[i] max profit by selling second time on ith day 
        # profit2[i] = max(maxProfit1[j] + prices[i] - RangeMin[index][i-1]) for all j

        n = len(prices)
        RangeMin = [[float("inf") for j in range(n)] for i in range(n)]
        for i in range(n):
            m = float("inf")
            for j in range(i, n):
                m = min(m, prices[j])
                RangeMin[i][j] = m
        
        profit1 = [0]
        maxProfit1 = [0]
        maxProfit1Index = [0]
        for i in range(1, n):
            profit1.append(prices[i]-RangeMin[0][i-1])
            if profit1[i] > maxProfit1[i-1]:
                maxProfit1.append(profit1[i])
                maxProfit1Index.append(i)
            else:
                maxProfit1.append(maxProfit1[i-1])
                maxProfit1Index.append(maxProfit1Index[i-1])
        
        profit2 = [0] * n
        for i in range(1, n):
            max_p2 = 0
            for j in range(i):
                # maxProfit1[j]: Best profit from 1st trade ending by day j
                # prices[i] - RangeMin[j][i]: 2nd trade bought between j and i, sold on i
                curr_profit = maxProfit1[j] + prices[i] - RangeMin[j][i]
                max_p2 = max(max_p2, curr_profit)
            profit2[i] = max_p2

        m = 0
        for i in range(n):
            m = max(m, profit1[i], profit2[i])
        return m
