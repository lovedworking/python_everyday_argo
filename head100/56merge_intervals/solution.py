# <p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
#
# <pre>
# <strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
# <strong>Output:</strong> [[1,6],[8,10],[15,18]]
# <strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# </pre>
#
# <p><strong class="example">Example 2:</strong></p>
#
# <pre>
# <strong>Input:</strong> intervals = [[1,4],[4,5]]
# <strong>Output:</strong> [[1,5]]
# <strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
# </pre>
#
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
#  <li><code>intervals[i].length == 2</code></li>
#  <li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
# </ul>
#
# <div><div>Related Topics</div><div><li>数组</li><li>排序</li></div></div><br><div><li>👍 2214</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        res = list()
        for interval in intervals:
            # 如果结果为空 或者结果末尾 小于当前起始 代表不重复 直接加入
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            # 在其他情形 需要合并结果列表最后一个list 最后一个元素和当前list结尾值最大的一项
            else:
                res[-1][-1] = max(res[-1][-1], interval[-1])
        return res

# leetcode submit region end(Prohibit modification and deletion)

sol = Solution()
print(sol.merge([[1, 3], [2, 3], [2, 4]]))
