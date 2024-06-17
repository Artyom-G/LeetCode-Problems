//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Two Sum, Two-Pointer
class Solution {
public:
    bool judgeSquareSum(int c) {
        int a = 0;
        int b = int(sqrt(c));
        int a_square = 0;
        int b_square = b*b;
        while(a<=b){
            if(a_square < c - b_square){
                a++;
                a_square = a*a;
            }
            else if(a_square > c - b_square){
                b--;
                b_square = b*b;
            }
            else{
                return true;
            }
        }
        return false;
    }
};
