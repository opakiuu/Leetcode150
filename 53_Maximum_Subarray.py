# 53_Maximum_Subarray
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        ans = nums[0]
        for i in range(len(nums)):
            total += nums[i]
            ans = max(total, ans)
            if total < 0:
                total = 0

        return ans


nums = [-2, -1]
sol = Solution()
print(sol.maxSubArray(nums))
