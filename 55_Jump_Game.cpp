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
            cout << n;
        cout << endl;
        int cur = 0, pos = 0, far = 0;
        while (1)
        {

            if (pos + far <= nums.size() - 1)
            {
                pos += far;
                cur = nums[pos];
            }
            else
            {
                return true;
            }

            if (cur == 0 && pos <= nums.size() - 1)
            {
                break;
            }
            far = 0;
            for (int i = 0; i <= cur; i++)
            {
                if (pos + i >= nums.size() - 1)
                {
                    return true;
                }
                if (i + nums[pos + i] > far)
                {
                    // cout<<"farfar"<<cur;
                    far = i + nums[pos + i];
                }
                cout << "pos: " << pos << endl;
                cout << "far: " << far << endl;
                cout << "cur_point: " << cur << endl;
            }

            cout << "pos: " << pos << endl;
            cout << "far: " << far << endl;
            cout << "cur_point: " << cur << endl;
        }
        return false;
    }
};

int main(void)
{
    vector<int> nums = {0};
    Solution solution;
    cout << solution.canJump(nums);
}