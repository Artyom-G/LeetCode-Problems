//Time Complexity: O(n + m)
//Space Complexity: O(n + m)
//Approach: Freq Map, Sliding Window
//Test Case 266/268: Memory Limit Exceeded
class Solution {
public:
    string minWindow(string s, string t) {
        if(t.size() > s.size()) return "";
        else if(t.size() == s.size() && t == s) return t;

        int L = 0;
        int R = 0;
        map<char, int> freq;
        int unique = 0;
        for(char i : t){
            if(!freq[i]) unique++;
            freq[i] += 1;
        }
        map<char, int> count;
        int satisfied = 0;
        int smallest = s.size();
        string res = "";
        if(freq[s[R]]){
            count[s[R]] += 1;
            if(freq[s[R]] == count[s[R]]) satisfied +=1; 
        }
        while(R < s.size()){
            //cout << L << " " << R << " " << satisfied << " " << unique << "\n";
            if(satisfied == unique){
                smallest = R - L + 1;
                res = s.substr(L, smallest);
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
        return res;
    }
};
