class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [[heights[i], names[i]] for i in range(len(names))]
        people.sort()
        res = [p[1] for p in people]
        return res[::-1]
