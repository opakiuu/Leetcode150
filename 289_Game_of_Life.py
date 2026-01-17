# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.


class Game_of_Life:
    def gameOfLife(self):
        raise NotImplementedError("no implementation in base class")


class Solution(Game_of_Life):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])
        # dead = -1
        # live = 2
        for r in range(ROWS):
            for c in range(COLS):

                lives = self.count_live_neighbors(board, r, c, ROWS, COLS)
                # [0, 1, 0]
                # [0, 0, 1]
                # [1, 1, 1]
                # [0, 0, 0]
                # print("%d " % lives)
                if board[r][c] == 1:
                    # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    # Any live cell with more than three live neighbors dies, as if by over-population.
                    if lives < 2 or lives > 3:
                        board[r][c] = -1
                    # Any live cell with two or three live neighbors lives on to the next generation.
                    # else:
                    #     board[r][c] = 2
                elif board[r][c] == 0:
                    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if lives == 3:
                        board[r][c] = 2
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
        return board

    def count_live_neighbors(self, board, r, c, ROWS, COLS):
        # [0, 1, 0]
        # [0, 0, 1]
        # [1, 1, 1]
        # [0, 0, 0]
        lives = 0
        for y in range(r - 1, r + 2, 1):
            for x in range(c - 1, c + 2, 1):
                if y == r and x == c:
                    continue
                elif 0 <= y < ROWS and 0 <= x < COLS:
                    if abs(board[y][x]) == 1:
                        lives += 1
        return lives


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solutions = [Solution()]
sol = Solutions[0]
print("%s => %s" % (board, sol.gameOfLife(board)))
