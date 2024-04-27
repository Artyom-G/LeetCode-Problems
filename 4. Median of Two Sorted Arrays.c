#Time Complexity: O(log(n+m))
#Space Complexity: O(1)
#Approach: Two Pointers on the Two Arrays
#This almost works but im tired bruh
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int left1 = 0;
    int right1 = nums1Size - 1;
    int left2 = 0;
    int right2 = nums2Size - 1;

    //Edge Cases
    if(nums1Size == 0){
        int medIndex = (nums2Size - 1) / 2;
        if(nums2Size % 2 == 0){
            return (nums2[medIndex] + nums2[medIndex+1]) / 2.0;
        }
        else{ 
            return nums2[medIndex];
        }
    }
    if(nums2Size == 0){
        int medIndex = (nums1Size - 1) / 2;
        if(nums1Size % 2 == 0){
            return (nums1[medIndex] + nums1[medIndex+1]) / 2.0;
        }
        else{ 
            return nums1[medIndex];
        }
    }

    //Two Pointer on both Arrs Method
    int MedMin;
    int MedMax;
    while(left1 + left2 < right1 + right2){
        printf("%d %d %d %d\n", left1, right1, left2, right2);
        if(nums1Size > left1 && nums2Size > left2){
            if(nums1[left1] < nums2[left2]){
                left1++;
                MedMin = nums1[left1];
            }
            else{
                left2++;
                MedMin = nums2[left2];
            }
        }
        else if(nums1Size < left1){
            left2++;
            //MedMin = nums2[left2];
        }
        else{
            left1++;
            //MedMin = nums1[left1];
        }

        if(1 <= right1 && 1 <= right2){
            if(nums1[right1] > nums2[right2]){
                right1--;
                MedMax = nums1[right1];
            }
            else{
                right2--;
                MedMax = nums2[right2];
            }
        }
        else if(1 > right1){
            right2--;
            //MedMax = nums2[right2];
        }
        else{
            right1--;
            //MedMax = nums1[right1];
        }
    }


    //Calculate Med
    int leftMax;
    int rightMin;
    leftMax = nums2[left2] > nums1[left1] ? nums2[left2] : nums1[left1];
    rightMin = nums2[right2] < nums1[right1] ? nums2[right2] : nums1[right1];
    printf("%d %d %d %d\n", left1, right1, left2, right2);
    printf("%d %d %d %d\n", nums1[left1], nums1[right1], nums2[left2], nums2[right2]);
    printf("%d %d \n", MedMax, MedMin);
    return (MedMin + MedMax) / 2.0;
}
