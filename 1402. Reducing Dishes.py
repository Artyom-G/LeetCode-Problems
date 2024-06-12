#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: Sort
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = []
        neg = []
        for i in range(len(satisfaction)):
            if satisfaction[i] >= 0:
                res = satisfaction[i:]
                neg = list(reversed(satisfaction[:i]))
                break

        series = 0
        for i in range(len(res)):
            series += (i+1) * res[i]

        res_sum = sum(res)
        for i in neg:
            if series < series + res_sum + i:
                series = series + res_sum + i
                res_sum += i
            else:
                break
        return series
        
