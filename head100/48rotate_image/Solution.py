# <p>You are given an <code>n x n</code> 2D <code>matrix</code> representing an image, rotate the image by <strong>90</strong> degrees (clockwise).</p>
#
# <p>You have to rotate the image <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>, which means you have to modify the input 2D matrix directly. <strong>DO NOT</strong> allocate another 2D matrix and do the rotation.</p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="width: 500px; height: 188px;" />
# <pre>
# <strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
# <strong>Output:</strong> [[7,4,1],[8,5,2],[9,6,3]]
# </pre>
#
# <p><strong class="example">Example 2:</strong></p>
# <img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="width: 500px; height: 201px;" />
# <pre>
# <strong>Input:</strong> matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# <strong>Output:</strong> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# </pre>
#
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>n == matrix.length == matrix[i].length</code></li>
#  <li><code>1 &lt;= n &lt;= 20</code></li>
#  <li><code>-1000 &lt;= matrix[i][j] &lt;= 1000</code></li>
# </ul>
#
# <div><div>Related Topics</div><div><li>数组</li><li>数学</li><li>矩阵</li></div></div><br><div><li>👍 1787</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix
# leetcode submit region end(Prohibit modification and deletion)
sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))