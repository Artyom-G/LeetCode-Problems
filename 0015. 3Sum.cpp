//Time Complexity: O(n^2)
//Space Complexity: O(n!) but O(1) Extra Space
//Approach: Two Sum, Two Pointer, Fixed Index
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = size(nums);
        int j;
        int k;
        vector<vector<int>> res;
        for(int i = 0; i < n-2; i++){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            j = i + 1;
            k = n - 1;
            while(j < k){
                if(nums[j] + nums[k] < -nums[i]){
                    j++;
                }
                else if(nums[j] + nums[k] > -nums[i]){
                    k--;
                }
                else{
                    res.push_back({nums[i], nums[j], nums[k]});
                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;
                    j++;
                    k--;
                }
            }
        }
        return res;
    }
};
