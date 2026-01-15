# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplana c analpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Ans = []
        # for i in s:
        #     if ord("A")<= ord(i)<=ord("Z"):
        #         Ans+=chr(ord(i)+32)
        #     if (ord("a")<= ord(i)<=ord("z"))  or (ord("0")<= ord(i)<=ord("9")):
        #         Ans+=[i]
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        # if str(Ans[0:int(len(Ans)/2+1):1])==str(Ans[len(Ans)-1:int(len(Ans)/2-1):-1]):
        #     return True
        # if Ans[::]==Ans[::-1]:
        #     return True

        # return False

        # n = len(Ans)
        # left = Ans[:n//2]
        # right = Ans[(n+1)//2:][::-1]   # (n+1)//2 會跳過中間那個（奇數長度）
        # return left == right


s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
