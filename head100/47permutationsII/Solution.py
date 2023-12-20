# <p>Given a collection of numbers, <code>nums</code>,&nbsp;that might contain duplicates, return <em>all possible unique permutations <strong>in any order</strong>.</em></p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
#
# <pre>
# <strong>Input:</strong> nums = [1,1,2]
# <strong>Output:</strong>
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# </pre>
#
# <p><strong class="example">Example 2:</strong></p>
#
# <pre>
# <strong>Input:</strong> nums = [1,2,3]
# <strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# </pre>
#
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>1 &lt;= nums.length &lt;= 8</code></li>
#  <li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
# </ul>
#
# <div><div>Related Topics</div><div><li>数组</li><li>回溯</li></div></div><br><div><li>👍 1510</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
            else:
                for i in range(len(nums)):
                    if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                        continue
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path, visited)
                    visited[i] = False
                    path.pop()

        nums.sort()
        res = []
        backtrack([], [False]*len(nums))
        return res


# leetcode submit region end(Prohibit modification and deletion)
sol =Solution()
print(sol.permuteUnique([1, 3, 1]))