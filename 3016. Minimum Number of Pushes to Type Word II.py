#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: Sort, Freq Map
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = {}
        for i in word:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        
        most_freq = []
        for i in counter.keys():
            most_freq.append([i, counter[i]])
        most_freq.sort(key=lambda x: -x[1])

        multiplier = 0
        res = 0
        for i in range(len(most_freq)):
            if i % 8 == 0: multiplier += 1
            res += multiplier * most_freq[i][1]

        return res
