class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        i = 0
        j = 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                print('匹配到相等 i当前值', i, 'j当前值', j)
                j += 1
            else:
                print('从此不相等了 减之前的i', i, 'j当前值', j)
                i -= j
                print('从此不相等了 减之后的i', i, 'j当前值', j)
                j = 0

            i += 1

        if j == len(needle):
            return i - j
        else:
            return -1

sol = Solution()
haystack = "hello world"
needle = ""
print(sol.strStr(haystack, needle))