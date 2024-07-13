//Time Complexity: O(n^2)
//Space Complexity: O(n)
//Approach: Math, Stack
class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        vector<tuple<int, int, char>> robots;
        for(int i = 0; i < positions.size(); i++){
            robots.push_back(tuple<int, int, char> {positions[i], healths[i], directions[i]});
        }

        sort(robots.begin(), robots.end());

        while(true){
            vector<tuple<int, int, char>> new_robots;
            char previous = get<2>(robots[0]);
            for(int i = 0; i < robots.size(); i++){
                if(!(get<2>(robots[i]) == 'L' && previous == 'R')){
                    new_robots.push_back(robots[i]);
                }
                else{
                    new_robots.pop_back();
                    if(get<1>(robots[i]) > get<1>(robots[i-1]) && get<1>(robots[i]) > 1){
                        new_robots.push_back(tuple<int, int, char>{get<0>(robots[i]), get<1>(robots[i]) - 1, get<2>(robots[i])});
                    }
                    else if(get<1>(robots[i-1]) > get<1>(robots[i]) && get<1>(robots[i-1]) > 1){
                        new_robots.push_back(tuple<int, int, char>{get<0>(robots[i-1]), get<1>(robots[i-1]) - 1, get<2>(robots[i-1])});
                    }
                }
                previous = get<2>(robots[i]);
            }

            if(robots == new_robots){
                unordered_map<int, int> pos_health;
                vector<int> res;
                for(int i = 0; i < robots.size(); i++){
                    pos_health[get<0>(robots[i])] = i+1;
                }

                for(int i = 0; i < positions.size(); i++){
                    if(pos_health[positions[i]]){
                        res.push_back(get<1>(robots[pos_health[positions[i]]-1]));
                    }
                }
                return res;
            }
            else{
                robots = new_robots;
            }
        }

        return vector<int>{};
    }
};
