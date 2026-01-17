# Code
# Testcase
# Testcase
# Test Result
# 242. Valid Anagram
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class object:
    def isAnagram(self):
        raise NotImplementedError("no implementation in base class")


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ss = sorted(s)
        tt = sorted(t)

        for i in range(min(len(ss), len(tt))):
            if ss[i] != tt[i]:
                return False
        return len(ss) == len(tt)


class clean(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


class less_time_complexity(object):
    def isAnagram(self, s, t):
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        return len(s)==len(t)


s = "ab"
t = "a"
Solutions = [Solution(), clean(), less_time_complexity()]
sol = Solutions[2]

print("pattern => %s\ns => %s\nans => %s" % (s, t, sol.isAnagram(s, t)))
