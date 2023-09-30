"""
初版本 勾出框架 但是注意最优
1 先列出框架
2 逐步补充 先补充更新最优解的计算
3 逐步优化 相同的数据不用重复计算了
"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        def best(cur_val):
            nonlocal res
            if abs(cur_val - target) < abs(res - target):
                res = cur_val
        for i in range(n):
            L = i + 1
            R = n - 1
            while L < R:
                s_value = nums[i] + nums[L] + nums[R]
                if s_value == target:
                    return s_value
                elif s_value > target:
                    while L < R and nums[R-1] == nums[R]:
                        R -= 1
                    R -= 1
                    best(s_value)
                else:
                    while L < R and nums[L + 1] == nums[L]:
                        L += 1
                    L += 1
                    best(s_value)
        return res

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))
