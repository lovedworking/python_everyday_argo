"""
python增强表达式定义二维数组   每遍历一行生成一个n的数组
动态规划步骤
1 建立动态方程
2 找出边界条件
3 初始化动态表达式

看图 dp[i][j] 参考左下方的值
a 先升序填列
b 再升序填行



1 状态 动态dp[i][j]表示子串s[i][j]是否为回文串
    dp[i][j] = s[i]== s[j] and ( j - i < 3  or dp[i+1][j-1])
2 边界条件 j-1 - (i+1) + 1 < 2 也就是j-1<3
3 初始化 dp[i][i] = true
得到 dp[i][j]为true 记录起始位置 和 长度


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        # dp[i][j]是否为回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1):
            # 枚举左
            for i in range(n):
                # 由L和i 确定右 j - i + 1 = L
                j = L + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 满足dp[i][j] == true就是 s[i..L 回文
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i +1
                    begin = i
        return s[begin:begin+max_len]



sol = Solution()
print(sol.longestPalindrome("babab"))
