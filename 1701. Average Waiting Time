//Time Complexity: O(n)
//Space Complexity: O(1)
//Approach: Array
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        int n = customers.size();
        double totalWaitTime = 0;
        int currentTime = customers[0][0]; 
        for (const auto& customer : customers) {
            int arrivalTime = customer[0];
            int cookingTime = customer[1];
            int startTime = max(currentTime, arrivalTime);
            int finishTime = startTime + cookingTime;
            totalWaitTime += finishTime - arrivalTime;
            currentTime = finishTime;
        }

        return totalWaitTime / n;
    }
};
