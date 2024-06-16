//Time Complexity: O(1)
//Space Complexity: O(n)
//Approach: Prefix Min, Stacks
class MinStack {
public:
    int t;
    vector<int> stack;
    vector<int> mins;
    MinStack() {
        t = -1;
    }
    
    void push(int val) {
        stack.push_back(val);
        if(t >= 0) mins.push_back(min(val, mins[t]));
        else mins.push_back(val);
        t++;
    }
    
    void pop() {
        stack.erase(stack.begin() + t);
        mins.erase(mins.begin() + t);
        t--;
    }
    
    int top() {
        return stack[t];
    }
    
    int getMin() {
        return mins[t];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
