# 11. Container With Most Water
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height) - 1
        maxTotal = 0
        while L < R:
            lowest = min(height[L], height[R])
            maxTotal = max(lowest * (R - L), maxTotal)
            if height[R] > height[L]:
                L += 1
            else:
                R -= 1

        return maxTotal


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# -1 -1 0 1
sol = Solution()
print("%s => " % str(height))
print("%d" % sol.maxArea(height))
