class Solution {
    intersection(nums1, nums2) {
        let result = [];
        
        // Convert arrays to sets for faster lookup
        const nums1Set = new Set(nums1);
        const nums2Set = new Set(nums2);
        
        // Iterate over the set of intersecting values
        for (let num of nums1Set) {
            if (nums2Set.has(num)) {
                result.push(num);
            }
        }
        
        return result;
    }
}

const inst = new Solution();
const nums1 = [1,2,2,1];
const nums2 = [2,2];

const result = inst.intersection(nums1, nums2);
console.log(result);
