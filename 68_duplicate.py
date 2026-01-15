class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        total_chars = 0
        prompt = []
        ans = []
        space = 0
        Left_more = 0
        i = 0
        while i < len(words):
            if (total_chars + len(words[i]) + space + 1) < maxWidth:
                total_chars += len(words[i])
                space += 1
                prompt.append(words[i])
                i += 1
                continue

            else:
                if space != 0:
                    Left_more += (maxWidth - total_chars) % space
                    space = int((maxWidth - total_chars) / space)
                for a in prompt:
                    ans += [a]
                    if Left_more>0:
                        ans+=" "
                        Left_more-=1
                    # for i in range(0, space, 1):
                    #     ans += [" "]
                    ans+=" " * space
            prompt.clear()
            space = 0
            Left_more = 0
            total_chars = 0
            # i+=1
        # if i 
        ans += [words[-1]]
        # return ["This    is    an", "example  of text", "justification.  "]
        return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
sol = Solution()
print("%s => " % (words))
for i in sol.fullJustify(words, maxWidth):
    print("%s" % (i))


# // wl + Space + w2 + space ... + space .-
# // mex Width

# // Otheraise :
# // GAP           //Gap
# // totol Chos: Wordl + space + word2 + space + word 3
# //                4      1       2        1      2
# // (maxWidth - total Chors ) / gaps
# // SPACES (17 - 10 ) / 2 = 3
# // rest : (17-10) % 2 = | the first gap has 3+1 spaces
# // Some gaps may have 1) more space than others
# // at most
