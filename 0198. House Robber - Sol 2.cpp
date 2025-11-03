// Time Complexity: O(n)
// Space Complexity: O(n)
// Approach: DP

class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 1) return max(0, nums[0]);
        else if(nums.size()==2) return max(0, max(nums[1], nums[0]));
        vector<int> dp(nums.size(), 0);
        dp[0] = max(0, nums[0]);
        dp[1] = max(0, nums[1]);
        dp[2] = max(nums[1], nums[0] + nums[2]);
        for(int i = 3; i < nums.size(); i++){
            dp[i] = max(dp[i-1], max(dp[i-2]+nums[i], dp[i-3]+nums[i]));
        }
        return dp[nums.size()-1];
    }
};
