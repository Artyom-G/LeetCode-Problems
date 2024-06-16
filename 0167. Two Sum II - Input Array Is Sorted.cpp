//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Two Pointer
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = size(numbers) - 1;
        vector<int> res;
        while(l < r){
            if(numbers[l] + numbers[r] < target){
                l++;
            }
            else if(numbers[l] + numbers[r] > target){
                r--;
            }
            else{
                res.push_back(l+1);
                res.push_back(r+1);
                return res;
            }
        }
        res.push_back(l+1);
        res.push_back(r+1);
        return res;
    }
};
