#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = (int)nums.size();
        memo.assign(n, -1); // -1 unknown, 0 false, 1 true
        return dfs(nums, 0);
    }

private:
    vector<int> memo;

    bool dfs(vector<int>& nums, int pos) {
        int n = (int)nums.size();
        if (pos >= n - 1) return true;
        if (memo[pos] != -1) return memo[pos];

        int step = nums[pos];
        for (int j = 1; j <= step; j++) {
            int nxt = pos + j;
            if (nxt >= n) return memo[pos] = 1;
            if (dfs(nums, nxt)) return memo[pos] = 1;
        }
        return memo[pos] = 0;
    }
};

int main(void)
{
    vector<int> nums = {2,3,1,1,4};
    Solution solution;
    cout << solution.canJump(nums);
}

