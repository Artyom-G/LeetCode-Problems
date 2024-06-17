//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Index Stack
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> indexStack;
        int n = heights.size();
        int res = 0;

        for (int i = 0; i < n; ++i) {
            while (!indexStack.empty() && heights[i] < heights[indexStack.top()]) {
                int topIndex = indexStack.top();
                indexStack.pop();
                int height = heights[topIndex];
                int width = indexStack.empty() ? i : i - indexStack.top() - 1;
                res = max(res, height * width);
            }
            indexStack.push(i);
        }

        while (!indexStack.empty()) {
            int topIndex = indexStack.top();
            indexStack.pop();
            int height = heights[topIndex];
            int width = indexStack.empty() ? n : n - indexStack.top() - 1;
            res = max(res, height * width);
        }

        return res;
    }
};
