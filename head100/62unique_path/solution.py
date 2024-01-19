class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """ 1  递归"""
        # def stat_path(right, down):
        #     if right == 1 or down == 1:
        #         return 1
        #     return stat_path(right-1, down) + stat_path(right, down-1)
        # return stat_path(m, n)

        """ 2  迭代"""
        # def stat_path(right, down):
        #     if m == 1 or n == 1:
        #         return 1
        #
        #     prev_row = [1] * n
        #     curr_row = [1] * n
        #
        #     for i in range(1, m):
        #         for j in range(1, n):
        #             curr_row[j] = prev_row[j] + curr_row[j - 1]
        #
        #         prev_row = curr_row[:]
        #
        #     return curr_row[-1]
        #
        # return stat_path(m, n)

        """ 3  动态规划"""
        dp = [[0] * n for _ in range(m)]

        # 初始化第一行和第一列的格子
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 计算其他格子的路径数量
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

sol = Solution()
print(sol.uniquePaths(3, 2))