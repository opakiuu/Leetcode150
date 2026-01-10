#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int far = 0;
        for (int i = 0; i < (int)nums.size(); i++)
        {
            if (i > far)
                return false;
            far = max(far, i + nums[i]);
            cout << far << endl;
            if (far >= (int)nums.size() - 1)
                return true;
        }
        return true;
    }
};

int main(void)
{
    vector<int> nums = {3,2,1,0,4};
    Solution solution;
    cout << solution.canJump(nums);
}