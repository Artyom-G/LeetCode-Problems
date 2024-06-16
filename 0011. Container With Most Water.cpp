//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Two-Pointer
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = size(height) - 1;
        int max = 0;
        while(l < r){
            if(height[l] <= height[r]){
                if(height[l] * (r - l) > max){
                    max = height[l] * (r - l); 
                }
                l++;
            }
            else{
                if(height[r] * (r - l) > max){
                    max = height[r] * (r - l);
                }
                r--;
            }
        }
        return max;       
    }
};
