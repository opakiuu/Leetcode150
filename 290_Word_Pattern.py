# 290. Word Pattern
# Easy
# Topics
# premium lock icon
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false


class object:
    def canConstruct(self):
        raise NotImplementedError("no implementation in base class")


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        memo = {}
        record = {}
        ss = s.split()
        for i in range(min(len(pattern),len(ss))):
            if pattern[i] in memo:
                if memo[pattern[i]] != str(ss[i]):
                    return False
            elif str(ss[i]) in record:
                if record[str(ss[i])] != pattern[i]:
                    return False
            memo[pattern[i]] = str(ss[i])
            record[str(ss[i])] = pattern[i]
        return len(pattern)==len(ss)


pattern = "jquery"
s = "jquery"
Solutions = [Solution()]
sol = Solutions[0]

print("pattern => %s\ns => %s\nans => %s" % (pattern, s, sol.wordPattern(pattern, s)))
