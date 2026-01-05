#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

// You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

// Example 1:

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
// Example 2:

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        for (auto n : nums)
        {
            cout << n;
        }
        cout << endl;
        return dp(nums, 0);
    }

private:
    bool dp(vector<int> &nums, int pos)
    {
        // 2,3,1,1,4
        //  exception
        int n = (int)nums.size();
        if (pos >= n - 1)
        {
            return true;
        }
        else if (nums[pos] == 0)
        {
            return false;
        }
        // general
        int far = 0;

        for (int i = 0; i < nums[pos]; i++)
        {
            // cout << i + nums[pos + i] << endl;
            if (pos + i > nums.size() - 1 || pos + i + nums[pos + i] > nums.size() - 1)
            {
                return true;
            }
            far = nums[pos + i] + i;
            // cout << far << endl;
        }
        cout << far << endl;
        // cout << nums[pos + far] << endl;
        return dp(nums, pos + far);
    }
};

int main(void)
{
    vector<int> nums = {5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0};
    Solution solution;
    cout << solution.canJump(nums);
}