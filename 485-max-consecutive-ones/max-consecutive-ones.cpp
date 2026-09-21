class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int current = 0;
        int maxCount = 0;

        for (int num : nums) {
            if (num == 1) {
                current++;
                maxCount = max(maxCount, current);
            }
            else {
                current = 0;
            }
        }

        return maxCount;
    }
};