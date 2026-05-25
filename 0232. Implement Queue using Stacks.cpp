// Time Complexity: O(1), O(n), O(n), O(1)
// Space Complexity: O(n)
// Approach: Stack, OOP

class MyQueue {
private:
    vector<int> queue;
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        queue.push_back(x);
    }
    
    int pop() {
        if(queue.empty()){
            return 0; // Change to Exception
        }
        vector<int> temp;
        while(queue.size() > 1){
            temp.push_back(queue.back());
            queue.pop_back();
        }
        int res = queue.back();
        queue.pop_back();
        while(!temp.empty()){
            queue.push_back(temp.back());
            temp.pop_back();
        }
        return res;
    }
    
    int peek() {
        if(queue.empty()){
            return 0; // Change to Exception
        }
        vector<int> temp;
        int res = 0;
        while(!queue.empty()){
            res = queue.back();
            temp.push_back(res);
            queue.pop_back();
        }
        while(!temp.empty()){
            queue.push_back(temp.back());
            temp.pop_back();
        }
        return res;
    }
    
    bool empty() {
        return queue.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
