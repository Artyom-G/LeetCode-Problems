// Time Complexity: O(n)
// Space Complexity: O(n)
// Approach: Hashmap
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> seen = new Dictionary<int, int>();

        for(int i = 0; i < nums.Count(); i++){
            if(seen.ContainsKey(target - nums[i])){
                return new int[]{seen[target - nums[i]], i};
            } else if(!seen.ContainsKey(nums[i])){
                seen[nums[i]] = i;
            }
        }
        return new int[]{};
    }
}
