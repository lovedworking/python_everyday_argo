# think
every row change into every column
and for i in range N 
row[i]  equals cloumn[i]

1 row[i][j] 变为 row[j][i]
2 every row reverse


这个人的题解比较好
https://leetcode.cn/problems/rotate-image/solutions/1692273/lu-qing-ge-chong-by-pennx-ce3x/

    上下对称：matrix[i][j] -> matrix[n-i-1][j]，（列不变）
    左右对称：matrix[i][j] -> matrix[i][n-j-1]，（行不变）
    主对角线对称：matrix[i][j] -> matrix[j][i]，（行列互换）
    副对角线对称：matrix[i][j] -> matrix[n-j-1][n-i-1] （行列均变，且互换）

