// Time Complexity: O(n^2)
// Space Complexity: O(n)
// Approach: DP

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        int currentLongest = 1;
        for(int i = 1; i < nums.size(); i++){
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j]){
                    dp[i] = max(dp[i], dp[j]+1);
                }
            }
            currentLongest = max(currentLongest, dp[i]);
        }
        return currentLongest;
    }
};
