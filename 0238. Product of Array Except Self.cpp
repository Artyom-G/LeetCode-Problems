//Time Complexity: O(n)
//Space Complexity: O(n) with O(1) Extra Space Complexity
//Approach: Prefix-Product, Suffix-Product
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        int n = nums.size();
        
        prefix.push_back(1);
        for(int i = 1; i < n; i++){
            prefix.push_back(prefix[i-1]*nums[i-1]);
        }

        //nums is the suffix
        int previous = nums[n-1];
        nums[n-1] = 1;
        int current;
        for(int i = n-2; i >= 0; i--){
            current = nums[i];
            nums[i] = nums[i+1] * previous;
            previous = current;
        }

        for(int i = 0; i < n; i++){
            prefix[i] *= nums[i];
        }

        return prefix;
    }
};
