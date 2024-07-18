//Time Complexity: O(logn)
//Space Complexity: O(1)
//Approach: Modular Arithmetic
class Solution {
public:
    int hammingWeight(int n) {
        int res = 0;
        while(n > 0){
            if(n % 2 == 1) res++;
            n /= 2;
        }
        return res;
    }
};
