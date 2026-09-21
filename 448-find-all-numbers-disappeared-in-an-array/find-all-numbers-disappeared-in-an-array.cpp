class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> ans;

        // Mark numbers that exist
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;

            nums[index] = -abs(nums[index]);
        }

        // Positive values mean the number is missing
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) {
                ans.push_back(i + 1);
            }
        }

        return ans;
    }
};