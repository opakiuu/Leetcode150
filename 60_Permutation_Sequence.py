# 60_Permutation_Sequence
# Hard
# Topics
# premium lock icon
# Companies
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.


# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"
# Example 3:

# Input: n = 3, k = 1
# Output: "123"


# Constraints:


# 1 <= n <= 9
# 1 <= k <= n!
import math


class object:
    def getPermutation(self, n, k):
        raise NotImplemented("you should overide")


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        for i in range(n):
            ans += [i]

        return self.dfs(n, k, ans, 1)

    def dfs(self, n, k, ans, stridx):
        # exception

        # general
        for i in range(stridx, n, 1):
            ans[stridx], ans[i] = ans[i], ans[stridx]
            self.dfs(n, k, ans, stridx + 1)
            ans[stridx], ans[i] = ans[i], ans[stridx]
        return "123"


class better(object):
    def getPermutation(self, n, k):
        f, nums = [1], []
        for i in range(1, n + 1, 1):
            f.append(f[i - 1] * i)
            nums.append(i)
        ans = ""
        for i in range(n - 1, -1, -1):
            idx = (k - 1) // f[i]
            k -= (idx) * f[i]
            ans+= str(nums.pop(idx))

        return ans


n = 4
k = 12
sol = [Solution(), better()]
print(sol[1].getPermutation(n, k))
