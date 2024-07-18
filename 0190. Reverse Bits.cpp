//Time Complexity: O(1)
//Space Complexity: O(1)
//Approach: Bit Manipulation
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        long long result = 0;
        for(int i = 0; i < 32; i++){
            long long leastSignificantBit = n & 1;
            n = n >> 1;
            result = result << 1;
            result = result | leastSignificantBit;
        }
        return result;
    }
};
