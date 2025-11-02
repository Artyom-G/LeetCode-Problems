// Time Complexity: O(n^2)
// Space Complexity: O(n)
// Approach: DP

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        int n = s.size();
        vector<bool> dp(n+1, false);
        dp[0] = true;

        for(int i = 1; i <= n; i++){
            for(int j = 0; j < i; j++){
                if(dp[j] && wordSet.find(s.substr(j, i-j)) != wordSet.end()){
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
};
