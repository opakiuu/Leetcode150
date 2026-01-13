class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split()
        return " ".join(s.split()[::-1])
    #"blue is sky the"

s = "the sky is blue"
sol = Solution()
print("%s => %s" %(s,sol.reverseWords(s)))
