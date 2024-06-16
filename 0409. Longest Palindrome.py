#Time Complexity: O(n^2) but O(n) on average
#Space Complexity: O(n)
#Approach: Sets
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = 0
        char_set = set()
        for i in s:
            if i in char_set:
                char_set.remove(i)
                counter += 2
            else:
                char_set.add(i)
        
        if len(char_set) > 0:
            counter += 1
        return counter
