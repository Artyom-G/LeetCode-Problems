//Time Complexity: O(nlogn)
//Space Complexity: O(n)
//Approach: Sort and Two-Pointer

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void swap(int* p1, int* p2);
int partition(int arr[], int* temp, int low, int high);
void quickSort(int arr[], int* temp, int low, int high);

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* indicies = malloc(sizeof(int) * (*returnSize));
    indicies[0] = 0;
    indicies[1] = numsSize - 1;

    int* temp = malloc(sizeof(int) * (numsSize));
    for(int i = 0; i < numsSize; i++){
        temp[i] = i;
    }

    quickSort(nums, temp, indicies[0], indicies[1]);

    while(indicies[0] < indicies[1]){
        if(nums[indicies[0]] == target - nums[indicies[1]]){
            indicies[0] = temp[indicies[0]];
            indicies[1] = temp[indicies[1]];
            free(temp);
            return indicies;
        }
        else if(target < nums[indicies[0]] + nums[indicies[1]]){
            indicies[1]--;
        }
        else{
            indicies[0]++;
        }
    }
    free(temp);
    return indicies;
}




//QUICK SORT: GEEK FOR GEEKS
void swap(int* p1, int* p2)
{
    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}
int partition(int arr[], int* temp, int low, int high)
{
    // choose the pivot
    int pivot = arr[high];

    // Index of smaller element and Indicate
    // the right position of pivot found so far
    int i = (low - 1);

    for (int j = low; j <= high; j++) {
        // If current element is smaller than the pivot
        if (arr[j] < pivot) {
            // Increment index of smaller element
            i++;
            swap(&arr[i], &arr[j]);
            swap(&temp[i], &temp[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    swap(&temp[i+1], &temp[high]);
    return (i + 1);
}

// The Quicksort function Implement

void quickSort(int arr[], int* temp, int low, int high)
{
    // when low is less than high
    if (low < high) {
        // pi is the partition return index of pivot

        int pi = partition(arr, temp, low, high);

        // Recursion Call
        // smaller element than pivot goes left and
        // higher element goes right
        quickSort(arr, temp, low, pi - 1);
        quickSort(arr, temp, pi + 1, high);
    }
}
