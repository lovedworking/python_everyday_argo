# spark

count = count(right) + count(down)

3 * 2

*  *   *

*  *   *


stop

right = 3

down = 2

    [0,0] = [0,1] + [1,0]


## so recursive simple  add

terrible shit !  
time limit exceeded

     def stat_path(right, down):
            if right == 1 or down == 1:
                return 1
            return stat_path(right-1, down) + stat_path(right, down-1)
        return stat_path(m, n)


## interation

        def stat_path(right, down):
            if m == 1 or n == 1:
                return 1

            prev_row = [1] * n
            curr_row = [1] * n

            for i in range(1, m):
                for j in range(1, n):
                    curr_row[j] = prev_row[j] + curr_row[j - 1]

                prev_row = curr_row[:]

            return curr_row[-1]

        return stat_path(m, n)


> 这段代码实现了一个函数 stat_path，它计算从起点到达目标位置的路径数。
>
> 在函数的参数中，right 表示向右移动的次数，down 表示向下移动的次数。
>
> 在函数体内，首先检查如果 right 或者 down 中有一个为
> 1，那么意味着只能直线移动到目标位置，因此返回路径数为 1。
>
> 然后，定义了两个列表 prev_row 和 curr_row，并将它们初始化为长度为 n
> 的列表，每个元素都为 1。这些列表用来存储路径数。
>
> 接下来，使用双重循环进行迭代计算。外层循环从第二行开始，逐行向下遍历（共进行 m-1
> 次迭代）。内层循环从第二列开始，逐列向右遍历（共进行 n-1 次迭代）。
>
> 在每个位置上，路径数等于其左边位置的路径数加上其上方位置的路径数。通过更新
> curr_row[j] 的值，我们逐步计算出每个位置的路径数。
>
> 在内层循环结束后，将 curr_row 的值赋给 prev_row，以便在下一行的计算中使用。
>
> 最后，返回 curr_row[-1]，即最右下角位置的路径数，作为结果。
>
> 在函数的最后，通过调用 stat_path(m, n)
> 来计算从起点到目标位置的路径数，并返回结果。


## dynamic programming

    dp[m][n] = dp[m-1][n] + dp[m][n-1]

the principle to consider is the dynamic expression

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


这个问题可以使用动态规划来解决。我们可以创建一个大小为 m x n 的二维数组 dp，并将所有元素初始化为 0。

对于第一行和第一列的格子，由于机器人只能向下或向右移动，所以到达这些格子的路径只有一条，因此将这些格子的 dp 值设为 1。

然后，对于其他格子 (i, j)，它可以从上面的格子 (i-1, j) 或左边的格子 (i, j-1) 到达，因此它的 dp 值等于上面格子和左边格子的 dp 值之和，即 dp[i][j] = dp[i-1][j] + dp[i][j-1]。

最后，返回 dp[m-1][n-1]，即右下角格子的 dp 值，即为机器人从左上角到达右下角的所有路径数量。
