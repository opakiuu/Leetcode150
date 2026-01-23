# 209_Minimum_Size_Subarray_Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

# 1,1,1,1,1,|3| 1 1 1 1 1
# R
# L


class object:
    def minSubArrayLen(self, target, nums):
        raise NotImplementedError("You should overide this")


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        Lp = 0
        Total = 0
        Ans = len(nums) + 1
        for Rp in range(len(nums)):
            Total += nums[Rp]
            while Total >= target:
                Ans = min(Ans, Rp - Lp + 1)
                Total -= nums[Lp]
                Lp += 1
        return 0 if Ans == len(nums) + 1 else Ans


nums = [2, 3, 1, 2, 4, 3]
target = 7
Solutions = [Solution()]
sol = Solutions[0]
print(
    "the original is %s \nTarget is %d\nAns is %d\n"
    % (nums, target, sol.minSubArrayLen(target, nums))
)
