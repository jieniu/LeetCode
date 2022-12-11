// https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int sum = 0;
        int i = 0;
        int result = INT_MAX;
        for (int j = 0; j < nums.size(); j++) {
            sum += nums[j];
            while (sum >= target) {
                int sub = j - i + 1;
                result = result < sub ? result : sub;
                sum -= nums[i];
                i += 1;
            }
        }
        return result == INT_MAX ? 0 : result;
    }
};
