class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        word_total = 0
        prompt = []
        ans = []
        space = 0
        Left_more = 0
        Left_more_bool = True
        for i in range(-1, len(words) - 1, 1):
            space += 1
            word_total += len(words[i + 1])
            if i!=-1:
                prompt .append(words[i])
            Left_more_bool = False
            if (word_total + space) < maxWidth:
                continue
            else:
                if (word_total + space) == maxWidth:
                    space -= 1
                    prompt.clear(words[i])
                if space != 0:
                    Left_more += (maxWidth - word_total) % space
                    space = int((maxWidth - word_total) / space)
                for a in prompt:
                    ans += [a]
                    if Left_more_bool:
                        # while Left_more > 0:
                        #     ans += [" "]
                        #     Left_more -= 1
                        # Left_more_bool = False
                        ans.append(" "*Left_more)
                        Left_more_bool = False
                    # for i in range(0, space, 1):
                    #     ans += [" "]
                    ans.append(" "*space)
            prompt.clear()
            space = 0
            Left_more = 0
            Left_more_bool = True
            word_total = 0
        ans+=[words[-1]]
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
