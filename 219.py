# 219. Contains Duplicate II
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


# Constraints:


# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105
class object:
    def containsNearbyDuplicate(self):
        raise NotImplementedError("no implementation in base class")


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        memo = {}
        for i in range(len(nums)):
            if nums[i] in memo and i - memo[nums[i]] <= k:
                return True
            memo[nums[i]] = i
        return False


class Hashset(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L>k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
Solutions = [Solution()]
sol = Solutions[0]
print("nums is %s\nk is %s\n=> %s" % (nums, k, sol.containsNearbyDuplicate(nums, k)))
