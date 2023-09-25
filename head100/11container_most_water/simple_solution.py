"""
设两指针 i , j，
指向的水槽板高度分别为 h[i]h[i]h[i] , h[j]h[j]h[j] ，此状态下水槽面积为 S(i,j)S(i, j)S(i,j) 。由于可容纳水的高度由两板中的 短板 决定，因此可得如下 面积公式 ：

S(i,j)=min(h[i],h[j])×(j−i)
在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 变短：

若向内 移动短板 ，水槽的短板 min(h[i],h[j])min(h[i], h[j])min(h[i],h[j]) 可能变大，因此下个水槽的面积 可能增大 。
若向内 移动长板 ，水槽的短板 min(h[i],h[j])min(h[i], h[j])min(h[i],h[j]) 不变或变小，因此下个水槽的面积 一定变小

解题的思路
当l < r
    1 计算当前面积 取和之前面积比较大值作为最大面积
    2 把小边和大边 逐渐缩小距离
        可能是l 往右靠
        也可能是r 往左靠



"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            res = max(res, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return res

sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

