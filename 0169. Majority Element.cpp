//Time Complexity: O(nlogn)
//Space Complexity: O(n)
//Approach: Sorting
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];  
    }
};
