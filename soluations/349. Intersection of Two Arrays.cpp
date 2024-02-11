#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        
        // Convert vectors to unordered_set for faster lookup
        unordered_set<int> nums1_set(nums1.begin(), nums1.end());
        unordered_set<int> nums2_set(nums2.begin(), nums2.end());
        
        // Iterate over the set of intersecting values
        for (int num : nums1_set) {
            if (nums2_set.count(num)) {
                result.push_back(num);
            }
        }
        
        return result;
    }
};

int main() {
    Solution inst;
    vector<int> nums1 = {1,2,2,1};
    vector<int> nums2 = {2,2};

    vector<int> result = inst.intersection(nums1, nums2);
    
    for (int num : result) {
        cout << num << " ";
    }
    
    return 0;
}
