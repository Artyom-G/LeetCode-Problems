//Time Complexity: O(n^2) but O(n) on average
//Space Complexity: O(n)
//Approach: Sets
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> used;
        for(int i = 0; i < nums.size(); i++){
            if(!used.count(nums[i])){
                used.insert(nums[i]);
            }
            else{
                return true;
            }
        }
        return false;
    }
};
