# 56. Merge Intervals
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.


# Constraints:


# 1 <= intervals.length <= 104
# intervals[i].length == 2
class object:
    def merge(seld):
        raise NotImplementedError("please overide")

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        result = []
        index = 0
        for i in range(len(intervals_sorted)):
            # print(intervals_sorted[i])
            if index > 0 and intervals_sorted[i][0] <= result[index - 1][1]:
                # print(result[index-1])
                result[index - 1][1] = max(result[index - 1][1], intervals_sorted[i][1])
                continue
            result.append(intervals_sorted[i])
            index += 1
            print(result[index - 1])
        return result

class Better(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        output = [intervals_sorted[0]]
        for start, end in intervals_sorted[1:]:
            lastEnd = output[-1][1]
            # print(intervals_sorted[i])
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
Solutions = [Solution(), Better()]
sol = Solutions[0]
print("%s => %s" % (intervals, sol.merge(intervals)))

