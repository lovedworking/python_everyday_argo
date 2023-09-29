"""
主要考虑什么
数组长度不确定
随机指定一个数组为基准数组
遍历数组 只要在遍历的时候
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        arr = strs[0]
        for i in range(len(arr)):
            for s in strs:
                if i >= len(s) or arr[i] != s[i]:
                    return arr[0:i]

        return arr


sol = Solution()
# print(sol.longestCommonPrefix(["flower","flow","flight"]))
# print(sol.longestCommonPrefix(["av","a"]))
print(sol.longestCommonPrefix([""]))


