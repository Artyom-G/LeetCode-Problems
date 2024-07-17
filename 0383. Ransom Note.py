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
