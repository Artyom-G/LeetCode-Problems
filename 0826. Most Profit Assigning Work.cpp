//Time Complexity: O(n*m)
//Space Complexity: O(n+m) 
//Approach: Sort
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        sort(worker.begin(), worker.end(), greater<int>());

        vector<pair<int, int>> job;
        int job_n = size(profit);

        for(int i = 0; i < job_n; i++){
            job.push_back(pair<int, int>(difficulty[i], profit[i])); 
        }

        sort(job.begin(), job.end(), [](auto &left, auto &right) {
            return left.first < right.first;
        });

        int res = 0;
        int M;
        for(int _worker : worker){
            M = 0;
            for(int i = 0; i < job.size(); i++){
                if(_worker < job[i].first){
                    job.erase(job.begin() + i, job.end());
                    break;
                }
                M = max(M, job[i].second);
            }
            res += M;
        }

        return res;

    }
};
