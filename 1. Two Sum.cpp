//Time Complexity: O(n)
//Space Comlplexity: O(n)
//Approach: Hashmap
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> used;
        for(int i = 0; i < nums.size(); i++){
            used[nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i++){
            int j = target - nums[i];
            if(used.count(j) && used[j] != i){
                return vector<int> {i, used[j]};
            }
        }
        return vector<int> {0, 0};
    }
};

//Time Complexity: O(nlogn)
//Space Comlplexity: O(1) Auxiliry
//Approach: Sort, Two-Pointer
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());

        int left = 0;
        int right = size(nums)-1;
        while(left < right){
            if(nums[left] + nums[right] > target){
                right -= 1;
            }
            else if(nums[left] + nums[right] < target){
                left -= 1;
            }
            else{
                return vector<int> {left, right}; //Oops, find and return original indicies
            }
        }
        return vector<int> {left, right}; //Same thing here
    }
};
