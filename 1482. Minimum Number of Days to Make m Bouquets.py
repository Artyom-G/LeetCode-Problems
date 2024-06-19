#Time Complexity O(n^2)
#Space Complexity: O(n)
#Approach: Hash
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        mins = list(dict.fromkeys(bloomDay))
        for M in range(len(mins)):
            bouqs = 0
            bouq_count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= M:
                    if M+1 < len(mins): 
                        bloomDay[i] = mins[M+1]
                    bouq_count+=1
                    if bouq_count >= k:
                        bouq_count = 0
                        bouqs+=1
                        #bloomDay = bloomDay[:i-k+1] + bloomDay[i+1:]
                else:
                    bouq_count = 0
            if bouqs >= m:
                return M

        return -1
