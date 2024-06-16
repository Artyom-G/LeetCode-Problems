#Time Complexity: O(n^2) but O(n*mlogm) on average
#Space Complexity: O(n*m)
#Approach: Hashmap, Sort
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = dict()
        res = []
        for word in strs:
            count = str(sorted(word))
            if count in counts:
                res[counts[count]].append(word)
            else:
                res.append([word])
                counts[count] = len(res) - 1
        return res
