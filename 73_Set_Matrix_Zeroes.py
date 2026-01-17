# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.


# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


class object:
    def setZeroes(self,):
        raise NotImplementedError("no implementation in base class")


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] == 0:
                    for tmp_x in range(cols):
                        memo[(y, tmp_x)] = 0
                    for tmp_y in range(rows):
                        memo[(tmp_y, x)] = 0
        for y in range(rows):
            for x in range(cols):
                if (y, x) not in memo:
                    memo[(y, x)] = matrix[y][x]
        result = []
        for y in range(rows):
            prompt = []
            for x in range(cols):
                prompt += [memo[(y, x)]]
            result += [prompt]
        return result

    # [1,1,1]
    # [1,0,1]
    # [1,1,1]

    # [1,0,1]
    # [0,0,0]
    # [1,0,1]


class O_m_plus_n(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rows_record = [1] * rows
        cols_record = [1] * cols
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] == 0:
                    cols_record[x] = 0
                    rows_record[y] = 0

        for y in range(rows):
            for x in range(cols):
                if rows_record[y] == 0 or cols_record[x] == 0:
                    matrix[y][x] = 0
        return matrix

    #  [ ,f, ]
    #  [1,1,1]
    # f[1,0,1]
    #  [1,1,1]

    # [1,0,1]
    # [0,0,0]
    # [1,0,1]


class O_one(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[y][0] == 0 for y in range(rows))
        first_cols_zero = any(matrix[0][x] == 0 for x in range(cols))
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0

        for y in range(1,rows):
            for x in range(1,cols):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0
        if first_row_zero:
            for y in range(rows):
                matrix[y][0] = 0
        if first_cols_zero:
            for x in range(cols):
                matrix[0][x] = 0
        return matrix


# ---------------------------main--------------------------------------
matrix = [[0, 1]]
Solutions = [Solution(), O_m_plus_n(), O_one()]
sol = Solutions[2]
print(matrix)
print(sol.setZeroes(matrix))
