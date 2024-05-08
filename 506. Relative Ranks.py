#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: value-index vector pair
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        vectorPair = []
        for i in range(len(score)):
            vectorPair.append([score[i], i])
        
        vectorPair.sort(key = lambda x: -x[0])

        placements = ["" for i in vectorPair]

        if(len(placements) > 0):
            placements[vectorPair[0][1]] = "Gold Medal"
            if(len(placements) > 1): placements[vectorPair[1][1]] = "Silver Medal"
            if(len(placements) > 2): placements[vectorPair[2][1]] = "Bronze Medal"

        for i in range(3, len(vectorPair)):
            placements[vectorPair[i][1]] = str(i + 1)
        
        return placements
