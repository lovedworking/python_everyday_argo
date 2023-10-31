class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 从右向左找到第一个满足 nums[i] < nums[i+1] 的元素
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找不到满足条件的 i，数组是降序排列的，直接反转为最小排列
        if i < 0:
            nums.reverse()
            return

        # 从右向左找到第一个满足 nums[j] > nums[i] 的元素
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # 交换 nums[i] 和 nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # 反转 i+1 及其之后的元素，使其变为升序排列
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums


sol = Solution()
print(sol.nextPermutation([3, 1, 2]))