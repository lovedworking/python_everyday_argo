# <p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x<sup>n</sup></code>).</p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
#
# <pre>
# <strong>Input:</strong> x = 2.00000, n = 10
# <strong>Output:</strong> 1024.00000
# </pre>
#
# <p><strong class="example">Example 2:</strong></p>
#
# <pre>
# <strong>Input:</strong> x = 2.10000, n = 3
# <strong>Output:</strong> 9.26100
# </pre>
#
# <p><strong class="example">Example 3:</strong></p>
#
# <pre>
# <strong>Input:</strong> x = 2.00000, n = -2
# <strong>Output:</strong> 0.25000
# <strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
# </pre>
#
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>-100.0 &lt; x &lt; 100.0</code></li>
#  <li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li>
#  <li><code>n</code> is an integer.</li>
#  <li>Either <code>x</code> is not zero or <code>n &gt; 0</code>.</li>
#  <li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
# </ul>
#
# <div><div>Related Topics</div><div><li>递归</li><li>数学</li></div></div><br><div><li>👍 1290</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result = result * x
            x = x * x
            n = n // 2
        return result


# leetcode submit region end(Prohibit modification and deletion)

sol = Solution()
print(sol.myPow(2, 4))