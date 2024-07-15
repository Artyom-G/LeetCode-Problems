//Time Complexity: O(logn)
//Space Complexity: O(1)
//Approach: Binary Search, Math
class Solution {
public:
    int mySqrt(int x) {
        int H = 46340; // sqrt(2147483647)
        int L = 0;
        int M = (H + L) / 2;
        while(L <= H){
            if(M * M > x){
                H = M - 1;
            }
            else{
                L = M + 1;
            }
            M = (H + L) / 2;
        }
        return M;
    }
};
