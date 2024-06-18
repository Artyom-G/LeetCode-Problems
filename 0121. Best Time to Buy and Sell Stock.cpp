//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Prefix Min and Suffix Max
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();

        vector<int> minPref;
        int M = 2147483647;
        for(int i : prices){
            M = min(i, M);
            minPref.push_back(M);
        }
        
        vector<int> maxSuf;
        M = 0;
        for(int i = 0; i < n; i++){
            M = max(prices[n-i-1], M);
            maxSuf.push_back(M);
        }

        int res = 0;
        for(int i = 0; i < n; i++){
            res = max(maxSuf[n-i-1] - minPref[i], res);
        }
        return res;
    }
};
