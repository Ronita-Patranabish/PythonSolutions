class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        
        // Store frequency of each element
        int freq[1001] = {0};

        for (int num : arr1) {
            freq[num]++;
        }

        vector<int> ans;

        // Add elements according to arr2 order
        for (int num : arr2) {
            while (freq[num] > 0) {
                ans.push_back(num);
                freq[num]--;
            }
        }

        // Add remaining elements in ascending order
        for (int num = 0; num <= 1000; num++) {
            while (freq[num] > 0) {
                ans.push_back(num);
                freq[num]--;
            }
        }

        return ans;
    }
};