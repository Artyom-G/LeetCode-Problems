//Time Complexity: O(n + m)
//Space Complexity: O(1)
//Approach: Freq Map, Sliding Window
class Solution {
public:
    string minWindow(string s, string t) {
        if(t.size() > s.size()) return "";
        else if(t.size() == s.size() && t == s) return t;

        int L = 0;
        int R = 0;
        int freq[128] = {0};
        int unique = 0;
        for(char i : t){
            if(!freq[i]) unique++;
            freq[i] += 1;
        }
        int count[128] = {0};
        int satisfied = 0;
        int smallest = s.size();
        string res = "";
        int minStart = -1;
        if(freq[s[R]]){
            count[s[R]] += 1;
            if(freq[s[R]] == count[s[R]]) satisfied +=1; 
        }
        while(R < s.size()){
            if(satisfied == unique){
                smallest = R - L + 1;
                minStart = L;
            }

            if(R - L + 1 >= smallest){
                if(freq[s[L]]){
                    count[s[L]] -= 1;
                    if(freq[s[L]] == count[s[L]] + 1) satisfied -=1; 
                }
                L += 1;
            }
            else if(R - L == smallest - 1){
                if(freq[s[L]]){
                    count[s[L]] -= 1;
                    if(freq[s[L]] == count[s[L]] + 1) satisfied -=1; 
                }
                L += 1;
                R+=1;
                if(freq[s[R]]){
                    count[s[R]] += 1;
                    if(freq[s[R]] == count[s[R]]) satisfied +=1; 
                }
            }
            else{
                R+=1;
                if(freq[s[R]]){
                    count[s[R]] += 1;
                    if(freq[s[R]] == count[s[R]]) satisfied +=1; 
                }
            }
            
        }
        if(minStart == -1) return "";
        return s.substr(minStart, smallest);
    }
};
