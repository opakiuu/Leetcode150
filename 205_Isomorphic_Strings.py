# 205. Isomorphic Strings
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true


class object:
    def isIsomorphic(self):
        raise NotImplementedError("Error Implemented")


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if s[i] in s2t:
                if s2t[s[i]] != t[i]:
                    return False
            elif t[i] in t2s:
                return False
            
            s2t[s[i]] = t[i]
            t2s[t[i]] = 1
        return True


s, t = "paper", "title"
Solutions = [Solution()]
sol = Solutions[0]
print(sol.isIsomorphic(s, t))
