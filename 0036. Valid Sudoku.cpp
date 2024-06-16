//Time Complexity: O(n^2)
//Space Complexity: O(n)
//Approach: Sets, Modular Arithmetic 
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> used_r;
        unordered_set<char> used_c;
        
        for(int r = 0; r < 9; r++) {
            used_r.clear();
            used_c.clear();
            for(int c = 0; c < 9; c++) {
                char ch_r = board[r][c];
                if(ch_r != '.') {
                    if(used_r.count(ch_r) > 0) {
                        return false;
                    }
                    used_r.insert(ch_r);
                }
                
                char ch_c = board[c][r];
                if(ch_c != '.') {
                    if(used_c.count(ch_c) > 0) {
                        return false;
                    }
                    used_c.insert(ch_c);
                }
            }
        }

        unordered_set<char> used_b;
        int r_add, c_add;
        for(int b = 0; b < 9; b++) {
            used_b.clear();
            r_add = b / 3 * 3;
            c_add = b % 3 * 3;
            
            for(int r = 0; r < 3; r++) {
                for(int c = 0; c < 3; c++) {
                    char ch = board[r + r_add][c + c_add];
                    if(ch != '.') {
                        if(used_b.count(ch) > 0) {
                            return false;
                        }
                        used_b.insert(ch);
                    }
                }
            }
        }

        return true;
    }
};
