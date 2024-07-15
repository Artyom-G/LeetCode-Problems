//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Array
class Solution {
public:
    int lengthOfLastWord(string s) {
        int L;
        int R;
        bool newWord = true;
        for(int i = 0; i < s.size(); i++){
            if(s[i] != ' '){
                if(newWord) L = i;
                R = i;
                newWord = false;
            }
            else{
                newWord = true;
            }
        }
        return R - L + 1;
    }
};
