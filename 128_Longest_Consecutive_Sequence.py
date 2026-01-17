# 128. Longest Consecutive Sequence
# Medium
# Topics
# premium lock icon
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class object:
    def isAnagram(self):
        raise NotImplementedError("no implementation in base class")


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        numSet = set(nums)

        for n in nums:
            count = 0

            while n in numSet:
                count += 1
                n -= 1
            longest = max(longest, count)
        return longest


# using starting point instead of checking every numbers => causing time complexity as much as O(n^2)
# Time complexity => O(n^2s)
# 起點 n	while 掃描
# 1	1
# 2	2 → 1
# 3	3 → 2 → 1
# 4	4 → 3 → 2 → 1
# 5	5 → 4 → 3 → 2 → 1


class better(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        numSet = set(nums)

        for n in numSet:
            if n - 1 not in numSet:
                cur = n
                count = 1
                while cur + 1 in numSet:
                    count += 1
                    cur += 1
                longest = max(longest, count)
        return longest


nums = [100, 4, 200, 1, 3, 2]
Solutions = [Solution(), better()]
sol = Solutions[1]

print("nums => %s\nans => %s" % (nums, sol.longestConsecutive(nums)))
