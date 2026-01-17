# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:


# Input: ransomNote = "aa", magazine = "aab"
# Output: true
class object:
    def canConstruct(self):
        raise NotImplementedError("no implementation in base class")


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_sorted = sorted(ransomNote)
        magazine_sorted = sorted(magazine)
        r = 0
        for m in range(len(magazine_sorted)):
            # print("magazine_sorted => %s" % magazine_sorted[m])
            # print("ransomNote => %s " % ransomNote_sorted[r])

            if r == len(ransomNote_sorted):
                return True
            if magazine_sorted[m] == ransomNote_sorted[r]:
                r += 1
        return r == len(ransomNote_sorted)


ransomNote = "aab"
magazine = "baa"
Solutions = [Solution()]
sol = Solutions[0]

print(
    "rasomNote => %s\nmagazine => %s\nans => %s"
    % (ransomNote, magazine, sol.canConstruct(ransomNote, magazine))
)
