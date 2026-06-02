#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: Sort, Two Pointer
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        j = 0
        for i in range(len(magazine)):
            if magazine[i] == ransomNote[j]:
                j+=1
                if j >= len(ransomNote): return True
        return False


# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for l in magazine:
            if(l in letters):
                letters[l] += 1
            else:
                letters[l] = 1
        
        for l in ransomNote:
            if(l not in letters):
                return False
            if(letters[l] <= 0):
                return False
            letters[l] -= 1
        return True
