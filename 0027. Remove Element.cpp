//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Two-Pointer
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int res = 0;
        int pointer = nums.size() - 1;
        for(int i = 0; i < nums.size(); i++){
            if(i >= pointer){
                if(nums[i] != val){
                    res++;
                }
                break;
            }
            while(pointer >= i && nums[i] == val){
                int temp = nums[i];
                nums[i] = nums[pointer];
                nums[pointer] = temp;
                pointer--;
            }
            if(pointer >= i){
                res++;
            }
        }
        return res;
    }
};
