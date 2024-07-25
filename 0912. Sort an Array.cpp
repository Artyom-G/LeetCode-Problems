class Solution {
public:
    void merge(vector<int>& array, int const left, int const mid,
            int const right)
    {
        int const subArrayOne = mid - left + 1;
        int const subArrayTwo = right - mid;

        auto *leftArray = new int[subArrayOne],
            *rightArray = new int[subArrayTwo];

        for (auto i = 0; i < subArrayOne; i++)
            leftArray[i] = array[left + i];
        for (auto j = 0; j < subArrayTwo; j++)
            rightArray[j] = array[mid + 1 + j];

        auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0;
        int indexOfMergedArray = left;

        while (indexOfSubArrayOne < subArrayOne
            && indexOfSubArrayTwo < subArrayTwo) {
            if (leftArray[indexOfSubArrayOne]
                <= rightArray[indexOfSubArrayTwo]) {
                array[indexOfMergedArray]
                    = leftArray[indexOfSubArrayOne];
                indexOfSubArrayOne++;
            }
            else {
                array[indexOfMergedArray]
                    = rightArray[indexOfSubArrayTwo];
                indexOfSubArrayTwo++;
            }
            indexOfMergedArray++;
        }

        while (indexOfSubArrayOne < subArrayOne) {
            array[indexOfMergedArray]
                = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
            indexOfMergedArray++;
        }

        while (indexOfSubArrayTwo < subArrayTwo) {
            array[indexOfMergedArray]
                = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
            indexOfMergedArray++;
        }
        delete[] leftArray;
        delete[] rightArray;
    }

    void mergeSort(vector<int>& array, int const begin, int const end)
    {
        if (begin >= end)
            return;

        int mid = begin + (end - begin) / 2;
        mergeSort(array, begin, mid);
        mergeSort(array, mid + 1, end);
        merge(array, begin, mid, end);
    }
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size()-1);
        return nums;
    }
};
