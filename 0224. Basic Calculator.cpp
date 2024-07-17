//Time Complexity: O(n)
//Space Complexity: O(n)
//Approach: Stacks
class Solution {
public:
    string form;

    void evaluateTop(stack<int>& nums, stack<char>& ops) {
        int b = nums.top();
        nums.pop();
        int a = nums.top();
        nums.pop();
        char op = ops.top();
        ops.pop();
        nums.push(applyOp(a, b, op));
    }

    int applyOp(int a, int b, char op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            default: return 0;  
        }
    }

    int precedence(char op) {
        if (op == '+' || op == '-') return 1;
        if (op == '(') return 0;
        return -1; 
    }
    int getInt(int& i) {
        string num = "";
        while (i < form.size() && isdigit(form[i])) {
            num += form[i];
            i++;
        }
        return stoi(num);
    }

    int calculate(string s) {
        s.erase(remove(s.begin(), s.end(), ' '), s.end());
        form = s;
        stack<int> nums;
        stack<char> ops;
        int i = 0;
        nums.push(0); 

        while (i < form.size()) {
            if (isdigit(form[i])) {
                nums.push(getInt(i));
            } else if (form[i] == '(') {
                ops.push(form[i]);
                i++;
            } else if (form[i] == ')') {
                while (ops.top() != '(') {
                    evaluateTop(nums, ops);
                }
                ops.pop(); 
                i++;
            } else { 
                if (form[i] == '-' && (i == 0 || form[i-1] == '(' || form[i-1] == '+' || form[i-1] == '-')) {
                    nums.push(0);
                }
                while (!ops.empty() && precedence(ops.top()) >= precedence(form[i])) {
                    evaluateTop(nums, ops);
                }
                ops.push(form[i]);
                i++;
            }
        }

        while (!ops.empty()) {
            evaluateTop(nums, ops);
        }

        return nums.top();
    }
};
