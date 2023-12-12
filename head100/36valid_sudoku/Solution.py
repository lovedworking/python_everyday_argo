# <p>Determine if a&nbsp;<code>9 x 9</code> Sudoku board&nbsp;is valid.&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:</p>
#
# <ol>
#  <li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.</li>
#  <li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
#  <li>Each of the nine&nbsp;<code>3 x 3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
# </ol>
#
# <p><strong>Note:</strong></p>
#
# <ul>
#  <li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
#  <li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.</li>
# </ul>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" />
# <pre>
# <strong>Input:</strong> board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# <strong>Output:</strong> true
# </pre>
#
# <p><strong class="example">Example 2:</strong></p>
#
# <pre>
# <strong>Input:</strong> board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# <strong>Output:</strong> false
# <strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being modified to <strong>8</strong>. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# </pre>
#
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>board.length == 9</code></li>
#  <li><code>board[i].length == 9</code></li>
#  <li><code>board[i][j]</code> is a digit <code>1-9</code> or <code>'.'</code>.</li>
# </ul>
#
# <div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>矩阵</li></div></div><br><div><li>👍 1173</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def is_valid(self, sub):
        sub = [x for x in sub if sub != '.']
        return len(sub) == len(set(sub))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check each row
        for row in board:
            if not self.is_valid(row):
                return False

        for col in range(9):
            column = [board[row][col] for row in range[9]]
            if not self.is_valid(column):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [
                    board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)
                ]
            if not self.is_valid(sub_box):
                return False

        return True





# leetcode submit region end(Prohibit modification and deletion)

sol = Solution()
bd = [["8","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(bd))

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        sub_box = [
            bd[row][col] for row in range(i, i + 3) for col in range(j, j + 3)
        ]
        print('sub', sub_box[0])