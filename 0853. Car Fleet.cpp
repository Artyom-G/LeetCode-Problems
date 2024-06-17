//Time Complexity: O(nlogn)
//Space Complexity: O(n) because of QuickSort, O(1) otherwise
//Approach: Sorting, Monotonic Stack
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();

        //We are going to sort both pos and speed vectors by the pos
        quickSort(position, speed, 0, n-1);

        stack<float>st;
        for(int i = 0; i < n; i++) {
            float time = (target-position[i]) / ((float) speed[i]);
            while(!st.empty() && time >= st.top()) {
                st.pop();
            }
            st.push(time);
        }
        return st.size();
    }

    //QUICK SORT: GEEK FOR GEEKS
    void swap(int* p1, int* p2)
    {
        int temp;
        temp = *p1;
        *p1 = *p2;
        *p2 = temp;
    }
    int partition(vector<int>& arr, vector<int>& temp, int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j <= high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(&arr[i], &arr[j]);
                swap(&temp[i], &temp[j]);
            }
        }
        swap(&arr[i + 1], &arr[high]);
        swap(&temp[i+1], &temp[high]);
        return (i + 1);
    }

    void quickSort(vector<int>& arr, vector<int>& temp, int low, int high)
    {
        if (low < high) {
            int pi = partition(arr, temp, low, high);
            quickSort(arr, temp, low, pi - 1);
            quickSort(arr, temp, pi + 1, high);
        }
    }
};
