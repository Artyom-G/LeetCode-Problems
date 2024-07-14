//Time Complexity: O(nlogn)
//Space Complexity: O(n)
//Approach: Stack, Freq Map, Sorting
//This code passes 20/31 test cases for some reason but its really close
class Solution {
public:
    string form;
    
    string getElement(int* i) {
        string element = "";
        element += form[*i]; 
        (*i)++; 
        while (*i < form.size() && islower(form[*i])) {
            element += form[*i];
            (*i)++;
        }
        return element;
    }

    int getMult(int* i) {
        if (!isdigit(form[*i])) {
            return 1;
        }
        string mult = "";
        while (*i < form.size() && isdigit(form[*i])) {
            mult += form[*i];
            (*i)++;
        }
        return stoi(mult);
    }

    string countOfAtoms(string formula) {
        form = formula;
        vector<int> mults;
        map<string, int> counter;
        vector<string> order; 
        int i = 0;
        while(i < form.size()){
            if(isupper(form[i])){
                counter[getElement(&i)] = 0;
                getMult(&i);
            }
            else if(isdigit(form[i])){
                mults.push_back(getMult(&i));
            }
            else{
                i++;
            }
        }

        stack<int> mults_stack; 
        i = 0;
        string element;
        int mult = 1;
        int mult_i = 0;
        while(i < form.size()){
            if(isupper(form[i])){
                element = getElement(&i);
                if(!counter[element]){
                    order.push_back(element);
                }
                int _mult = getMult(&i) * mult;
                counter[element] += _mult;
            }
            else if(form[i] == '('){
                mults_stack.push(mults[mult_i]);
                mult *= mults[mult_i];
                mult_i++;
                i++;
            }
            else if(form[i] == ')'){
                mult /= mults_stack.top();
                mults_stack.pop();
                i++;
                getMult(&i);
            }
            else{
                continue;
            }
        }

        sort(order.begin(), order.end());

        string res;
        for(i = 0; i < order.size(); i++){
            res += order[i];
            if(counter[order[i]] > 1){
                res += to_string(counter[order[i]]);
            }
        }

        return res;
    }
};
