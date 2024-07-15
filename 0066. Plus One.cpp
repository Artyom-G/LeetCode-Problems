//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Array, Math
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() - 1;
        for(int i = n; i >= 0; i--){
            if(digits[i] == 9){
                digits[i] = 0;
            }
            else{
                digits[i]++;
                return digits;
            }
        }
        digits.push_back(0);
        digits[0] = 1;
        return digits;
    }
};
