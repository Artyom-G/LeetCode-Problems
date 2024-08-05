#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: HashSets
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        words = set()
        distinct = set(arr)
        for word in arr:
            if word not in words:
                words.add(word)
            elif word in distinct:
                distinct.remove(word)

        d = 0
        for i in arr:
            if i in distinct:
                d += 1
                if d == k: return i
        return ""
