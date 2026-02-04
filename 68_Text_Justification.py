class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        len_total = 0
        ans = []
        index = 0
        for w in range(0, len(words), 1):
            part = []
            if len_total + len(words[w]) + (w - index) - 1 < maxWidth:
                len_total += len(words[w])
            else:
                if w - index - 1 > 0:
                    gap = (maxWidth - len_total) // (w - index - 1)
                    extra = (maxWidth - len_total) % (w - index - 1)
                    for k in range(index, w - 1, 1):
                        part.append("".join(words[k]))
                        part.append(" " * (gap + (1 if k - index < extra else 0)))
                    part.append("".join(words[w - 1]))
                else:
                    part.append("".join(words[index:w]))
                    part.append(" " * (maxWidth - len_total))

                ans.append("".join(part))
                index = w
                len_total = len(words[w])
        ans.append(" ".join(words[index:]))
        ans[-1] += " " * (maxWidth - (len(ans[-1])))
        return ans


words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth = 20
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
