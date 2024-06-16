//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Two-Pointers
//Move the pointer with the smaller height
int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize-1;

    int max = 0;
    int minHeight;
    int curHeight;
    while(left < right){
        if(height[left] <= height[right]){
            minHeight = height[left];
        }
        else{
            minHeight = height[right];
        }

        curHeight = minHeight * (right - left);
        if(max < curHeight){
            max = curHeight;
        }

        if(height[left] <= height[right]){
            left++;
        }
        else{
            right--;
        }
    }
    return max;
}
