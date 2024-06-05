#Time Complexity: O(n*m)
#Space Complexity: O(n*m)
#Approach: Hash Table
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2: return words
        
        def countDict(word):
            dups = dict()
            for i in word:
                if i in dups:
                    dups[i] += 1
                else:
                    dups[i] = 1
            return dups

        dups = countDict(words[0])

        for word in words:
            dups = Counter(countDict(word)) & Counter(dups)

        return list(dups.elements())
