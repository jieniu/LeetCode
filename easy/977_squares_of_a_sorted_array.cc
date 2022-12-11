// https://leetcode.com/problems/squares-of-a-sorted-array/description/
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> result(nums.size());
        int k = nums.size() - 1;

        for (int i = 0, j = k; i <= j;) {
            if (nums[i] * nums[i] < nums[j] * nums[j]) {
                result[k] = nums[j] * nums[j];
                j--;
                k--;
            } else {
                result[k] = nums[i] * nums[i];
                i++;
                k--;
            }
        }
        return result;
    }
};
