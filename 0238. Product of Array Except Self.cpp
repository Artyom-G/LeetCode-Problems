//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Prefix-Product, Suffix-Product
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        vector<int> suffix;
        int n = nums.size();
        
        prefix.push_back(1);
        for(int i = 1; i < n; i++){
            prefix.push_back(prefix[i-1]*nums[i-1]);
        }

        suffix.push_back(1);
        for(int i = 1; i < n; i++){
            suffix.push_back(suffix[i-1]*nums[n-i]);
        }

        for(int i = 0; i < n; i++){
            prefix[i] *= suffix[n-i-1];
        }

        return prefix;
    }
};
