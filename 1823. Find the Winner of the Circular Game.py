#Time Complexity: O(n^2)
#Space Complexity: O(n)
#Approach: Modular Arithmetic
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k - 1
        players = [i for i in range(1, n+1)]
        c = 0
        while len(players) > 1:
            c = (c + k%len(players)) %len(players)
            print(c)
            del players[c]

        return players[0]
            
