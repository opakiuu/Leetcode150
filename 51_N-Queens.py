# 51_N-Queens
# Hard
# Topics
# premium lock icon
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]


# Constraints:

# 1 <= n <= 9


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = {}
        memo_xy = {}
        memo_yx = {}
        self.ans = []
        path = [-1] * n
        self.backtracking(path, col, 0, memo_xy, memo_yx, n)
        return self.ans

    def backtracking(self, path, col, row, memo_xy, memo_yx, n):
        # exception
        if row == n:
            part = []
            for i in range(n):
                c = path[i]
                part.append("." * (c) + "Q" + "." * (n - c-1))
            self.ans.append(part)
        # general
        else:
            for c in range(n):
                if c in col or (row + c) in memo_xy or (row - c) in memo_yx:
                    continue
                col[c] = 1
                memo_xy[row + c] = 1
                memo_yx[row - c] = 1
                path[row] = c
                self.backtracking(path, col, row + 1, memo_xy, memo_yx, n)
                del col[c]
                del memo_xy[row + c]
                del memo_yx[row - c]
                path[row] = -1

        # return [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]


n = 4
sol = Solution()
for i in sol.solveNQueens(n):
    print(str(i))
    print("\n")
