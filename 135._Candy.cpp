#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

// There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

// You are giving candies to these children subjected to the following requirements:

// Each child must have at least one candy.
// Children with a higher rating get more candies than their neighbors.
// Return the minimum number of candies you need to have to distribute the candies to the children.

// Example 1:

// Input: ratings = [1,0,2]
// Output: 5
// Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
// Example 2:

// Input: ratings = [1,2,2]
// Output: 4
// Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
// The third child gets 1 candy because it satisfies the above two conditions.

class Solution
{
public:
    int candy(vector<int> &ratings)
    {
        vector<int> result(ratings.size(), 1);
        int ans = 0;
        for (int r = 1; r < ratings.size(); r++)
        {
            if (ratings[r] > ratings[r - 1])
            {
                result[r] = result[r - 1] + 1;
            }
        }

        for (int r = ratings.size() - 2; r >= 0; r--)
        {
            if (ratings[r] > ratings[r + 1] && result[r] <= result[r + 1])
            {
                result[r] = result[r + 1] + 1;
            }
            ans += result[r + 1];
        }
        for (auto r : result)
        {
            cout << r;
        }
        cout << endl;
        ans += result[0];
        return ans;
    }
};

int main(void)
{
    vector<int> ratings = {1, 0, 2};
    // 1 2 3 4 1
    //1 1 2
    Solution solution;
    cout << solution.candy(ratings);
}
