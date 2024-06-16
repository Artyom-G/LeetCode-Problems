//Time Complexity: O(nlogn)
//Space Complexity: O(n)
//Approach: Sort
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<int> res(k, 0);
        vector<int> freq(k, 0);
        int cur_freq = 0;
        int cur_num = nums[0];
        int j = 0;
        for(int i : nums){
            if(cur_num != i){
                cur_num = i;
                cur_freq = 1;
                j = 0;
            }
            else{
                cur_freq++;
            }

            //Swapping elements in the mode vector to make sure its sorted, will run only once unless its the first time looping and all elements are 0.
            while(j < k && (cur_freq > freq[j] || (j+1 < k && cur_freq > freq[j+1]))){
                
                freq[j] = cur_freq;
                res[j] = cur_num;

                if(j+1 < k && freq[j] > freq[j+1]){
                    int temp = freq[j+1];
                    freq[j+1] = freq[j];
                    freq[j] = temp;
                    temp = res[j+1];
                    res[j+1] = res[j];
                    res[j] = temp; 
                    j++;
                }
            }
        }
        return res;
    }
};
