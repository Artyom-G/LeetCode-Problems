//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Hashmap
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> counter;
        for(char i : s){
            counter[i] += 1;
        }
        
        for(char i : t){
            counter[i] -= 1;
        }

        for (auto& i: counter) {
            if(i.second){
                return false;
            }
        }
        return true;
    }
};
