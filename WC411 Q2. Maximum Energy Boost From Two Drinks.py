#Time Complexity: O(n)
#Space Complexity: O(n)
#Approach: DP
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        if n == 0: return 0

        res = 0
        A = [energyDrinkA[0]]
        B = [energyDrinkB[0]]

        i = 1
        while i < n:
            if i >= 2: 
                A.append(energyDrinkA[i] + max(A[i-1], B[i-2]))
                B.append(energyDrinkB[i] + max(B[i-1], A[i-2]))
            else:
                A.append(energyDrinkA[i] + A[i-1])
                B.append(energyDrinkB[i] + B[i-1])
            i+=1
        return max(A[-1], B[-1])
