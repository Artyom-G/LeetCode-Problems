//Time Complexity: O(n)
//Space Complexity: O(n!) 
//Approach: Recursion
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        function<void(int, int, string)> recursion = [&](int open, int close, string combo) {
            if (combo.size() == 2 * n) {
                res.push_back(combo);
                return;
            }
            if (open < n) {
                recursion(open + 1, close, combo + "(");
            }
            if (close < open) {
                recursion(open, close + 1, combo + ")");
            }
        };

        recursion(0, 0, "");
        return res;
    }
};
