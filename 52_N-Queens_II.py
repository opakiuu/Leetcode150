# 52_N-Queens_II
# Hard
# Topics
# premium lock icon
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.


# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1


# Constraints:

# 1 <= n <= 9


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo_xy = {}
        memo_yx = {}
        column = {}

        return self.dfs(n, 0, memo_xy, memo_yx, column, 0)

    def dfs(self, n, row, memo_xy, memo_yx, column, count):
        # exception
        if row == n:
            return count + 1
        # General

        for i in range(n):
            if i in column or (i + row) in memo_xy or (i - row) in memo_yx:
                continue
            column[i] = 1
            memo_xy[i + row] = 1
            memo_yx[i - row] = 1
            count = self.dfs(n, row + 1, memo_xy, memo_yx, column, count)
            del column[i]
            del memo_xy[i + row]
            del memo_yx[i - row]
        return count

n = 4
sol = Solution()
print(sol.totalNQueens(n))
