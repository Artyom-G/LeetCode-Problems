// Time Complexity: O(n)
// Space Complexity: O(n)
// Approach: Hashmap
public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> freq = new Dictionary<int, int>();
        int majorityFreq = nums.Count() / 2;
        for(int i = 0; i < nums.Count(); i++){
            int num = nums[i];
            if(freq.ContainsKey(num)){
                freq[num]++;
            } else{
                freq[num] = 1;
            }
            if(freq[num] > majorityFreq){
                return num;
            }
        }
        return 0;
    }
}
