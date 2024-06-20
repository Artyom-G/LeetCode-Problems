#Time Complexity: O(nlogn)
#Space Complexity: O(n) because of Timsort
#Approach: Binary Search, Sort, Modular Arithmetic 
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def checkValidity(mid):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position = position[i]
                if count == m:
                    return True
            return False
        
        low = 1
        high = position[-1] - position[0]
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            if checkValidity(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
