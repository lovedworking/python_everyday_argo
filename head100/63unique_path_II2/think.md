# spark
compare with 62，the difference is that the obstacle in the path. what
we should do to satisfy the adjustment ? add the condition that if the
square is not the obstacle

"To address the difference compared to 62,  
we need to consider the obstacles in the path.  
One possible solution is to add a condition  
 that excludes squares occupied by obstacles."


 #

    假设我们定义到达右下角的走法数为 f(m,n)f(m, n)f(m,n), 
    因为右下角只能由它上方或者左方的格子走过去，
    因此可以很容易的写出递归求解式，
    即 f(m,n)=f(m−1,n)+f(m,n−1)
    
    然而事情并木有结束～ 因为这样自底向上的递归会存在大量的重复计算
    所以我们将其改写为在二维数组中自顶向下的递推即可，即
    dp[i,j]=dp[i−1,j]+dp[i,j−1]
