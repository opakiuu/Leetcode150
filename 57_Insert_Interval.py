# 57_Insert_Interval
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.


# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105
class object:
    def minSubArrayLen(self, target, nums):
        raise NotImplementedError("You should overide this")

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        return self.binary_search(intervals, newInterval, len(intervals) // 2)

    def binary_search(self, intervals, newInterval, middle):
        # exception
        if intervals[middle][0] <= newInterval[0][0] <= intervals[middle][1]:
            index = middle
            ans = []
            for i in range(middle):
                ans += [intervals[i]]
            while intervals[index][0] < newInterval[1]:
                index += 1
            if newInterval[1] == intervals[index + 1][0]:
                intervals[middle][1] = intervals[index + 1][1]
            elif newInterval[1] < intervals[index + 1][0]:
                intervals[middle][1] = newInterval[1]
            ans += [intervals[middle]]
            for i in range(index + 1, len(intervals), 1):
                ans += [intervals[i]]
            return ans
        # general
        if intervals[middle][0] < newInterval[0][0]:
            middle = len(intervals) - (len(intervals) - middle) // 2
            return self.insert(intervals, newInterval, middle)
        else:
            middle = middle // 2
            return self.insert(intervals, newInterval, middle)


class better(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval
        res = []
        index = 0
        while index < len(intervals) and intervals[index][1] < s:
            res.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index][0] <= e:
            s = min(s, intervals[index][0])
            e = max(e, intervals[index][1])
            index += 1
        res.append([s, e])
        while index < len(intervals):
            res.append(intervals[index])
            index += 1
        return res


intervals = [[1, 5]]
newInterval = [5, 7]
Solutions = [Solution(), better()]
sol = Solutions[1]
print(
    "the original is %s \nTarget is %s\nAns is %s\n"
    % (intervals, newInterval, sol.insert(intervals, newInterval))
)
