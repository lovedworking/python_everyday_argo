"""
注意边界
if -2³¹ <= x <= 2³¹ - 1 :
    return 0
它的语法形式是[start:stop:step]
特殊情况
想到的就是反转字符串
可以锻炼什么
熟练python一些集合使用 但是不好的地方在哪里呢
切片
[start:stop:step]
% 是取模运算符（Modulus Operator），用于计算两个数相除的余数。
/ 是除法运算符（Division Operator），用于执行浮点数除法操作（即得到一个浮点数结果）。
// 是整数除法运算符（Floor Division Operator），用于执行整数除法操作（即得到一个整数结果）。

"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x < 0:
            x = str(x)[::-1]
            x = -int(x)
        else:
            x = str(x)[::-1]
            x = int(x)
        return x if -2**31 < x < 2**31-1 else 0


sol = Solution()
print(sol.reverse(123))