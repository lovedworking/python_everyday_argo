# <p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>
#
# <p><strong>Note:</strong>&nbsp;You must not use any built-in BigInteger library or convert the inputs to integer directly.</p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre><strong>Input:</strong> num1 = "2", num2 = "3"
# <strong>Output:</strong> "6"
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre><strong>Input:</strong> num1 = "123", num2 = "456"
# <strong>Output:</strong> "56088"
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>1 &lt;= num1.length, num2.length &lt;= 200</code></li>
#  <li><code>num1</code> and <code>num2</code> consist of digits only.</li>
#  <li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number <code>0</code> itself.</li>
# </ul>
#
# <div><div>Related Topics</div><div><li>数学</li><li>字符串</li><li>模拟</li></div></div><br><div><li>👍 1306</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        f, t = len(num1), len(num2)
        pos = [0]*(f+t)
        for i in range(f-1, -1, -1):
            for j in range(t-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                total = mul + pos[p2]
                pos[p1] += total // 10
                pos[p2] = total % 10
        res = ''.join(map(str,pos)).lstrip('0')
        return res if res else '0'


sol = Solution()
print(sol.multiply('12', '11'))




# leetcode submit region end(Prohibit modification and deletion)
