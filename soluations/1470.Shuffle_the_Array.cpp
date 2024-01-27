class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
 // Create a vector to store the shuffled result
        vector<int> ans;
 // Iterate over the first 'n' elements of 'nums'
        for ( int i = 0; i<n; ++i){
              // Append the current element of 'nums' to 'ans'
            ans.push_back(nums[i]);
            // Append the corresponding element from the second half of 'nums' to 'ans'
            ans.push_back(nums[i+n]);
        }
        return ans;
        
    }
};