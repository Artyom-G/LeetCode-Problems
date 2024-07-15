//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Math
class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0){
            return 1;
        }
        if(n == 1 || x == 1 || x == 0){
            return x;
        }
        if(x == -1){
            if(n % 2 == 0) return 1;
            else return -1;
        }
        if(n < 0){
            x = 1/x;
            if(n == -2147483648) return 0;
            n *= -1;
        }
        double pow = x;
        int pow_i = 1;
        while(pow_i < n){
            pow *= x;
            pow_i++;
        }
        return pow;
    }
};
