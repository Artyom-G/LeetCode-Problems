//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Stack
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;
        int a, b;
        for(string ch : tokens){
            if(ch == "+"){
                a = nums.top();
                nums.pop();
                b = nums.top();
                nums.pop();
                nums.push(a + b);
            }
            else if(ch == "-"){
                a = nums.top();
                nums.pop();
                b = nums.top();
                nums.pop();
                nums.push(b - a);
            }
            else if(ch == "*"){
                a = nums.top();
                nums.pop();
                b = nums.top();
                nums.pop();
                nums.push(a * b);
            }
            else if(ch == "/"){
                a = nums.top();
                nums.pop();
                b = nums.top();
                nums.pop();
                nums.push(b / a);
            }
            else{
                nums.push(stoi(ch));
            }
        }
        return nums.top();
    }
};
