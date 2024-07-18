//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Bit Manipulation, XOR
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(int i : nums){
            res ^= i;
        }
        return res;
    }
};
