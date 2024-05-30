#Time Complextity: O(n^2)
#Space Complextity: O(n)
#Approach: 
#We will use these mathematical properties:
#XOR is associative
#if a = b then a ^ b = 0
#Make a cummutative xor array
#Every pairs that are equal in the cummutative array are guarenteed to have all solutions no matter where the middle index is placed
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        def cummutative_xor(arr):
            output = [0] * (len(arr) + 1)
            for i in range(len(arr)):
                output[i + 1] = output[i] ^ arr[i]
            return output
        
        counter = 0
        cum_xor = cummutative_xor(arr)

        for i in range(0, len(arr)):
            for k in range(i + 1, len(arr)):
                if cum_xor[i] == cum_xor[k+1]:
                    counter += (k-i)
        
        return counter

