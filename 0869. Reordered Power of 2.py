# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Maps
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        two_powers = [1]
        while two_powers[-1] < 1000000000:
            two_powers.append(two_powers[-1] * 2)
            two_powers[-2] = str(two_powers[-2])
        two_powers[-1] = str(two_powers[-1])
        
        n = str(n)
        count_digits_n = dict()
        for c in n:
            if c in count_digits_n:
                count_digits_n[c] += 1
            else: count_digits_n[c] = 1

        for num in two_powers:
            if len(num) == len(n):
                count_digits = dict()
                for c in num:
                    if c in count_digits:
                        count_digits[c] += 1
                    else: count_digits[c] = 1

                if count_digits.items() == count_digits_n.items():
                    return True
        return False
            
