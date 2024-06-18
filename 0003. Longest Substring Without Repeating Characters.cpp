//Time Complexity: O(n^2)
//Space Complexity: O(n)
//Approach: Sliding Window, Hash
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        int n = s.size();
        int res = 0;

        while (r < n) {
            if (checkSubstring(s, l, r)) {
                res = max(res, r - l + 1);
                r++;
            } else {
                l++;
            }
        }
        return res;
    }

    bool checkSubstring(string s, int left, int right) {
        unordered_set<char> used;
        for (int i = left; i <= right; i++) {
            if (used.find(s[i]) != used.end()) {
                return false;
            }
            used.insert(s[i]);
        }
        return true;
    }
};
