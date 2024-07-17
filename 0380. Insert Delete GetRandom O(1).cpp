//Time Complexity: O(1)
//Space Complexity: O(n)
//Approach: Index Map, List
class RandomizedSet {
public:
    unordered_map<int, int> index_map;
    vector<int> list;

    RandomizedSet() {
    }
    
    bool insert(int val) {
        if(index_map[val] == 0){
            list.push_back(val);
            index_map[val] = list.size();
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if(index_map[val] > 0){
            list[index_map[val]-1] = list[list.size()-1];
            index_map[list[list.size()-1]] = index_map[val];
            list.pop_back();
            index_map[val] = 0;
            return true;
        }
        return false;
    }
    
    int getRandom() {
        return list[rand()%list.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
