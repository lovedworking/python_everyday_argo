"""
https://leetcode.cn/search/?q=LCR
回头再搞剑指offer
https://leetcode.cn/problems/zigzag-conversion/description/

https://www.nowcoder.com/exam/oj/ta?page=1&tpId=13&type=13
And then read line by line: "PAHNAPLSIIGYIR"

注意只有在0行 numRows-1 变换方向向 上边界变为加   下边界变为减
最终只保留每一行对应一个字符串

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))











