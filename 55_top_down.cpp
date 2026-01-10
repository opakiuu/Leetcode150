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
// 5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0
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
        for (int i = 1; i <= nums[pos]; i++)
        {
            //cout << "pos+nums[i]" << pos + i << endl;
            if (dp(nums, pos + i))
            {
                return true;
            }
        }
        return false;
    }
};

int main(void)
{
    vector<int> nums = {2,3,1,1,4};
    Solution solution;
    cout << solution.canJump(nums);
}

