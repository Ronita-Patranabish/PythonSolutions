class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long long first = LLONG_MIN;
        long long second = LLONG_MIN;
        long long third = LLONG_MIN;

        for (int num : nums) {

            // Ignore duplicates
            if (num == first || num == second || num == third)
                continue;

            // New maximum
            if (num > first) {
                third = second;
                second = first;
                first = num;
            }

            // New second maximum
            else if (num > second) {
                third = second;
                second = num;
            }

            // New third maximum
            else if (num > third) {
                third = num;
            }
        }

        // If third maximum doesn't exist
        if (third == LLONG_MIN)
            return first;

        return third;
    }
};