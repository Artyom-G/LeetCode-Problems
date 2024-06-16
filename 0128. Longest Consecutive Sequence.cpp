//Time Complexity: O(n^2) but O(n) on average
//Space Complexity: O(n)
//Approach: Hashmaps, Sets
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> map;
        unordered_set<int> set;
        for(int num : nums){
            set.insert(num);
        }
        int res = 0;
        int x;
        int y;
        int seq;
        for(int num : set){
            x = map[num-1];
            y = map[num+1];
            seq = x + y + 1;
            map[num-x] = seq;
            map[num+y] = seq;
            if(res < seq){
                res = seq;
            }
        }
        return res;
    }
};


//Time Complexity: O(n^3) but O(n) on average
//Space Complexity: O(n)
//Approach: Hashmaps
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, bool> map;
        for(int i = 0; i<nums.size(); i++){
            map[nums[i]] = true;
        }
        for(int i=0; i<nums.size(); i++){
            if(map.count(nums[i]-1) > 0){
                map[nums[i]] = false;
            }
        }
        int maxlen = 0;
        for(int i=0; i<nums.size(); i++){
            if(map[nums[i]] == true){
                int j=0; int count=0;
                while(map.count(nums[i]+j) > 0){
                    j++;
                    count++;
                }
                if(count>maxlen){
                    maxlen = count;
                }
            }
        }
        return maxlen;
    }
};


//Time Complexity: O(n^3) but O(n) on average
//Space Complexity: O(n)
//Approach: Sets, Hashmaps
//Time Limit Exceeded
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> used;
        for(int i : nums){
            used.insert(i);
        }

        int j = 0;
        int longest_seq = 0;
        int seq = 1;
        unordered_map<int, int> seqs;
        for(int i : used){
            seq = 1;
            j = i + 1;
            while(used.count(j) > 0){
                if(seqs.count(j) > 0){
                    seq += seqs[j];
                    int _seq = seqs[j];
                    while(j > i + 1){
                        seqs[j] = _seq;
                        _seq-=1000;
                        j-=1000;
                    }
                    break;
                }
                j++;
                seq++;
            }
            seqs[i] = seq;
            if(seq > longest_seq){
                longest_seq = seq;
            }
        }
        return longest_seq;
    }
};
