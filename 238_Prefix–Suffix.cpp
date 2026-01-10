#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

// Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
// Example 2:

// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> ans;
        int total = 1;
        for (auto n : nums)
        {
            ans.push_back(total);
            total *= n;
        }

        total = 1;
        for (int n = nums.size() - 1; n >= 0; n--)
        {
            ans[n] *= total;
            total *= nums[n];
        }
        return ans;
    }
};

int main(void)
{
    vector<int> nums = {1, 2, 3, 4};

    //[1, 1, 2,6]
    //[24,12,4,1]

    // 1,2,3,4
    //[1    ,1*1  ,1*2  ,1*2*3]
    //[4*3*2,4*3  ,4*1  ,1]
    Solution solution;
    for (auto ans : solution.productExceptSelf(nums))
    {
        cout << ans << " ";
    }
}
