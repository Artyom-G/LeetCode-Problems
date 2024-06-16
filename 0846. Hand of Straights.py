#Time Complexity: O(n^2)
#Space Complexity: O(n) because of Timsort, could be O(1) with diff sort
#Approach: Sort
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while len(hand) > 0:
            m = hand.pop(0)
            for i in range(groupSize - 1):
                m += 1
                try:
                    hand.remove(m)
                except:
                    return False 
        return True
