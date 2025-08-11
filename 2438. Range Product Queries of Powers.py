# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Bit Manipulation, Prefix Product 
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        cur_power = 1
        while n != 0:
            if n % 2 == 1:
                powers.append(cur_power)
            n = n >> 1
            cur_power *= 2
        
        prefix_prod = [powers[0]]
        for i, num in enumerate(powers[1:]):
            prefix_prod.append(prefix_prod[-1] * num)
        
        res = []
        for q in queries:
            l, r = q[0], q[1]
            if l - 1 >= 0:
                res.append(prefix_prod[r] // prefix_prod[l-1] % 1000000007)
            else:
                res.append(prefix_prod[r] % 1000000007)
        return res
