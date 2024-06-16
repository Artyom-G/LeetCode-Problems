//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Prefix Max, Suffix Max
class Solution {
public:
    int trap(vector<int>& height) {
        int n = size(height);

        vector<int> left_max;
        int M = 0;
        for(int i : height){
            left_max.push_back(M);
            M = max(i, M);
        }

        vector<int> right_max;
        M = 0;
        for(int i = n-1; i >= 0; i--){
            right_max.push_back(M);
            M = max(height[i], M);
        }

        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += max(0, min(left_max[i], right_max[n-i-1]) - height[i]);
        }
        return sum;      
    }
};
