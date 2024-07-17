//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Stacks
class Solution {
public:
    string s;
    string getFolderName(int* i){
        string name = "";
        while(*i < s.size() && s[*i] != '/'){
            name.push_back(s[*i]);
            (*i)++;
        }
        return name;
    }
    void getSlashes(int* i){
        while(*i < s.size() && s[*i] == '/'){
            (*i)++;
        }
    }
    string simplifyPath(string path) {
        s = path;
        vector<string> dirs;

        int i = 0;
        string dir;
        while(i < s.size()){
            getSlashes(&i);
            if(i < s.size()) dir = getFolderName(&i);
            else break;
            if(dir == "."){
                continue;
            }
            else if(dir == ".."){
                if(dirs.size() > 0) dirs.pop_back();
            }
            else{
                dirs.push_back(dir);
            }
        }

        if(dirs.size() == 0) return "/";

        string res = "";
        for(string dir : dirs){
            res += '/';
            res += dir;
        }
        return res;
    }
};
