//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Index Stack
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> indexStack;
        int n = temperatures.size();
        vector<int> res(n, 0);
        for(int i = 0; i < n; i++){
            while(!indexStack.empty() && temperatures[i] > temperatures[indexStack.top()]){
                int idx = indexStack.top();
                res[idx] = i - idx;
                indexStack.pop();
            }
            indexStack.push(i);
        }
        return res;
    }
};
