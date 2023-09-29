
class Solution(object):
    def threeSum(self, nums):

        n = len(nums)
        res = []
        if not nums or n < 3:
            return res
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, n - 1
            while L < R:
                # 如果三数之和是0就添加结果
                # 考虑左侧移动时 判断下一元素是否和当前相等
                # 同理判断右侧时 是否元素和当前相等
                if (nums[i] + nums[L] + nums[R]) == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R - 1] == nums[R]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return res



sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
