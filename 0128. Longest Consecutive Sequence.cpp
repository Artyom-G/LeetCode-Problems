//Time Complexity: O(n^2)
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
