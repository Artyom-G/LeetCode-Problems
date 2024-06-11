#Time Complexity: O(nlogn)
#Space Complexity: O(n)
#Approach: Hash Map, Sort
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frequencies = Counter(arr1)
        
        output = []
        for i in arr2:
            output += [i] * frequencies[i]
            del frequencies[i]

        additional = []
        for i in frequencies:
            print(i)
            additional += [i] * frequencies[i]

        return output + sorted(additional)
