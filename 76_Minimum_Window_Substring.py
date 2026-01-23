# 76_Minimum_Window_Substring
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

class object:
    def minSubArrayLen(self, target, nums):
        raise NotImplementedError("You should overide this")

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # ADOBECODEBANC
        # ABC
        need = {}
        memo = {}
        t_total = 0
        for t_i in range(len(t)):
            need[t[t_i]] = need.get(t[t_i], 0) + 1
            t_total += 1
        # print(tuple(need))
        Lp = 0
        S_total = 0
        best_l = 0
        best_r = 0
        best_len = len(s) + 1
        for s_i in range(len(s)):
            if s[s_i] in need:
                memo[s[s_i]] = memo.get(s[s_i], 0) + 1
                if memo[s[s_i]] == need[s[s_i]]:
                    S_total += 1

            while S_total == len(need):
                if s_i - Lp + 1 < best_len:
                    best_len = min(best_len, s_i - Lp + 1)
                    best_l, best_r = Lp, s_i
                if s[Lp] in memo:
                    memo[s[Lp]] -= 1
                    if memo[s[Lp]] < need[s[Lp]]:
                        S_total -= 1
                Lp += 1
        return "" if best_len == len(s) + 1 else s[best_l : best_r + 1]


s = "a"
t = "aa"
Solutions = [Solution()]
sol = Solutions[0]
print("the original is %s \nTarget is %s\nAns is %s\n" % (s, t, sol.minWindow(s, t)))
