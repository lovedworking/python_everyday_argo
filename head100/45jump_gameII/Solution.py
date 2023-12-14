# <p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>. You are initially positioned at <code>nums[0]</code>.</p>
#
# <p>Each element <code>nums[i]</code> represents the maximum length of a forward jump from index <code>i</code>. In other words, if you are at <code>nums[i]</code>, you can jump to any <code>nums[i + j]</code> where:</p>
#
# <ul>
#  <li><code>0 &lt;= j &lt;= nums[i]</code> and</li>
#  <li><code>i + j &lt; n</code></li>
# </ul>
#
# <p>Return <em>the minimum number of jumps to reach </em><code>nums[n - 1]</code>. The test cases are generated such that you can reach <code>nums[n - 1]</code>.</p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
#
# <pre>
# <strong>Input:</strong> nums = [2,3,1,1,4]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# </pre>
#
# <p><strong class="example">Example 2:</strong></p>
#
# <pre>
# <strong>Input:</strong> nums = [2,3,0,1,4]
# <strong>Output:</strong> 2
# </pre>
#
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
#  <li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
#  <li>It's guaranteed that you can reach <code>nums[n - 1]</code>.</li>
# </ul>
#
# <div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>动态规划</li></div></div><br><div><li>👍 2387</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 00
        bound = 0
        far = 0
        n = len(nums)
        for i in range(n-1):
            if i <= far:
                far = max(far, i + nums[i])
                if i == bound:
                    steps += 1
                    bound = far

        return steps
sol = Solution()
print(sol.jump([2,3,0,1,4]))


# leetcode submit region end(Prohibit modification and deletion)
