# 62_Unique_Paths
# Medium
# Topics
# premium lock icon
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


class object:
    def uniquePaths(self, m, n):
        raise NotImplemented("you have to overload")


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.dfs(m, n, 0)

    def dfs(self, m, n, count):
        # exception
        if m == 1 and n == 1:
            return count + 1
        # general
        else:
            if m != 1:
                count = self.dfs(m - 1, n, count)
            if n != 1:
                count = self.dfs(m, n - 1, count)

        return count


class better(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cn = m + n - 2
        total = 1
        for i in range(cn, m - 1, -1):
            total = total * i
        for i in range(n - 1, 0, -1):
            total //= i
        return total


class test(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.ans = []
        part = []
        self.dfs(m, n, 0, part)
        return self.ans

    def dfs(self, m, n, count, part):
        # exception
        if m == 1 and n == 1:
            self.ans.append(part[:])
            return count + 1
        # general
        else:
            if m != 1:
                part.append("down")
                count = self.dfs(m - 1, n, count, part)
                part.pop()
            if n != 1:
                part.append("right")
                count = self.dfs(m, n - 1, count, part)
                part.pop()

        return count


m, n = 3, 2
solutions = [Solution(), better(), test()]
sol = solutions[2]
print(sol.uniquePaths(m, n))
